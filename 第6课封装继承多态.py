# 面向对象有哪些特性,封装继承多态
# 在python中,分装有两层含义:
# 把现实主体中的属性和方法书写到类中的操作称为封装,封装可以为属性和方法添加私有权限

# 公有方法和私有方法
# 公有属性和方法:无论在类的内部还是在类的外部,我们都可以对属性和方法进行操作
# 但是在某些情况下,我们不希望在类的外部对类内部的属性和方法进行操作,我们就可以将这个属性或方法封装成私有形式

# 在python中设置私有属性和方法的方式非常简单:在属性名和方法名前加两个下划线"__"
# 类中的私有属性和方法不能被子类所继承
# 在python和Java中,一般定义函数名为'get_xx',和'set_xx'来获取和设置私有属性作为接口

class Girl():
    def __init__(self,name):
        self.name = name
        self.__age = 18

    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return self.__age

girl = Girl('王小美')
print(girl.get_age())
