'''
操作数据库的SQL语言,可以基于功能,划分为4类
数据定义:DDL(Data Definition Language)
库的创建,删除,表的创建删除

数据操纵:DML(Data Definition Language)
新增数据,删除数据,修改数据等

数据控制:DCL(Data Control Language)
新增用户,删除用户,密码修改,权限管理

数据查询:DQL(Data Query Language)
基于需求查询和计算数据
'''

'''
SQL 语言,大小写不敏感
show databases;
SHOw tables;

SQL语言通过';'结束一行的命令

SQL支持注释:
单行注释:-- 注释内容(--后面一定要加一个空格)
单行注释: # 注释内容(# 后面可以不加空格,但是推荐加上)
多行注释: /* 注释内容 */
'''

"""
查看数据库
show databases;

使用数据库
use databases;

创建数据库(在创建数据库名的时候可以设置中文)
create database xxx charset utf8;
CHARACTER SET utf8

删除数据库
drop database xxx;
注意在删除数据库的时候没有条件判断if语句

查看当前使用的数据库
select database();

查看有哪些表
show tables;

删除表
drop table 表名称;
drop table if exists 表名称;

创建表
create table 表名称(
    列名称 列类型,
    列名称 列类型,
    ....
);
列类型有
int  --整数
float --浮点数
varchar --文本,长度为数字,()括号内做最大长度限制
date --日期类型
timestamp --时间戳类型

如果数据库中的表已经创建,但是想要在数据库中添加新的字段(也就是列),不能使用insert(insert是向数据库中添加行的操作),需要使用 ALTER TABLE 语句配合 ADD COLUMN 来进行操作
如:ALTER TABLE test_table ADD COLUMN age INT;

"""
# use world;
# show tables;
# create table student(
#     id int,
#     name varchar(10),
#     age int
# );

