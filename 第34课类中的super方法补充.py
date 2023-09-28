class Car():
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def run(self):
        print("I can run")


class GasCar(Car):
    # 在编写构造器的时候,由于和父类存在继承关系,所以不用重写构造器,增加代码冗余,但是如果想加入新的属性如何处理,适用超类构造器,super
    def __init__(self,brand,model,color,money,speed):
        super().__init__(brand, model, color)
        self.money = money
        self.speed = speed

    def run(self):
        print("油车能跑")

car= Car('宝马','X7','白色')
gascar = GasCar('奔驰','迈巴赫','黑色','7000000',320)
print(car.model)
gascar.run()
print(gascar.model)
print(gascar.speed)
# def __init__(self, brand, model, color, money, speed):
    #     self.brand = brand
    #     self.model = model
    #     self.color = color
    #     self.money = money
    #     self.speed = speed
