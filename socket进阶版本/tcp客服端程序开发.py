'''
socket类的介绍
导入socket模块
import socket
创建客户端socket对象
socket.socket(AddressFamily,type,proto)

AddressFamily 表示IP地址类型分为IPv4和IPv6。Type 表示传输协议类型
方法说明:
connect(host,port)表示和服务端套接字建立连接,host是服务器ip地址，port是应用程序的端口号
send(data) 表示发送数据，data是二进制数据。
recv(buffersize) 表示接收数据buffersize是每次接收数据的长度
'''

"""
创建tcp客户端套接字
和服务端套接字建立链接
发送数据到服务端
接收数据从服务端
关闭连接套接字
"""
import socket

if __name__ == '__main__':
    client = socket.socket()
    client.connect(('localhost',8888))
    while True:
        client.send("你好".encode('utf-8'))
        receiver = client.recv(1024)
        print("接收到的数据是:",receiver.decode('utf-8'))