"""
    用python创建一个tcp服务端和创建客户端一样简单。
    你可能需要将自己的tcp服务端绑定到命令行shell或创建一个代理(这两个需求我们之后完成)
    首先，我们创建一个标准的多线程tcp服务器，
    大体的代码结构如下：
"""
import socket
import threading

bind_ip = '0.0.0.0'
bind_prit = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_prit))
server.listen(5)
print('[* ] listening on %s:%d' % (bind_ip, bind_prit))

# 这是客户处理线程
def handle_client(client_socket):
    # 打印出客户端发送得到的内容
    request = client_socket.recv(1024)
    print('[* ] received: %s' % request)
    data = 'ack!'
    # 返还一个数据包
    client_socket.send(data.encode(encoding="utf-8"))
    client_socket.close()

while True:
    client, addr = server.accept()
    print('[* ] Accepted connection from: %s:%d' % (addr[0], addr[1]))
    # 挂起客户端线程，处理传入的数据
    client_handlee = threading.Thread(target=handle_client, args=(client,))
    client_handlee.start()


"""
    首先，我们确定服务器需要监听的IP地址和端口。
    然后，我们启动监听并将最大连接数设为5。
    下一步，我们让服务端进入主循环中，并在这里等待连接。

    当一个客户端成功建立连接的时候，
    我们将接收到的客户端套接字对象保存到client变量中，
    将远程连接的细节保存到addr变量中。

    接着，我们以handle_client 函数为回调函数创建了一个新的线程对象，
    将客户端套接字对象作为一个句柄传递给它。

    然后我们启动线程开始处理客户端连接。
    handle_ client 函数执行recv()函数之后将一段信息发送给客户端。

    如果你使用我们之前编写的TCP客户端，那么你就可以发送一个测试数据包到服务器端，你将看到以下输出:
    [*] Listening on 0.0.0.0:9999
    [*] Accepted connection from: 127.0.0.1:62512
    [*] Received: ABCDEF
    就是这样!非常简单，但的确是非常有用的一段代码。在接下来的两节里，
    我们将在此基础上扩展建立一个netcat替代工具和-一个TCP代理。 

    注意：
        handle_client 函数为回调函数此方法为新线程，如js的异步回调函数
"""














