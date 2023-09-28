# filter(func,lst) 用于过滤序列,但是在多个python的库中都有这个函数提供过滤(筛选)的功能
# 返回一个filter对象,如果想转换为列表,可以使用list()来转换


def func(n):
    return n % 2 == 0
list1 = [1,2,3,4,5,6,7,8,9]
# 调用filter函数进行过滤操作
result = filter(func, list1)
print(list(result))