'''
需求:完成多任务,使用线程,因为线程比进程更节省资源

'''
import socket
import threading


# 处理客户端请求的操作
def handle_client_request(ip_port, new_client):
    print("客户端的ip和端口号为", ip_port)
    # 收发消息都使用返回的这个新套接字
    # 循环接收客户端的消息
    while True:
        recv_data = new_client.recv(1024)  # 当断开连接时服务端收到的消息是空字符串的空消息
        if recv_data:
            print("接收到的客户端数据的长度为", len(recv_data))
            # 对二进制数据进行解码变为字符串
            recv_content = recv_data.decode('utf-8')
            print("接收到的客户端数据为:", recv_content, ip_port)
            send_message = "问题正在处理中"
            # 对字符串进行编码,变为二进制数据
            send_data = send_message.encode('utf-8')
            # 发送数据到客户端
            new_client.send(send_data)
        else:
            # 客户端关闭连接
            print("客户端下线了", ip_port)
            break
    # 关闭服务端和客户端的套接字,表示终止通信
    new_client.close()


if __name__ == '__main__':
    socket_server = socket.socket()  # 获得一个socket对象
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = 'localhost'
    port = 8888
    socket_server.bind((host, port))
    socket_server.listen(12)
    while True:
        new_client, ip_port = socket_server.accept()
        sub_thread = threading.Thread(target=handle_client_request, args=(ip_port, new_client))
        # 设置守护线程,主线程退出子线程直接销毁
        sub_thread.setDaemon(1)
        sub_thread.start()  # 启动子线程,执行对应的任务

    socket_server.close()  # 关闭服务端的套接字对象,表示服务端不再接收客户端的连接请求

    # 当主线程服务端直接使用按钮销毁时,子线程一并销毁,不会存在stop线程的状态
