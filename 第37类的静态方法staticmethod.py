'''
静态方法
需要在类中封装一个方法,这个方法:
不需要访问实例属性或者调用实例方法
也不需要访问类属性或者调用类方法

本身就是一个单独的功能或者说是模块

这时候可以将这个方法封装成一个静态方法


基本语法
@staticmethod
def 静态函数名():
    pass

注意在静态方法中,不要传入参数self类似于Java中类的对象指针this

静态方法：使用@staticmethod修饰器声明。静态方法没有固定的第一个参数，也没有明确的self 或 cls 参数，它们可以被类的实例或者类本身调用
'''

# 例如创建一个xx系统,但是在xx系统的菜单中只需要使用打印输出的print()方法不需要使用多余的类方法或者是类属性,这时在类中创建一个类的静态方法


class Game:
    @staticmethod
    def menu():
        print("Welcome")
        print("开始[1]")
        print("暂停[2]")
        print("退出[3]")
    def __init__(self,name="飞机大战"):
        self.name = name
        print(name)
        print(self.name)
    def dayin(self):
        print(111)

# 开始游戏打开菜单
Game.menu()
print(Game)
print(Game.dayin()) #在没有为类中实例方法填写self参数的前提下,是会报错的,注意即使将self的参数使用类名代替,但是实质上还是没有创建对象的情况下调用实例方法
# print(Game.__init__(Game))
# 通过验证可以得到,在没有创建类对象的前提下,只是使用类名.方法名()的方法可以调用类中的方法