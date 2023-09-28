# 闭包:在函数嵌套的前提下,内部函数使用了外部函数的变量,并且外部函数返回了内部函数,我们把这个使用外部函数变量的内部函数称为闭包
'''
def outer(loge):
    def inner(msg):
        print(f"<{loge}>{msg}<{loge}>")

    return inner  # 将函数本身作为返回值返回,而不是将函数的调用作为返回值返回


fn1 = outer("黑马程序员") # 返回值是一个内部的函数inner(),但是也起到了打印输出的作用
fn1("大家好") # fn1相当于对函数inner的引用,并且传入的参数直接作用于inner()函数
fn1("学习python")

fn2 = outer("传智教育")
fn2("IT职业教育机构")
fn2("学习python就来")
'''


# 修改外部函数变量的值
def outer(num1):
    def inner(num2):
        nonlocal num1
        num1 += num2 # 在内层函数的内部可以修改外层函数中的参数的取值
        print(
            num1
        )

    return inner


fn = outer(10)
fn(10) # 20
fn(10) # 30
