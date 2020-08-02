# # 自动调整代码格式ctrl + alt + L
# from turtle import *  #turtle 绘图
# forward(100)
# left(120)
# forward(100)
# left(120)
# 使用原始字符保留字符原来内容
print(r'hello \nworld')
# 使用\ 进行转义
print('hello \'world' + 'ljy')
print('wzn is a \N{pig}!')
# 数据结构之列表和元组
# 列表：可修改，所有元素都放在方括号中，并用逗号隔开
# 元组：不可修改
wzn = ['Wang Zining', 'sex: \N{pig}', 'age:24']
ljy = ['Liu Jingyuan', 'sex: male', 'age:18']
database = [wzn, ljy]  # 两个列表重新组成一个列表数组
database2 = wzn + ljy  # 将两个列表拼接起来成一个列表，注意和上面的区别
print(database[0][1][1])
print(database2[0][1])
# 练习1(索引)：要求输入年、月（数1-21）、日（数1-31），再使用相应的月份名等将日期打印出来：
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
# 一个列表，其中包含数1~31对应的结尾
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
          + ['st', 'nd', 'rd'] + 7 * ['th'] \
          + ['st']
year = input('Year: ')  # input只获取键盘输入的值，与括号内原来的字符串无关，括号内原来的字符串只是起到了提示用户输入的作用
month = input('Month(1-12): ')
day = input('Day(1-31): ')
month_number = int(month)
day_number = int(day)
# 不要忘了将表示月和日的数减1才能找大正确的索引
month_name = months[month_number - 1]
day_name = day + endings[day_number - 1]
print(month_name + ' ' + day_name + ' ' + year)

# 切片：访问特定范围内的元素，可使用两个索引，并用冒号隔开
# example： 取元组后三个元素 a[-3:],取元组第二到最后的元素，a[2:],取第五个到倒数第四个元素a[5:-4]
##练习2（切片） 从类似看i与http://www.something.com的URL中提取域名
url = input('Please enter the URL :')
domain = url[11:-4]
print("Domain name : " + domain)
# 切片中更大的步长
# 切片的格式：  a[起始索引:终止索引:步长] 其中三个都可以为负数，步长为负数表示从右向左
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex1 = a[-1:-5:-2]
ex2 = a[1:10:3]
print(ex1 + ex2)
#   +号的使用，用以同一类型的类型拼接
b = [1, 2, 3, 4]
c = [5, 6, 7]
d = b + c
print(d)
#   *号的使用，用于倍数重复序列
a = 'wzn is a ' + '\N{pig}' * 5
print(a)
#   None关键字：表示列表中什么都没有
a = [None] * 10
# 1print(a[1][1])  # None关键字表示什么都没有 不是字符串

# 练习3：序列（字符串）乘法运算实例，在位于屏幕中央且宽度合适的方框内打印一个句子
sentence = input('please input what you want to say:')
boxwidth = 80  # 方框宽度为80个字符
box_left = 10  # 左数第十个字符为起始位置
box_right = boxwidth + box_left
l = len(sentence)
sentence_left = (boxwidth - l) / 2 + box_left
print(' ' * box_left + '\N{pig}' + (boxwidth - 2) * '-' + '\N{pig}')
print(' ' * box_left + '|' + (boxwidth - 1) * ' ' + '|')
print(' ' * box_left + '|' + (boxwidth - 1) * ' ' + '|')
print(' ' * box_left + '|' + int(sentence_left - box_left) * ' ' \
      + sentence + int(sentence_left - box_left-1) * ' ' + '|')
print(' ' * box_left + '|' + (boxwidth - 1) * ' ' + '|')
print(' ' * box_left + '|' + (boxwidth - 1) * ' ' + '|')
print(' ' * box_left + '\N{pig}' + (boxwidth - 2) * '-' + '\N{pig}')
# 🐖------------------------------------------------------------------------------🐖
# |                                                                               |
# |                                                                               |
# |                                       dsad                                    |
# |                                                                               |
# |                                                                               |
# 🐖------------------------------------------------------------------------------🐖
#   成员资格运算符号in：用于检查特定的值是否在序列中，满足时返回True，不满足返回False
#   内置函数len，max，min分别返回序列包含的元素个数、最大值和最小值
#   练习4：序列成员资格示例，检查用户名和PIN码是否在database中
database = [
    ['Liujingyuan', '180'],
    ['Wangzining', '190'],
    ['Giao', '165'],
    ['Yao', '226'],
]
username = input('Please input your name:')
pin = input('please input your pin code:')
seq = [username, pin]
print(len(database))
if seq in database:
    print("Access granted!")
else:
    print("No permitted!")
# 列表和元组：
# 列表：列表是可变的，动态的，支持增删改查
# 常用的列表操作示例
names = ['Alice', 'Beth', 'Cecil', 'Dee-dee', 'Earl']
print(names)
# 删除列表中第三个元素，也可以用names[2:] = []操作
del (names[2])
print(names)
# 给切片赋值
names[2:] = ['ljy', 'wddw', 'dadada', '123']  # 改变从第三个之后的元素，可比原来的序列多，也可以少,因为列表的长度是可变的
print(names)
# num = ['1','2','3','1','6','7']  #步长为2的切片还没有弄好
# num[::2] = []
# print(num)
