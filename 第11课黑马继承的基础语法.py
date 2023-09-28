'''
演示面向对象:继承的基础语法

一般的类和静态static类不同,静态类不需要实例化对象即可调用
在多继承中,优先级由左到右,左边的优先继承,优先级高,后继承的右边的属性和方法如果和先继承的重复,则将后继的覆盖
'''


# 演示单继承
class Phone():
    IMEI = None  # 序列号
    profile = "华为"

    def call_by_4g(self):
        print("4G通话")


class Phone2023(Phone):
    face_id = "10010"

    def call_by_5g(self):
        print("2023年新功能5G通话")


phone = Phone2023()
print(phone.profile)
phone.call_by_4g()


# 演示多继承
class NFCReader(object):
    nfc_type = "第五代"
    producer = "红米"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl():
    rc_type = ("红外遥控")

    def control(self):
        print("红外遥控开启了")


class Myphone(Phone2023,NFCReader,RemoteControl):
    pass

myphone = Myphone()
myphone.control()
myphone.call_by_5g()