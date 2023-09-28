'''
线程的注意点介绍
1.线程之间执行是无序的
2.主线程会等待所有的子线程执行结束再结束
3.线程之间共享全局变量
4.线程之间共享全局变量数据出现错误问题


'''
import time

""" 验证线程之间的执行是无序的
import threading
import time

def task():
    time.sleep(1)
    # 获取当前线程
    current_thread = threading.current_thread()
    print("子线程:", current_thread)
    # for i in range(10):
    #     print("子线程中i:", i)

if __name__ == '__main__':
    # 循环创建大量线程,测试线程之间执行是否无序
    for i in range(20):
        # 每循环一次创建一个子线程
        sub_thread = threading.Thread(target=task)
        # 启动子线程所对应的任务
        sub_thread.start()

    # 线程之间执行是无序的,具体哪个线程执行由操作系统调度完成
"""
'''
# 主线程会等待所有的子线程结束之后再结束

import threading
# 执行一个较长的子线程任务,观察主线程是否会等待子线程执行
def task():
    while True:
        print("子线程执行中...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建一个子线程,将子线程设置为守护主线程,再主线程执行结束后,子线程直接销毁
    # sub_thread = threading.Thread(target=task,daemon=True)
    sub_thread = threading.Thread(target=task)
    # 使用set方法也能够将子线程设置成为守护主线程
    sub_thread.setDaemon(True)
    sub_thread.start()
    # 主线程延迟执行一秒钟
    time.sleep(1)
    print("主线程执行结束")
    exit()
# 通过测试可以发现,即使主线程执行结束,依然要等待子线程执行完成后才会结束,和进程相似
'''

# 线程之间共享全局变量
import threading

g_list = list()


def add_data():
    for i in range(3):
    # 每循环一次将数据添加到全局变量列表中
        g_list.append(i)
        print("add:", i)
        time.sleep(0.1)
    print("添加完成:", g_list)

def read_data():
    for i in range(3):
        print("read:", g_list)

if __name__ == '__main__':
    # 创建添加数据的子线程
    add_thread = threading.Thread(target=add_data)
    # 创建读取数据的子线程
    read_thread = threading.Thread(target=read_data)
    # 启动线程执行对应的任务
    add_thread.start()
    add_thread.join() # 使用join()方法不仅再进程中有用再线程中依旧可以使得join后面的代码等待子线程执行完成后再执行
    # 当前线程等待添加数据的子线程执行完成后再继续执行
    read_thread.start()
    # 结论:线程之间共享数据,原因是线程之间再同一个进程中可以共享该进行的全局变量