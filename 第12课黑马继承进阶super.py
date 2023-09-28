class Phone():
    IMEI = None # 序列号
    producer = "ITCAST" # 厂商

    def call_by_5g(self):
        print("使用5G网络进行通话")


# 定义子类,复写父类成员
class MyPhone(Phone):
    producer = "IRHEIMA"

    def call_by_5g(self):
        print("开启Cpu单核模式,确保通话时省电")
        # print("使用5g网络进行通话")
        # 方式1
        # print(f"父类的厂商是:{Phone.producer}") # 直接输出父类的属性,但是这里似乎没有实例化对象
        # Phone.call_by_5g(self) # 创建一个零时的变量用来存储对象
        # 方式2 超类的方式运行
        print(f"父类的厂商是{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式,确保性能")


myphone = MyPhone()
myphone.call_by_5g()
print(myphone.producer) # 实现了复写方法和属性

'''
一旦复写父类成员,那么类对象调用成员的时候,就会调用复写后的新成员,如果需要
使用被复写的父类的成员,需要使用特殊的方式
方式1:
调用父类成员
使用成员变量:父类名.成员变量
使用成员方法:父类名.成员方法(self)

方式2:
使用super()调用父类成员
使用成员变量:super()成员变量
使用成员方法:super().成员方法()

super():调用父类的属性或者是方法,完整写法:  super(当前类名,self).属性或方法()    但是在新版的python中直接适用super().属性/super().方法
'''