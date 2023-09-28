'''
python在3.5版本的时候引入了类型注解
类型注解:在代码中涉及数据交互的地方,提供数据类型的注解(显式的说明)
主要功能:
帮助第三方IDE对代码类型进行推断,协助代码做提示
帮助开发者自身对变量进行类型注释(备注)

支持:变量的类型注解
    函数(方法)形参列表返回值的注解类型
'''
import json
import random

"""
为变量设置类型注解
基础语法:   变量:类型

基础数据类型注解
var_1: int = 10
var_2: float = 13.121
var_3: bool = True
var_4: str = "itheiam"

类对象类型注解
class Student():
    pass
stu: Student = Student()


基础容器类型注解
my_list: list = [1,2,3]
my_tuple: tuple = (1,2,3)
my_set: set = {1,2,3}
my_dict: dict = {"name":"Student"}
my_str: str = "Student"

容器类型详细注解
my_list: list[int] = [1,2,3] 对于列表类型数据的注解不能像使用元组的注解可以分别指定其中每个元素的类型注解
my_tuple: tuple[str,int,bool] = ("学生",100,True)
my_set: set[int] = {1,2,3}
my_dict: dict[str,int] = {"name":666}

注意:元组类型设置类型详细解释,需要将每一个元素都标记出来
字典类型设置类型详细注解,需要2个类型,第一个是key,第二个是value
"""
var_1: int = 10
var_2: float = 13.121
var_3: bool = True
var_4: str = "itheiam"


# 使用注释的方式在代码中进行注解
# 语法: type: 类型
class Student():
    pass


var_1 = random.randint(1, 10)  # type: int
var_2 = json.loads("{'name':'王道','age':21.0}")  # type: dict[str, float]


def func():
    return 10
    pass


var_4 = func()  # type: int
