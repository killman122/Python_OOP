# 可以先写出类名
# 写出这个类中的所有属性
# 定义出这个类所具有的动作

class Person(object):
    def __init__(self,food=None):
        self.food = food

    def eat(self,food=None):
        print("我喜欢吃零食")

    def drink(self,food=None):
        print("我喜欢喝可乐")

person = Person()
person.eat()
print(person) # 显示出这个对象的地址
# 在java ,js等语言中,类的实例化一般是通过new关键字实例化生成的,但是在python中只需要类名+()代表类的实例