# 死锁:一致等待对方释放锁的场景叫做死锁

# 需求:多线程同时根据下标在列表中取值,要保证同一时刻只能有一个线程去取值
import threading

# 创建一个互斥锁
lock = threading.Lock()

def get_value(index):
    lock.acquire() # 上锁
    my_list = [1,4,6]
    # 判断列表下标是否越界
    if index >= len(my_list):
        print("下标越界:",index)
        # 当下标越界时,直接return结束函数,不执行后面的代码,会进入死锁状态
        # 取值不成功也需要释放互斥锁,不要影响后面的线程取值
        lock.release() # 解锁
        return
    # 根据下标取值
    value = my_list[index]
    print(value)
    lock.release() # 解锁
    print(f"打印现在的线程是什么{threading.current_thread()}")


if __name__ == '__main__':
    # 创建多个线程,同时去执行下标取值的函数
    for i in range(10):
        sub_thread = threading.Thread(target=get_value,args=(i,))
        sub_thread.start()