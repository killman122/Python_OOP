import pymysql
from pymysql import *

connection = Connection(
    host='localhost',
    port=3306,  # 注意在创建数据库的链接时如果产生黄色的警告,实际上时是错误语法的使用,可能是数据库中的数据类型写错
    user='root',
    password='wjr107024',
    autocommit=True
)

with connection:
    cursor = connection.cursor()  # 获取一个游标对象
    connection.select_db('黑马_sql')
    # 执行sql语句
    cursor.execute("insert into student value ('10006','张学油',39,'男')")
    # 在执行完上面的命令后可以发现,数据库中并没有保存该数据,也就是将插入的数据保存在数据库中
    # pymysql在执行数据的插入或者是其他产生数据更改的SQL语句时,默认是需要提交更改行为
    # 通过使用链接对象.commit()能够确认这个行为,如果不想手动确认这个提交更改的请求,可以在连接时设置autocommit属性为True
    # connection.commit()
