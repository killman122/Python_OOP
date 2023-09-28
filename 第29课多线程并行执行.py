# 使用threading 模块进行多线程
'''
threading 模块
import threading
thread_obj= threading.Thread([group[,target[,name[,args[kwargs]])
group:暂时无用,未来功能的预留参数
target:执行的目标任务名也就是函数名
args:以元组的方式给执行任务传参
kwargs:以字典的方式给执行任务传参
name:线程名,一般不用设置
thead_obj.start()
构建出多少个thread对象就有多少个线程

'''
import time
import threading


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # sing()
    # dance()
    # 创建线程对象
    # th1 = threading.Thread(target=sing)
    # TODO:注意在多线程模块中目标只有函数名,不能包括函数的()
    # th2 = threading.Thread(target=dance())
    # th1.start()
    # th2.start()
    # 创建线程对象并调用
    th1 = threading.Thread(target=sing,kwargs={"msg":"我在唱歌"}).start() # 注意在传入参数时元组需要加,或者是两个以上的参数
    th2 = threading.Thread(target=dance,args=("我在跳舞",)).start()  # 当创建出的对象没有赋值给变量时,相当于对象作为一个临时变量使用,没有办法从别的地方引用这个对象
