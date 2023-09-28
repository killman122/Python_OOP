from student import Student

class StudentManger(object):
    def __init__(self):
        # 定义一个列表,存储学员的所有信息
        self.student_list = []

    # 定义load_student_list()方法
    def load_student_list(self):
        pass

    # 定义静态方法show_help()
    @staticmethod
    def show_help():
        print("-" * 40)
        print("黑马通讯录管理系统")
        print("1.添加学员信息")
        print("2.删除学员信息")
        print("3.修改学员信息")
        print("4.查询学员信息")
        print("5.显示所有学员信息")
        print("6.保存学员信息")
        print("7.退出")
        print("-" * 40)

    # 定义一个run()方法,专门用于实现对系统中各个功能的调用
    def run(self):
        # 调用一个方法,用于加载文件中的所有学员信息,将加载后的信息暂存在上面的列表中
        self.load_student()
        # 提示帮助信息,提示用户要实现的功能编号
        while True:
            # 显示帮助信息
            self.show_help()
            # studentManger.show_help()
            # 提示用户输入操作功能的编号
            user_num = int(input("输入要操作的编号\n"))
            if user_num == 1:
                self.add_student()
            elif user_num == 2:
                self.del_student()
            elif user_num == 3:
                self.mod_student()
            elif user_num == 4:
                self.show_student()
            elif user_num == 5:
                self.show_all()
            elif user_num == 6:
                self.save_student()
            elif user_num == 7:
                print("感谢使用学生管理系统")
                break
            else:
                print("信息输入错误")

        pass

    def load_student(self):
        pass

    # 需求:用户输入学员姓名,年龄,手机号,将学员添加到系统中
    # 步骤:
    # p用户输入姓名,年龄,手机号
    # p创建该学员对象
    # p将该学员对象添加到列表可以使用append追加的方式
    def add_student(self):
        name = input("请输入学员的姓名")
        age = input("请输入学员的年龄")
        mobile = input("请输入学员的电话号码")
        # 使用Student类实例化对象
        student = Student(name=name, age=age, phone_number=mobile)
        # 调用student_list类属性,追加信息到列表中,将对象添加到列表中
        self.student_list.append(student) # 在另一种情况下,可以使用列表中存储字典的形式保存数据
        print("学员信息已经添加成功")
        pass

    def save_student(self):
        pass
    # 需求:用户输入目标学员姓名,如果学员存在则删除该学员
    # 步骤:
    # 用户输入目标学员姓名
    # 遍历学员数据列表,如果用户输入的学员姓名存在则删除否则
    def del_student(self):
        del_name = input("输入要删除的学员姓名")
        for i in self.student_list:
            if del_name == i.name:
                print("已经匹配到要删除的学员的信息")
                self.student_list.remove(i)
                print("删除成功")
                break
            else:
                print("该学员似乎不在系统中")
        pass

    def mod_student(self):
        pass

    def show_student(self):
        pass

    def show_all(self):
        pass


 