'''
Process类执行任务并传递给的方式有2种,一种是使用args的元组方式传递参数
一种是通过kwargs的字典方式传递参数
'''
import multiprocessing


def show_info(name, age):
    print(name, age)


# sub_process = multiprocessing.Process(target=show_info, args=("王道", 21)) # 但是需要注意使用元组的方式传递参数,会导致不能变换各个参数之间的位置,如果需要变换位置,只能使用字典方式传入参数
sub_process = multiprocessing.Process(target=show_info, kwargs={"name":"王道","age":21})

# 启动进程
# sub_process.start()
# 注意:不知道是进程启动不能在非主函数或者是非全局函数的内部,总结就是不能将多进程实现在全局代码空间中,甚至通过别的函数调用都可以运行
# def yunxing():
# sub_process.start()

if __name__ == '__main__':
    sub_process.start()
    # yunxing()
