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

# 定义一些全局变量
listen               = False
command              = False
upload               = False
execute              = ''
target               = ''
upload_destination   = ''
port                 = 0

"""
这里导入了说有需要的py库并设置了些全局变量。
接下来创建主函数处理命令行参数和调用编写的其他函数。
"""
def usage():
    print('BHP Net Tool\n')
    print('Usage: bhpnet.py -t target_host -p port')
    print('-l --listen              - listen on [host]:[port] for incoming connections')
    print('-c --command             - execute the given file upon receiving a connection')
    print('-u --upload=destination  - initialize a command shell')
    print('-e --execute=file_to_run - upon receiving connection upload a file and write to [dextination]')
    print('')
    print('')
    print('Examples:')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -c')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\'cat /etc/passwd\'')
    print('echo: "ABCDEFGHI" | ./bhpnet.py -t 192.168.11.12 -p 135')
    sys.exit(0)

def main():
    global listen
    global command
    global execute
    global target
    global upload_destination
    global port

    if not len(sys.argv[1:]):
        usage()

    # 读取命令行选项
    l = ['help', 'listen', 'command', 'upload', 'execute', 'target', 'port']
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hel:t:p:cu:", l)
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
        # 发送数据
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
    


main()

















