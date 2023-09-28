# 魔术方法 __xx__()叫做魔术方法,指的是具有特殊功能的函数在类中
# __init__() 初始化方法,构造方法,构造器
# 实例化对象时,连带其中的参数,一并传递给init函数自动执行,init函数的第一个参数指的是自己这个对象self
class Person():
    # 初始化实例对象属性
    def __init__(self, name, age):
        # 赋予name属性和age属性给实例化对象本身
        # 将右边的参数复制给左边的属性
        self.name = name
        self.age = age

    # 使用__str__方法更改类的描述,函数内部使用return 返回相关属性实现
    def __str__(self):
        return self.name

    def __del__(self):
        print("调用了函数内部的__del__()删除方法")

# 实例化对象并传入初始化属性值
p1 = Person('孙悟空', 500)
# 调用p1对象自身属性name和age
print(p1.name)
print(p1.age)
print(p1)
# p1.__del__()
# __str__

del p1
# 当删除对象时,解释器默认调用__del__()方法,在其他的编程语言中叫做析构方法,删除方法
# 当在类的外部调用del方法时默认使用类内部的析构函数
# 在一个对象使用完毕时.系统默认调用__del__()方法删除对象节省空间,还可以用于关闭文件,关闭数据库链接等
# __del__
