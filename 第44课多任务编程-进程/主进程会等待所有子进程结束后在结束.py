import multiprocessing
import time

def task():
    # for i in range(10):
    while True:
        print("任务执行中")
        time.sleep(0.3)

if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    # 1.设置守护进程,把子进程设置成为守护进程,主进程退出,子进程直接销毁
    # sub_process.daemon = True

    # 启动子进程
    sub_process.start()

    # 主进程延迟0.5s
    time.sleep(0.5)

    # 2.在主进程退出前,先让子进程销毁
    sub_process.terminate()
    print("程序执行完毕") # 当执行完主线程代码时,主线程并未结束,而是等待子线程执行,当子线程都执行完毕后,主线程结束退出

# 结论:主进程会等待子进程执行完毕后程序在退出

# 当一个需求,子进程是一个无限循环无法退出,正常情况下会导致主进程也无法退出,但是按照需求必须在主进程执行完后退出,不必等待子进程,那么需要使用守护进程
# 解决办法:主进程退出,子进程销毁
# 1.让子进程设置成为守护主进程,主进程退出子进程销毁,子进程会依赖主进程
# 2.让主进程退出之前,先让子进程销毁