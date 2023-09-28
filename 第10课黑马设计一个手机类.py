class Phone():
    # 提供私有成员变量
    __is_5g_enable = True  # 表示5g状态,现在的状态是开启

    def __check_is_5g_enable(self):
        if self.__is_5g_enable == True:
            print("5g开启")
        else:
            print("5g关闭,使用4g网络")

    def call_by_5g(self):
        self.__check_is_5g_enable()
        print("正在通话中")


# Phone.call_by_5g(Phone)  # 创建临时对象
# 创建持久化的对象
phone = Phone()
phone.call_by_5g()