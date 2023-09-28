# account_amount = 0
# def atm(num,deposit=True):
#     global account_amount
#     if deposit:
#         account_amount+= num
#         print(f"存款:+{num},账户余额:{account_amount}")
#     else:
#         account_amount -= num
#         print(f"取款:-{num},账户余额:{account_amount}")
#
# atm(300)
# atm(300)
# atm(300,False)

def account_create(initial_amount=0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款:+{num},账户余额:{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款:-{num},账户余额:{initial_amount}")

    return atm

    # 如果不使用nonlocal关键字修饰,则可以将传入的参数打印,但是不能修改父函数的参数


fn = account_create()
fn(100)
fn(100)

# 使用闭包的方式可以不使用外部的全局变量防止篡改全局变量的数据,当通过import的方式从外部导入的时候
# 但是闭包中类似于全局变量的参数,还是可以通过nonlocal关键字实现更改

'''
使用闭包的优点和缺点
优点:
无需定义全局变量即可实现通过函数,持续的访问修改某个值
闭包使用的变量的作用在函数内,难以被错误的调用修改

缺点:
由于内部函数持续引用外部函数的值,所以会导致这一部分内存空间不被释放,一直占用内存
'''