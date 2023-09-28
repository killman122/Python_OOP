# reduce()函数
'''
reduce(func,lst),其中func必须有两个参数,每次func计算的结果继续和序列的下一个元素作累加运算,注意reduce()传入的参数func必须接收两个参数
list1= [1,2,3]
def func(a,b)
    return a+b
reduce(func,lst)把列表中的每个元素放入func中进行加工,然后进行累加操作
'''
import functools
# 定义一个函数
def func(a,b):
    return a+b
# 定义一个列表
list1 = [10,20,30,40,50]
sums = functools.reduce(func, list1)
print(sums)