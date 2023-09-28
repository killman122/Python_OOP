# 想要在python中操作mysql数据库,需要使用第三方库pymysql
import pymysql

# 连接mysql数据库使用pymysql模块,在学习过面向对象后可以发现这里导入的模块其实都是使用模块中的类,并将类的对象实例化
from pymysql import *

# 获取到mysql数据库的链接对象
# 使用注解的方式在类中,似乎能够有效的指出是哪里的方法,或者是说成员函数实现了什么
connection = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='wjr107024'
)

# 打印mysql数据库的软件信息
# print(connection.get_server_info())

# 在获取游标对象后能够执行sql命令
cursor = connection.cursor()
# 选择数据库
connection.select_db("黑马_sql")
# 执行连接后的操作,执行正常的sql语句
cursor.execute('show tables;')
# cursor.execute('create table test_table(name  varchar(20));')  # 在使用pymysql执行sql语法时,实际上可以省略';'的使用
cursor.execute('ALTER TABLE test_table ADD COLUMN age INT')  # 在使用pymysql执行sql语法时,实际上可以省略';'的使用,在已经创建好的数据库表中添加新的类,标识新的属性字段
cursor.execute('select * from student')
# 获取查询结果,并将结果存储在一个元组对象中
results: tuple = cursor.fetchall()
print(results)
# 元组作为返回的数据类型需要遍历元组中的每一个元素,当然也可以直接输出元组的结果
for row in results:
    print(row)

# 关闭当前数据库的链接
connection.close()

# with connection:# 在使用的过程中可以观察数据的格式,不难发现这种链接并不是一个简单的从属于类的对象,而是作为拓展的方法来链接数据库
#     connection.db()

'''
可以使用with的方式自动关闭数据库的链接在使用完成后
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             database='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
'''
