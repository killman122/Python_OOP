# self是python中内置的关键字之一,指向了类实例对象本身

# 定义一个类
class Person(object):
    def speak(self):
        print(self)
        print("nice to meet you")


# 类的实例化(生成对象)
p1 = Person()
print(p1)
p1.speak()