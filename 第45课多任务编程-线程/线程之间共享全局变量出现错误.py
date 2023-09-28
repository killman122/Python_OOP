import threading
import time

# 定义两个函数,实现循环1000000次给全局变量加1
g_num = 0


def add1():
    global g_num  # 全局变量g_num是不可变得,需要使用global关键字,除非使用列表,字典等可变类型,也只是限于append(),extend(),remove()方法,如果使用赋值语句,也需要使用global关键字
    for i in range(1000000):
        g_num += 1
    print("add1:", g_num)


def add2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("add2:", g_num)


if __name__ == '__main__':
    sub_thread1 = threading.Thread(target=add1)
    sub_thread2 = threading.Thread(target=add2)
    sub_thread1.start()
    # time.sleep(1) # 此处为添加延迟的代码,线程等待,让第一个线程先执行,然后第二个线程在执行,这样就可以保证数据的正确性,但是这样就失去了多线程的意义
    sub_thread1.join() # 主线程等待第一个子线程执行完成后再继续执行
    # 线程等待是属于线程同步的一种方式
    # 线程同步:保证同一时刻只有一个线程去控制全局变量 同步:就是协调步调,按照预定的先后次序去执行
    # 线程同步的方式:线程等待(join)和互斥锁

    sub_thread2.start()
    # time.sleep(1) # 如果不添加时间的等待再执行下面的输出语句时,由于两个子线程和当前的主线程并发执行,但是执行后的结果不一定是2000000,因为主线程执行完毕后,两个子线程可能还没有执行完毕,
    # 所以输出的结果可能是小于2000000的 并且由于数据之间没有加锁进行保护,所以数据会出现错误,当多个线程操作一个数据,可能会出现数据的赋值冲突,虽然添加延迟可以避免,但是就失去了多线程的作用
    print(g_num, f"{threading.current_thread()}线程执行结束")
