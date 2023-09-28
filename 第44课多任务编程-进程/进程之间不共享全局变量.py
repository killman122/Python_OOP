import multiprocessing
import os
import time
# 定义全局变量列表
g_list = list()

def add_data():
    for i in range(3):
        # print(i)
        # 因为列表是可变类型可以在原有内存的基础上修改数据,并且修改后内存地址不变,所以不需要添加global关键字
        # 加上global 表示要修改声明全局变量的内存地址
        g_list.append(i)
        print(f"add{i}")
        time.sleep(0.2)
        print(f"输出现在使用的进程id{os.getpid()}")
    print(f"添加完成列表为{g_list}")

def read_data():
    for i in range(3):
        print("read_data函数已经执行")
        print(f"read:{g_list}")
        print(multiprocessing.current_process())



"""
在Mac和Linux（Unix风格操作系统）中，由于使用了fork()系统调用，父进程的状态（包括全局变量等） 在子进程中会被复制一份，但是父进程和子进程之后的更改不会影响到对方。
而在Windows中，由于操作系统不支持fork()，Python会启动一个新的解释器实例载入脚本，这相当于对主进程代码的重新执行，因此在全局范围内启动子进程会导致无限递归创建新的解释器实例，从而导致问题。
但需要指出的是，不止是start()代码，实际上在Windows中，所有全局范围内的代码，在创建新的子进程时都会再次执行。为了避免这种无限递归的问题，我们使用if __name__ == '__main__':来保证只在脚本初次执行时执行某些代码，当脚本作为模块导入时（如在创建子进程时），这部分代码不会执行。
所以，一个更准确的描述可能是：“在Windows中，由于使用了新的Python解释器实例来加载脚本并执行全局范围的代码，因此，在全局范围内启动子进程（不仅仅是start()函数）可能会导致无限递归创建子进程，因此我们需要把相关代码放入 if __name__ == '__main__':中以避免这个问题。”
"""
if __name__ == '__main__':
    # 添加数据的子进程
    add_process = multiprocessing.Process(target=add_data)
    # 读取数据的子进程
    read_process = multiprocessing.Process(target=read_data)
    # 读取数据的子进程
    add_process.start()
    add_process.join()
    # 当前进程等待添加数据的进程执行完成后继续往下执行代码
    read_process.start()
    print(g_list)
# 通过测试可以得到使用两个进程之间并不能实现共享变量
# 结论:进程之间不共享全局变量
# 创建子进程其实是对主进程资源的拷贝,子进程其实就是主进程的一个副本,子进程中对全局变量的操作不会影响到包括主进程的所有进程

'''
对于mac和linux来说:主进程执行的代码不会进行拷贝(当子进程创建并启动后),但是对于windows来说,当子进程运行后对于的主进程代码也会运行,虽然全局变量依旧不会发生更改
提示:多于mac和linux主进程执行的代码不会进行拷贝,但是对于windows来说主进程执行的代码也会进行拷贝执行
对于windows来说创建子进程的代码(这里主要是启动的start()代码),如果进程拷贝执行相当于无限递归创建子进程会报错
'''
