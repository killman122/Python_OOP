'''
引言:
当需要大量创建一个类的实例的时候,可以使用工厂模式
从原生的使用类的构造去创建对象的形式
迁移到基于工厂提供的方法去创建对象的形式
'''


# 常见的类的原生的构建方式去创建不同的类对象
'''
class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


worker = Worker()
stu = Student()
teacher = Teacher()
'''

# 工厂模式使用案例
# 使用工厂类get_person()方法创建具体的类对象
# 优点:
# 大批量创建对象的时候有统一的入口,易于代码维护,当发生修改,仅仅修改工厂类的创建方法就可以

class Person:
    pass
class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

class Factory:
    def get_person(self,p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()

factory = Factory()
worker = factory.get_person('w')
student = factory.get_person('s')
teacher = factory.get_person('t')