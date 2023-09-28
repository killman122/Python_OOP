# 使用关键字GROUP BY 关键字 进行分组聚合查询
'''
分组聚合的应用场景非常多,如:统计班级中,男生和女生的人数
这种需求需要:
按照性别分组
统计每个分组的个数
这就称之为:分组聚合

基础语法:
select 字段|聚合函数 from 表 [where 条件] group by 列
select 字段,聚合函数 from 表 [where 条件] group by 列
当在group by 后出现了哪个字段作为筛选的列,那么在前面的select显示中才能选取那个特定的group by 后的字段
在聚合函数中可以填写任意的列或者说是字段的值

聚合函数有:
sum(列)求和
avg(列)求平均值
min(列)求最小值
max(列)求最大值
count(列|*)求数量

例如:求男女分组后的每一种的年龄的平均值
select avg(age) from student group by gender;
'''

# 分组聚合的注意事项?
# group by 中出现了哪个列,哪个列才能出现在select中的非聚合中