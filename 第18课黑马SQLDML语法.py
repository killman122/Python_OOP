'''
DML
DML 是指数据操作语言,英文全称是Data Manipulation Language,用来对数据库中的表的数据记录进行更新
关键字:
插入  INSERT
删除  DELETE
更新  UPDATED
'''

# 插入
# 基础语法:
# insert into 表[(列1,列2,...列N)] values(值1,值2,...值N)[,(值1,值2,...,值N),...,(值1,值2,...值N)]
# 使用[]包起来的部分表示可以省略,可以保留

# 创建一个新的表在数据库中
# create table student(
#     id int,
#     name VARCHAR(20),
#     age int
# );

# 仅插入id列数据
# insert into student(id) values(10001),(10002),(10003)
# # 插入全部列数据
# insert into student(id,name,age) values(10001,"周杰伦",31),(10002,"王力宏",33),(10003,"林俊杰",26)
# # 插入全部列数据,快捷写法
# insert into student values(10001,'周杰伦',31),(10002,'王力宏',32),(10003,'林俊杰',32)


'''
数据删除
delete from 表名称 where 条件判断

条件判断: 列,操作符,值
操作符: = <= >= < > != 等
如:id = 5
id < 3
id >= 6
delete from book where id ==1
貌似在多表查询中可以使用xx表名.属性数据
如果delete中没有指定筛选条件直接使用会删除数据库中该表的所有


数据更新
update 表名 set 列=值 [where 条件判断]
update book set name="张学友" where id=4 
当没有筛选条件的条件判断where语句后,如何直接执行update则会将整个数据库中表的所有值都设置为name 后的
'''

# 注意事项:当字符串的值,出现在SQL语句中,必须使用单引号引起
