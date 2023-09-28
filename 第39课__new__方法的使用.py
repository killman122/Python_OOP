'''
使用类名()创建对象时,python解释器会首先调用__new__方法为对象分配空间
new 是一个有object提供的内置的静态方法,主要作用有两个:
返回对象的引用
在内存中为对象分配空间

传递给__init__方法重写__new__方法的代码非常固定,一定要使用
return super().__new__(cls),否则python解释器得不到分配的空间的对象的引用,就不会调用对象的初始化方法
'''


class MusicPlayer(object):
    # 重写__new__()魔术方法
    def __new__(cls, *args, **kwargs): # 以元组方式传递参数和以列表方式传递参数
        print("1.开辟内存空间")
        print("2.返回实例化对象引用地址")
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name


# 实例化mp1对象
mp1 = MusicPlayer('红色高跟鞋')
# 可以发现在创建对象时,一定会调用__new__()方法
print(mp1)
print(mp1.name)
mp2 = MusicPlayer('蓝色高跟鞋')
print(mp2)
print(mp2.name)


