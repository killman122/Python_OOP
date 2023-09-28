# 在文件夹中使用鼠标右键后,点击创建python包,在包创建好后,存在一个__init__.py文件
'''
什么是Python包
包将所有的联系的模块组织在一起,放在同一个文件夹下,并且在这个文件夹中创建一个名字叫做"__init__.py"的文件
那么这个文件夹称为包

在文件夹中创建模块 mypackage1 and mypackage2

导入包
方法一:
import 包名.模块名
包名.模块名.目标

import python自定义包.my_model1
mypackage1.mymodel1.func1()

方法2
注意:必须在'__init__.py'文件中添加'__all__=[]',控制允许导入的模块列表
这里导入的模块列表使用__init__.py只能限制一次性导入多个,如 from xxx import *,但是如果拆成多个分别的import,是可以继续导入
__all__ = ['my_model1','my_model2']

'''