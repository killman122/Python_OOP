"""
首先导入线程模块threading

线程类Thread参数说明
Thread([group [, target [, name [, args [, kwargs]]]]])
group: 线程组，目前只能使用None
target: 线程执行的函数名
name: 线程名
args: 传入target函数的参数，以元组的形式传入
kwargs: 传入target函数的参数，以字典的形式传入
daemon: 布尔值，表示是否是守护线程,守护线程会在主线程结束时自动退出,防止在子线程中出现僵尸线程也就是说当子线程为一个死循环时,如果不设置守护线程,那么主线程结束时,子线程会继续执行导致主线程无法结束,如果设置了守护线程,那么主线程结束时,子线程会自动结束,和进程相似
启动线程
启动线程使用start方法，而不是run方法，否则只是执行了一个函数，没有启动线程
"""

# 导入多线程模块
import threading
import time


def sing():
    # 获取当前线程
    thread1 = threading.current_thread()  # 此处的用法和进程中的用法相同
    print("sing:", thread1)
    for i in range(3):
        print("在唱歌")
        time.sleep(1)


def dance():
    # 获取当前线程
    thread2 = threading.current_thread()  # 此处的用法和进程中的用法相同
    print("dance:", thread2)
    for i in range(3):
        print("在跳舞")
        time.sleep(1)



# # 创建线程类对象的实例化thread
# thread_sing = threading.Thread(target=sing)
# thred_dance = threading.Thread(target=dance)
# thread_sing.start()

if __name__ == '__main__':
    # 获取主线程中的当前线程
    current_thread = threading.current_thread()
    print("main_thread:", current_thread)
    # 创建线程类对象的实例化thread
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)
    thread_sing.start()
    thread_dance.start()

'''
通过在主程序/主线程中实现start方法,可以直接调用,似乎可以避免和进程之间的拷贝和下面的进程处理不同,当然在主线程的
对于mac和linux来说:主进程执行的代码不会进行拷贝(当子进程创建并启动后),但是对于windows来说,当子进程运行后对于的主进程代码也会运行,虽然全局变量依旧不会发生更改
提示:多于mac和linux主进程执行的代码不会进行拷贝,但是对于windows来说主进程执行的代码也会进行拷贝执行
对于windows来说创建子进程的代码(这里主要是启动的start()代码),如果进程拷贝执行相当于无限递归创建子进程会报错
'''
