# 定义一个播放器类
class MusicPlayer(object):
    # 定义一个类属性,使用instance记录之前实例化对象返回的内存引用
    instance = None # 类属性值在类中被更改后,除非类和类对象被删除,否则不会释放内存中的地址
    # 重写__new__()魔术方法
    def __new__(cls, *args, **kwargs):
        # 判断实例化时有没有分配过空间
        if cls.instance is None:
            cls.instance = super().__new__(cls) # 使用new方法分配空间,并在下面返回地址
        return cls.instance


    def __init__(self,name):
        self.name = name

# 实例化mp1对象
mp1 = MusicPlayer('红色高跟鞋')
print(mp1)

# 实例化mp2对象
mp2 = MusicPlayer('蓝色高跟鞋')
print(mp2)

# 在另外的教程中直接为实例化的对象起别名也是一种伪单例模式的方法