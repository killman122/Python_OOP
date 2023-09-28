'''
获取进程编号的目的:
获取进程编号的目的是验证主进程和子进程的关系,可以得知子进程是由哪个主进程创建出来的
获取进程编号的两个操作:
获取当前进程编号    获取当前父进程编号

获取当前进程编号:
os.getpid()表示获取当前进程编号
获取当前父进程的编号:
os.getppid()表示获取当前父进程编号

'''
import os
import multiprocessing
import time


# 跳舞任务
def dance():
    # 获取当前进程编号
    print("dance:", os.getpid())
    # 获取当前进程
    print("dance:", multiprocessing.current_process())
    for i in range(5):
        print("跳舞中...")
        time.sleep(0.2)
        # 拓展,根据进程号杀死进程
        # os.kill(os.getgid(), 2)   os.kill(os.getgid(),9) kill 9 强制杀死


def sing():
    # 获取当前进程编号
    print("sing:", os.getpid())
    # 获取当前进程
    print("dance:", multiprocessing.current_process())
    for i in range(3):
        print("唱歌中")
        time.sleep(0.5)


# 获取当前进程的编号
main_process_id = os.getpid()  # 注意此处只是获取当前进程的编号,但是实际上还没有运行上面的两个函数
print(f"当前的主进程id为main_pocess_id:{main_process_id}")
# 获取当前进程对象,查看当前代码是由哪个进程执行的
print(f"当前对象中,代码是由{multiprocessing.current_process()}进程执行,当前进程的pid为{os.getpid()}")

dance_process = multiprocessing.Process(target=dance)
sing_process = multiprocessing.Process(target=sing)

# dance_process.start()
# sing_process.start()

# dance_process.join() 等待该进程执行完毕才可进入下一个进程
if __name__ == '__main__':
    dance_process.start()
    sing_process.start()

# 注意:如果在全局范围内创建和开始进程,在全局范围中开始一个进程,将不间断的开始新的进程,导致无穷递归,所有与进程创建和开始的代码应该放在局部的环境中,或者放在mian模块中
'''
理解多进程的关键在于理解当您开始一个新的进程时，实际上操作系统会启动一个新的Python解释器实例，并重新加载您的脚本。
在Windows上使用Python的multiprocessing模块，与在Unix/Linux上的行为略有不同。Unix/Linux使用fork()系统调用来创建新的进程，而新的进程将继承父进程的全局状态。相反，Windows不支持fork()，所以Python启动一个全新的Python解释器实例。
当这个新的解释器实例开始运行，它会从头开始执行你的脚本。这就是每次当您创建一个新的进程，全局级别的代码就会重新执行。
但是这里需要注意的关键之处是，虽然新的Python解释器实例会从头开始执行你的脚本，但是它仅仅只会执行在if __name__ == '__main__':语句块中的代码。新的解释器实例知道自己是作为一个子进程创建的，所以__name__变量不会被设置为'__main__'，那些位于if __name__ == '__main__':语句块中的代码不会被执行。
所以，在编写使用了multiprocessing模块的Python脚本时，要确保所有的全局级别的代码（也就是说不在函数或方法中的代码）应当放在if __name__ == '__main__':语句块中，防止这些被意外地运行多次。
'''