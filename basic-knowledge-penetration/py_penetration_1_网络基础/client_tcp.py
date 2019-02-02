""" 
    在渗透测试的过程中，我们经常会遇到需要创建一个TCP客户端来连接服务、发送垃圾数据、进行模糊测试或者进行其他任务的情况。
    如果你工作在一个独立的大型企业网络环境中，那么你不会拥有丰富的网络工具或者编译器，
    你甚至可能会在一个不具备基本的复制和粘贴功能或者失去互联网连接的环境下工作。
    在这种环境下，你需要迅速手动创建-一个TCP客户端。
    多说无益，我们开始编写代码。
    下面是一个简单的TCP客户端。

    TCP（Transmission Control Protocol 传输控制协议）:是一种面向连接的、可靠的、基于字节流的传输层通信协议，由IETF的RFC793定义。

    UDP应用于及时通信，而TCP协议用来传送文件、命令等操作，因为这些数据不允许丢失，否则会造成文件错误或命令混乱。
    下面代码就是模拟客户端通过命令行操作服务器。
    客户端输入命令，服务器执行并且返回结果。
"""
import socket
from lib import *


host_ip = helper.get_host_ip()
target_host = '127.0.0.1'  #标准的ipv4地址或主机名
target_port = 9999

# 建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到客户端
client.connect((target_host,target_port))

# 发送一些数据
contents = 'GET / HTTP/1.1\r\nHost:'+ target_host +'\r\n\r\n'
client.send(contents.encode())

# 接受一些数据
response = client.recv(4096)

print(response)

"""
    1.创建一个包含AF_INET和SOCK_STREAM参数的socket对象
        AF_INET         说明我们将使用标准的ipv4地址或主机名
        SOCK_STREAM     说明这将是一个tcp客户端
    2.然后我们将客户端链接服务器并发送一些数据
    3.最后一步是接受返回的数据并将相应数据打印出来

    在以上代码段中，你应该注意到我们对套接字做了一定的假设：
        第一条假设就是连接总是能成功建立，不会出错或异常;
        第二条假设是服务器总是期望客户端能首先发送数据(与之相反的是服务器首先向你发送数据并等待你的响应);
        第三条假设是服务器每次都能及时返回数据。

    我们做这些假设主要是为了方便起见。
    当然，程序员会有各种方法处理套接字阻塞、套接字异常，以及与之相关的情况。
    渗透测试人员很少对自己编写的、用于侦查和攻击的“短平快”的工具添加以上细节，所以我们将在本章中忽略它们。

"""

""" 
注意:
    1. connect() 接受一个参数 connect((主机名,端口))
    2. send() 向服务器端发送编码后的数据（二进制字节）,编码方法encode(),解码decode()
        :::py3需要如此,py2书上列子没有
        python3只能收发二进制数据，需要显式转码
"""

