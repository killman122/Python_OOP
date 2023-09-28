# 可以对查询的结果使用order by关键字,指定某个列进行排序,语法:
# select 列|聚合函数|* from 表 where ... group by ... order by ... [asc|desc]
# drop table if exists student;
# create table student(
#     id int,
#     name varchar(20),
#     age int,
#     gender varchar(10)
# );
#
# insert into student values (10001,'周杰伦',31,'男'),(10002,'王力宏',33,'男'),(10003,'蔡依林',35,'女'),(10004,'林志玲',36,'女'),(10005,'刘德华',30,'男');
#
# # 按照年龄降序排序结果
# select * from student order by age desc;
# # 按照id升序排序结果
# select * from student where age>31 order by id;

# 结果分页查询
'''
使用limit关键字,对查询结果进行数量限制或者是分页显示,语法:
select 列|聚合函数|* from 表 where ... group by ...order by ...[asc|desc] limit n[,m]
limit 后的n和m分别代表开始的显示的数据行数次和显示的数据行数量
select * from student limit 5; 限制5条数据显示
select * from student limit 5,1; 查询的结果集中取第6条开始,取出一条数据就可以
'''