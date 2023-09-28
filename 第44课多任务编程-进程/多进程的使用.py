# 导入进程包
import multiprocessing

'''
在multiprocessing模块中,其中__init__.py文件已经导入了Process类,所以在调用时直接导入就行 

Process ([group[,target[,name[,args[,kwargs]]]])
group:指定进程组,目前只能使用None
target: 执行的目标任务名
name: 进程名字
args: 以元组的方式给任务执行传参
kwargs: 以字典的方式给执行任务传参

Process创建的实例对象的常用方式:
start():启动子进程实例(创建子进程)
join():等待子进程执行完毕
terminate():不管任务是否完成,立即终止子进程

Process创建的实例对象的常用属性:
name: 当前进程的别名,默认为Process-N,N为从1开始的递增的整数
'''
import time
import multiprocessing


def sing():
    while True:
        print("在唱歌")
        time.sleep(1)


def dance():
    while True:
        print("在跳舞")
        time.sleep(1)


if __name__ == '__main__':
    mul_sing = multiprocessing.Process(target=sing)
    mul_dance = multiprocessing.Process(target=dance)
    print(mul_sing)
    mul_sing.start()
    mul_dance.start()
    # 注意:进程之间的执行是无序的,具体哪个进程先执行是由操作系统调度决定的
    # mul_dance.join()
    # 不使用join()方法不影响使用多进程的执行任务
