# 基础数据查询
# 在SQL中,通过select关键字开头的SQL语句,来进行数据的查询
# 基础语法:select 字段列表|* from 表

'''
演示
首先查找要丢弃的表是否存在,如果存在则丢弃该表
drop table if exists student;其中的student是数据库中表名
create table student(
    id int,
    name varchar(10),
    age int
);
insert into student values(10001,'周杰伦',31),(10002,'王力宏',33),(10003,'林俊杰',35),(10004,'张学友',36),(10005,'刘德华',30);

查询id和name两个列
select id,name from student;
查询全部列
select id,name,age from student;
查询全部列的快捷写法
select * from student;
'''

"""
基础查询数据-过滤
查询可以带有指定条件:
select 字段列表|* from 表 where 条件判断
"""