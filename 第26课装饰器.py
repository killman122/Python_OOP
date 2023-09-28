'''
装饰器:
装饰器其实也是一种闭包,其功能是在不破坏目标函数原有的代码和功能的前提下,为目标函数增加新的功能

def sleep():
    import random
    import time
    print("睡眠中")
    time.sleep(random.randint(1,5))

希望为sleep函数增加一个新功能:
在调用sleep前输出:我要睡觉啦
在调用sleep后输出:我起床了
'''


# 一般写法,不通过装饰器
# def outer(func):
#     print("我要睡觉了")
#     func()
#     print("我起床了")
#
# def sleep():
#     import random
#     import time
#     print("睡眠中")
#     time.sleep(random.randint(1,5))
#
# fn = outer(sleep)
# fn()

# 通过装饰器的一般写法(一般闭包写法)
# def outer(func):
#     def inner():
#         print("我要睡觉了")
#         func()
#         print("我起床了")
#
#     return inner
#
# def sleep():
#     import random
#     import time
#     print("睡眠中")
#     time.sleep(random.randint(1,5))
#
# fn = outer(sleep)
# fn()

# 装饰器的语法糖闭包写法,简易的真正意义上的闭包
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")

    return inner


# 使用装饰器后相当于可以不使用闭包的内部函数的调用,而是直接通过闭包自动调用
@outer
def sleep():
    import random
    import time
    print("睡眠中")
    time.sleep(random.randint(1, 5))


sleep()
