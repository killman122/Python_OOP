'''
多态.指的是:多种状态,即完成某个行为时,使用不同的对象会得到不同的状态
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("汪汪汪")
'''


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)  # 将原本应该填入是父类的方法填入子类
make_noise(cat)  # 同样的行为体现出不同的多态性质

# dog.make_noise() # 无法使用该方式调用
# 可以发现在父类的speak方法中是一个空实现,具体的实现是通过子类的方法实现,需要父类确定有哪些方法
'''
这种设计方法的含义是:
父类确定有哪些方法
具体方法的实现,由子类决定

这种写法,叫做抽象类,也可以称之为接口     接口的统称在多个语言中都适用
抽象类:含有抽象方法的类称之为接口
抽象方法:方法体是空实现的(pass)称之为抽象方法
'''


# 抽象类实现

class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调核心制冷科技")

    def hot_wind(self):
        print("美的空调电热丝加热")

    def swing_l_r(self):
        print("美的空调无风感左右摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调变频省电制冷")

    def hot_wind(self):
        print("格力空调电热丝加热")

    def swing_l_r(self):
        print('格力空调静音左右摆风')


# 使用注解将参数注解是ac对象并从属于AC空调类
def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)

# 使用抽象类创建父类接口,但是并不实现具体的方法,而是由子类实现在父类中所确定的子类方法
# 通过多态抽象类实现父类的顶层设计,子类是实现具体