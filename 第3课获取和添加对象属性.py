# 类的属性就是特征
# 对象属性既可以在类对象外面添加和获取也可以在类里面添加和获取
# 在类的外面添加属性和获取属性
# 对象.属性 = 属性值

# 在类的内部获取类外部定义的属性
class Person():
    def speak(self):
        print(f"我的名字:{self.name}")

person = Person()
person.name = "王道"
person.speak()