"""
bind((host,port)):注意参数的填写方式要求是元组类型数据,表示绑定端口号,host是ip地址,port是端口号,IP地址一般不指定,表示本机的所有ip地址
listen (backlog)表示设置监听，backlog参数表示最大等待建立连接的个数
accept()表示等待接受客户端的连接请求send(data) 表示发送数据,data是二进制数据
recv(buffersize) 表示接收数据,buffersize 是每次接收数据的长度
"""

# 创建socket对象
import socket

socket_server = socket.socket()  # 获得一个socket对象

# 设置端口号复用,在程序退出后端口立即释放,防止在关闭程序后端口启用较慢,影响端口复用
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = 'localhost'
port = 8888
# 绑定socket_server到指定的IP和地址
socket_server.bind((host, port))

# 服务端开始监听端口
# socket_server.listen(__backlog=1)
socket_server.listen(1)
# backlog为int整数,表示允许的连接数量,超出则等待,可以不填,不填会自动设置一个合理值

# 接收客户端连接,获得连接对象,连接对象第一个参数是客户端的连接对象,第二个参数是客户端的地址信息(是元组数据类型)
print(
    socket_server.accept())  # (<socket.socket fd=396, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8888), raddr=('127.0.0.1', 2506)>, ('127.0.0.1', 2506))
# conn = socket_server.accept()[0] 客户端和服务端的链接对象
# address = socket_server.accept()[1] 客户端的地址信息,客户端的ip地址和端口号
# 注意:每次当服务端和客户端连接成功会返回一个新的套接字对象和地址信息
# 套接字socket_server只负责等待客户端的连接请求,收发消息不使用该套接字
conn, address = socket_server.accept()  # 使用元组的形式,返回,conn表示客户端和服务端的链接对象,address表示客户端的地址信息
# 代码执行到此,客户端和服务端之间建立链接成功

print(f'接收到客户端连接,客户端的信息是:{address}')
# accept方法是阻塞方法,如果没有连接,会卡在这一行不在向下执行代码
# accept返回的是一个二元元组,可以直接使用两个变量接收二元元组的元素,和字典中items()的遍历相似,直接赋值给元组

# 接收客户端的信息,要使用客户端和服务端的本次链接服务,而非socket_server对象
# 客户端连接后,使用recv方法,接收客户端发送的消息
while True:
    data: str = conn.recv(1024).decode('utf-8')  # 使用注解并对二进制数据进行解码
    # recv方法的返回值是字节数组Bytes,可以通过decode使用utf-8解码为字符串
    # recv方法的传参是buffersize,缓存区大小,一般设置为1024
    if data == 'exit':
        break
    print("接收到发来的数据:", data)
    # 向客户端发送消息
    date: str = input('输入你要发送的消息')
    conn.send(f"{date}".encode("utf-8"))

conn.close()  # 关闭新创建的返回的套接字对象
socket_server.close()
# 可以通过while True无限循环来持续和客户端的数据交互
# 可以通过判断客服端发来的特殊标记,如exit,来退出无限循环
# 通过使用conn(客户端当次连接对象),调用send方法可以回复消息
# conn(客户端当次连接对象)和socket_server对象调用close方法,关闭连接
