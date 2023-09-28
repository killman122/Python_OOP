'''
互斥锁的概念:对共享数据进行锁定,保证同一时刻只能有一个线程去操作
注意:互斥锁是多个线程一起去抢,抢到锁的线程才能去操作共享数据,没有抢到锁的线程只能等待

互斥锁的使用
threading模块中定义了Lock类,可以使用这个类来创建互斥锁对象
# 创建锁
mutex = threading.Lock()
# 上锁
mutex.acquire()
使用共享数据之前先上锁
这里编写代码保证同一时刻只能有一个线程去操作共享数据
# 释放锁
mutex.release()
'''
import threading, time

g_num = 0
mutex = threading.Lock() # 创建一个互斥锁的锁对象


def add1():
    # 上锁
    mutex.acquire()
    global g_num  # 全局变量g_num是不可变得,需要使用global关键字,除非使用列表,字典等可变类型,也只是限于append(),extend(),remove()方法,如果使用赋值语句,也需要使用global关键字
    for i in range(1000000):
        g_num += 1
    print("add1:", g_num)
    # 释放锁
    mutex.release()



def add2():
    # 上锁
    mutex.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    print("add2:", g_num)
    # 释放锁
    mutex.release()


if __name__ == '__main__':
    sub_thread1 = threading.Thread(target=add1)
    sub_thread2 = threading.Thread(target=add2)
    # mutex.acquire() # 上锁
    sub_thread1.start()
    # mutex.release() # 释放锁
    sub_thread2.start()
    print(g_num, f"{threading.current_thread()}线程执行结束")
    '''
    如果将锁放在主线程中，比如在if __name__ == '__main__':代码块中，显然不能保证数据的一致性和完整性，因为主线程和其他启动的线程是并发运行的，主线程中对锁的操作（获取和释放锁）并不能对其他线程中的操作产生影响。我们必须把对锁的操作放在需要同步的代码段中，也就是对全局变量g_num操作的代码段中，这样才能确保同一时间只能有一个线程操作此全局变量。
总的来说，我刚才说的是为什么要在对全局变量g_num操作的代码段中加锁，而不能在主线程中加锁。其主要原因是在线程之间同步控制的目的地是要保护特定代码段或者资源，而不仅仅是限制主线程的访问，因此要把锁的操作放在被保护的代码或资源的上下文中。
    '''
    # 互斥锁可以保证在同一时刻只能有一个线程去操作共享数据,从而保证数据的完整性和一致性,但是不能确保哪个函数或任务抢占执行
    # 无论是使用线程等待join还是互斥锁Lock类都相当与将多线程的操作,临时转为了单线程中的操作,将多任务临时抓换为了单任务,保证了数据的安全但是执行的效率下降

# 上锁和解锁是在要执行的多线程函数内部进行的,而不是在主线程中进行的,因为主线程中的代码是顺序执行的,如果在主线程中进行上锁和解锁,那么就会导致两个子线程不能同时执行,失去了多线程的意义
