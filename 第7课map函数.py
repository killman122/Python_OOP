# map(func,lst),将传入的函数变量func作用到lst变量的每个元素中,并将结果组成为新的列表/迭代器传入
# lst = [1,2,3]
# func函数:求某个数的平方,如输入2返回4,输入3返回9

def func(n):
    return n**2

# 定义一个列表
list1 = [1,2,3]
list2 = list(map(func, list1)) # 第二个参数为可迭代的对象,第一个参数是要执行的函数

print(list2)
