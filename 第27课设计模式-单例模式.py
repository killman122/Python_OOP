"""
引言:
某些场景下,我们需要一个类无论获取多少次类对象,都仅仅提供一个具体的实例用以节省创建类对象的开销和内存开销
比如某些工具类,仅仅需要创建一个实例,即可在各处使用

单例模式
定义:保证一个类只有一个实例,并提供一个访问它的全局访问点
适用场景:当一个类只能有一个实例,而客户可以从一个众所周知的访问点访问它时
"""

class StrTools:
    pass

str_tool = StrTools()

s1 = str_tool
s2 = str_tool
print(s1)
print(s2) # 输出对象地址后,发现两个不同名的实际上是同一个对象的实现