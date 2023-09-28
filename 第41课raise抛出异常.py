# 在python中,抛出自定义异常的语法为raise 异常类对象
# 需求:密码长度不足,则报异常(用户输入密码,如果输入的长度不足6,则报错,即抛出自定义异常,并捕获该异常)

# 原生方法
# def input_password():
#     passwd = input("Enter your password 不少于6位:")
#     if len(passwd) < 6:
#         # 抛出异常
#         raise Exception('你的密码长度少于6位') # Exception是python中所有异常类的基类
#         return
#     # 如果密码长度正常,则直接显示密码
#     print(passwd)
# input_password()


# 面向对象抛出自定义异常,如果是自定义异常类,则必须继承于Exception异常基类
class ShortInputError(Exception):
    # length代表输入的密码长度,min_length代表ShortInputError最小密码长度
    def __init__(self,length,min_length):
        self.length = length
        self.min_length = min_length

    def __str__(self):
        return f'您输入的密码长度为{self.length}位,不能少于{self.min_length}个字符'


def main():
    try:
        password = input('Enter your password\n')
        if len(password)<6:
            raise ShortInputError(len(password),6)
    except Exception as e:
        print(f"Error:{e}")
    else:
        print(f"Password输入符合长度需求")

if __name__ == '__main__':
    main()