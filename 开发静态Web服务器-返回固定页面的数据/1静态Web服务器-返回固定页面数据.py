import socket

if __name__ == '__main__':
    # 创建一个tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口号
    tcp_server_socket.bind(('localhost', 8888))
    # 设置监听
    tcp_server_socket.listen(129)  # 最大有129个连接可以等待监听
    # 如果不加while 循环执行一次后只能连接一个客户端,为了实现多端通信,可以采用while True无限循环
    # 循环等待接受客户端的连接请求
    while True:
        # 等待接受客户端的连接请求
        new_socket, ip_port = tcp_server_socket.accept()
        # 代码执行到此说明连接建立成功
        # 接受客户端的请求信息
        recv_data = new_socket.recv(4096)
        print(recv_data)
        # recv_data = recv_data.decode('utf-8')
        # 打开文件读取文件中的数据,这里的文件指的是网页的静态资源文件
        with open('static/index.html', 'r') as file:  # 这里的file表示打开文件的对象
            # 即使file_data在with语句外面也可以使用,因为with语句会自动关闭文件
            file_data = file.read()  # 使用readline是读取一行,但是可以使用while循环来读取多行,使用readlines是读取所有行,返回一个列表,可以铜鼓遍历列表得到每一行,使用read也是读取整个文件
            '''
            尽管 file_data 在一个with语句中被创建，但该变量在 with语句块执行完成后仍然存在，因为它并不是在函数内部被创建的，而是在全局的范围内创建的。with语句并不像函数或类定义那样引入新的作用域。
因此，file_data 在 with块之后仍然是可见的，并且可以像你的代码那样打印它。这是因为Python的作用域规则是基于函数的，而不是基于块的。这样，当然，这个 file_data 变量并不会影响到与它名字相同的其他局部变量。
总的来说，尽管 file_data 严格来说并不是局部变量，但你仍然需要小心在代码的其他地方不要使用同样的变量名，避免引起混淆。
            '''
        # 将数据分装成HTTP 响应报文的格式数据
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Server: PWS1.0\r\n"
        # 响应空行,已经添加了\r\n可以不用再次添加换行和回车
        # 响应主体
        response_body = file_data
        # 组装响应报文数据
        response_data = response_line + response_header + '\r\n' + response_body
        # 发送响应报文数据给客户端,将字符串编码成二进制,发送给浏览器的响应报文
        new_socket.send(response_data.encode('utf-8'))
        # 关闭服务于客户端的套接字,表示和客户端终止通信
        new_socket.close()
        # 服务端tcp_server_socket不能关闭,关闭则相当于停服