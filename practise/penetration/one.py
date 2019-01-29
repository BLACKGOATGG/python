import socket

target_host = '10.200.21.32'  #服务器的ip，和上面的server.py对应
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
注意:
    1. connect() 接受一个参数 connect((主机名,端口))
    2. send() 向服务器端发送编码后的数据（二进制字节）,编码方法encode(),解码decode()
        :::py3需要如此,py2书上列子没有
    3. 


"""





















