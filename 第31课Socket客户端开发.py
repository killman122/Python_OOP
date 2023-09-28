# 创建socket对象
import socket
socket_client = socket.socket() # 获得一个socket对象

host = 'localhost'
port = 8888
# 连接到服务端的ip和端口
socket_client.connect((host, port))

# 发送消息
while True: #可以通过无限循环来保持发送消息给服务端
    send_msg = input("请输入要发送的信息")
    if send_msg == "exit":
        # 通过特殊标记来确保可以退出无限循环
        break
    socket_client.send(send_msg.encode("utf-8"))
    # 在使用send方法发送消息时需要将消息编码发送
    # 使用recv方法接收消息
    recv_msg = socket_client.recv(1024)
    # recv是阻塞式的接收函数,如果不接受到消息会持续等待消息的响应
    print("服务端回复消息为:",recv_msg.decode("utf-8")) # 需要对接收到的消息进行解码

socket_client.close()