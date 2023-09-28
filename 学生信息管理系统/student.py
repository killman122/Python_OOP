class Student:
    def __init__(self,name,age,phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return f"姓名{self.name}年龄{self.age}电话号码{self.phone_number}"
