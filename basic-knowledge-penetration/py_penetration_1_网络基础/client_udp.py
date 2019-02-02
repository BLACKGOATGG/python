""" 
    python编写的udp客户端和tcp客户端差别不大，仅需要做两处简单的修改，将数据包以udp格式发出

    UDP:用户数据报协议，是一个面向无连接的协议。
    采用该协议不需要两个应用程序先建立连接。
    UDP协议不提供差错恢复，不能提供数据重传，因此该协议传输数据安全性差。

    UDP应用于及时通信，而TCP协议用来传送文件、命令等操作，因为这些数据不允许丢失，否则会造成文件错误或命令混乱。
    下面代码就是模拟客户端通过命令行操作服务器。
    客户端输入命令，服务器执行并且返回结果。
"""
import socket
from lib import *


host_ip = helper.get_host_ip()
target_host = '127.0.0.1'  #标准的ipv4地址或主机名
target_port = 80

# 建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送一些数据
contents = 'GET / HTTP/1.1\r\nHost:'+ target_host +'\r\n\r\n'
client.sendto(contents.encode(),(target_host,target_port))

# 接受一些数据
data, addr = client.recvfrom(4096)

print(data, addr)

"""
    在创建嵌套字对象时，将嵌套字的类型改为SOCK_DGRAM
    之后调用sendto将数据传到你想发送的服务器上
    因为udp是一个无连接状态的传输协议，所以不需要在此之前调用connect()函数，
    最后一步是调用recvfrom()接受返回的udp数据包，
    你将接受回传的数据以及远程主机的信息和端口号
"""

""" 
注意:
    1. sendto() 向服务器端发送编码后的数据（二进制字节）,编码方法encode(),解码decode()
        :::py3需要如此,py2书上列子没有
        python3只能收发二进制数据，需要显式转码
"""

