# 需求:定义学员信息类,包含姓名,成绩属性,定义打印成绩的方法(90分以上显示为优秀,80分以上显示为良好,70分以上显示为中等,60分以上显示为及格,60分以下定义为不及格)

class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        if self.score > 90:
            print(f'{self.name},{self.score}分,成绩优秀')
        elif self.score > 80:
            print(f'{self.name},{self.score}分,成绩良好')
        elif self.score > 70:
            print(f"{self.name},{self.score}分,成绩中等")
        elif self.score > 60:
            print(f"{self.name},{self.score}分,成绩及格")
        else:
            print(f"{self.name},{self.score}分,成绩不及格")


student1 = Student('张三', 99)
student2 = Student('里斯', 66)
student1.print_score()
student2.print_score()
