import socket
from lib import *


host_ip = helper.get_host_ip()
target_host = host_ip       # 这是客户端的电脑的ip
target_port = 13141         # 接口选择大于10000的，避免冲突
bufsize = 1024              # 定义缓冲大小

addr = (target_host,target_port)                                # 元组形式
udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # 创建客户端   

while True:
    contents = input('>>> ')
    if not contents:
        break

    contents = contents.encode(encoding="utf-8")                # 处理数据
    udpClient.sendto(contents,addr)                             # 发送数据

    responseData, responseAddr = udpClient.recvfrom(bufsize)   # 接收数据和返回地址
    print(responseData.decode(encoding="utf-8"), 'from', responseAddr)

udpClient.close()


