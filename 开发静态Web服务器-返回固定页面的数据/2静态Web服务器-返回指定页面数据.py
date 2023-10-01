'''
根据访问的网址返回指定页面的数据,在浏览器中输入什么url,则在服务端响应跳转到指定URL的服务:
'''

import socket
import os

def main():
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
        if len(recv_data) == 0:
            # 判断接受的数据长度是否为0,如果接受的数据长度为0,则直接return不再向下运行
            new_socket.close() # 当没有数据发送时,直接将返回的新的套接字对象直接关闭
            return
        # 需要对二进制数据进行解码
        recv_content = recv_data.decode('utf-8')
        print(recv_content)
        request_list = recv_content.split(' ',
                                          maxsplit=2)  # maxsplit=2表示分割两次,分割两次后,后面的内容不再分割,在默认情况下,分割次数是无限次,maxsplit=-1表示无限次
        # 通过split()分割获取请求的资源路径,也可以使用正则表达式来获取,或者是使用字符串的find()方法来获取,也可以使用字符串的切片来获取
        # 需要判断数据是否为空,如果数据为空,则不执行后续代码,因为数据为空,由于使用字符串的split()方法返回的是一个列表,如果数据输入为空,则列表为空,无法使用列表下标取值,会出现列表index索引越界从而引发异常
        request_path = request_list[1]
        # 判断请求的是否是根目录,如果是根目录设置返回的信息,直接返回到index.html主页
        if request_path == '/':
            request_path = '/index.html'
        # 第一种方式判断文件是否存在,如果文件不存在,则返回404错误
        os.path.exists("static/"+request_path)
        # 第二种方式判断文件是否存在,可以直接使用try..except的方式捕获异常,如果捕获到异常,则说明文件不存在,则返回404错误
        # recv_data = recv_data.decode('utf-8') # decode解密
        # 打开文件读取文件中的数据,这里的文件指的是网页的静态资源文件
        try:
            with open('static' + request_path,
                      'rb') as file:  # 这里的file表示打开文件的对象,打开的格式类型为,二进制数据读取模式,由于需要使用图标文件ico所有不能直接使用r的文本读取模式打开数据,所以在次使用rb模式打开文件
                # 即使file_data在with语句外面也可以使用,因为with语句会自动关闭文件
                file_data = file.read()  # 使用readline是读取一行,但是可以使用while循环来读取多行,使用readlines是读取所有行,返回一个列表,可以铜鼓遍历列表得到每一行,使用read也是读取整个文件
                # 由于以二进制可读模式打开文件,所以read()读取数据的过程中使用的是二进制的方式,所以读取到的数据也是二进制数据,所以在发送响应报文数据的时候不需要进行编码
                '''
                尽管 file_data 在一个with语句中被创建，但该变量在 with语句块执行完成后仍然存在，因为它并不是在函数内部被创建的，而是在全局的范围内创建的。with语句并不像函数或类定义那样引入新的作用域。
    因此，file_data 在 with块之后仍然是可见的，并且可以像你的代码那样打印它。这是因为Python的作用域规则是基于函数的，而不是基于块的。这样，当然，这个 file_data 变量并不会影响到与它名字相同的其他局部变量。
    总的来说，尽管 file_data 严格来说并不是局部变量，但你仍然需要小心在代码的其他地方不要使用同样的变量名，避免引起混淆。
                '''
        except Exception as e:
            # 代码执行到此,说明服务器没有请求中的该文件,返回404状态信息
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            # 响应空行,已经添加了\r\n可以不用再次添加换行和回车
            with open("static/error.html", "rb") as file:
                file_data = file.read()
            # 响应主体
            response_body = file_data
            # 组装响应报文数据 response_data = b"response_line + response_header + '\r\n'" + response_body 的方式是错误的
            # 注意在b''字节字符串的方法使用过程中无法处理变量,没有类似于格式化字符串中槽的概念,如果数据中含有变量,那么在变量的处理过程中,需要将变量转换为二进制数据,然后再进行拼接,这里用到的转换的方法是使用encode方法
            response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            new_socket.send(response_data)

            pass
        else:
            # 代码执行到此说明文件存在路径中,返回200状态信息
            # 将数据分装成HTTP 响应报文的格式数据
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            # 响应空行,已经添加了\r\n可以不用再次添加换行和回车
            # 响应主体
            response_body = file_data
            # 组装响应报文数据 response_data = b"response_line + response_header + '\r\n'" + response_body 的方式是错误的
            # 注意在b''字节字符串的方法使用过程中无法处理变量,没有类似于格式化字符串中槽的概念,如果数据中含有变量,那么在变量的处理过程中,需要将变量转换为二进制数据,然后再进行拼接,这里用到的转换的方法是使用encode方法
            response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            new_socket.send(response_data)
            # 发送响应报文数据给客户端,将字符串编码成二进制,发送给浏览器的响应报文
            # new_socket.send(response_data.encode('utf-8'))  # encode加密
            # 关闭服务于客户端的套接字,表示和客户端终止通信
        finally:
            new_socket.close()
            # 服务端tcp_server_socket不能关闭,关闭则相当于停服


if __name__ == '__main__':
    main() # 由于使用return 必须在函数中,所以为了防止在调用函数的时候出现异常,将main在中的代码分装在一个函数中