import socket

target_host = '10.200.21.32'  #标准的ipv4地址或主机名
target_port = 80

# 建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到客户端
client.connect((target_host,target_port))

# 发送一些数据
client.send('GET / HTTP/1.1\r\nHost:10.200.21.32\r\n\r\n'.encode())

# 接受一些数据
response = client.recv(4096)

print(response)

"""
    1.创建一个包含AF_INET和SOCK_STREAM参数的socket对象（7）
        AF_INET         说明我们将使用标准的ipv4地址或主机名
        SOCK_STREAM     说明这将是一个tcp客户端
    2.然后我们将客户端链接服务器（10）并发送一些数据（13）
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
    3. 
"""

