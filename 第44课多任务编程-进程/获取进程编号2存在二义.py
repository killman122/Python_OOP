import multiprocessing
import time,os

# 跳舞任务
def dance():
    for i in range(3):
        print("跳舞中...")
        time.sleep(0.2)

# 唱歌任务
def sing():
    for i in range(3):
        print("唱歌中...")
        time.sleep(0.2)

# 获取当前进程(主进程)的编号
main_process_id = os.getpid()
print("main_process_id:", main_process_id)


dance_process = multiprocessing.Process(target=dance)
sing_process = multiprocessing.Process(target=sing)

# 启动进程执行时对应的任务
# dance_process.start()
# sing_process.start()

# 进程的执行是无序的,具体哪个进程执行由操作系统调度完成
if __name__ == '__main__':
# 启动进程执行时对应的任务
    dance_process.start()
    sing_process.start()

# 只要创建多线程变量不是在函数的局部作用域,否则在执行时,由于python机制的原因相当于创建新的解释器,但是使用该解释器在main中调用start方法,会导致全局变量和中间式子都会执行