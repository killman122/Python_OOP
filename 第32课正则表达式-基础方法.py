import re

'''
python 正则表达式,使用re模块,并基于re模块中三个基础方法作为正则匹配
三个方法分别是:match,search,findall
re.match(匹配规则,被匹配字符串)
从被匹配的字符串开头进行匹配,匹配成功返回匹配对象(包含匹配的消息),匹配不成功返回空
'''

# re.match(r'') 案例
s = 'python it黑马 python itheima'
result = re.match(r'python', s)
print(result)
print(result.span())  # 打印出的数据是匹配到的结果下标,从下标0开始到下标,由于元组的特性算头不算尾
print(result.group())  # 打印出查找到的分组也就是匹配到的字符串的信息

# 但是使用re.match()方法只能匹配到字符串的开头,如果字符串的开头不匹配则返回数据none,不会向后查找
s = 'itpython it黑马 python'
result = re.match(r'python', s)
print(result)

# 使用search(匹配查找,找出匹配的,从前向后,找到第一个后,就停止,不会继续向后查找,如果整个字符串都没有找到,返回None)
s = '666666666学习python找工作,进大厂88888888888888'
result = re.search(r'python', s)
print(result)
print(result.span())
print(result.group())


# 使用findall(匹配规则,被匹配字符串),匹配整个字符串返回全部找到的数据
s = 'ipython666itheima6666python6666'
result = re.findall('python',s)
print(result)

# 如果找不到返回空list: []
result = re.findall('itcast',s)
print(result)