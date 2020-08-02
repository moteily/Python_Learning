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
# 继续列表的操作，增删改查等，演示常用函数
#   1.append方法：将一个对象附加于列表的末尾
lst = [1, 2, 3]
lst.append(4)
print(lst)
#   2.clear方法：将列表清空,等同于lst[:] = []
lst.clear()
print(lst)
#   3.copy方法：列表复制******有trick 重点
a = [1, 2, 3]
b = a  # 采用=将b指向a
c = a.copy()  # 采用copy的方法复制a的内容
d = a[:]
# b[1] = 4   #对列表和被复制的列表都会有改变
# c[1] = 4    #只会改变列表c，对列表a无影响
d[1] = 4  # 与copy相同，只改变副本，对原来列表无影响
print(a)  # 只用=以后，b和a指向了同一片内存，修改b的同时a会改变
#   4.count方法：计算指定元素在列表中出现的次数
a = ['d', 'd', ['d', 'd'], 'ab']
print(a.count('d'))  # 结果为2
#   5.extend方法：同时将多个值附加到列表末尾，即使用一个列表来扩展另一个列表
#   a.extend(b) 与a = a+b效果相同，但执行效率更高
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
#   6.index方法：在列表中查找指定值第一次出现的索引
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('the'))
# print(knights.index('theddd')) #'thedd'不在列表中，产生异常
#   insert方法：用于将一个对象插入列表，比采用切片[3:3]的方式要高效的多
numbers = [1, 2, 3, 6]
numbers.insert(3, 'four')  # 在列表第三个位置插入'four'
numbers[4:4] = ['five']  # 采用切片的方式插入
print(numbers)
#   7.pop和attend构成出入栈操作，pop为拿出列表中对应的元素，没有参数则返回最后一个元素
x = [1, 2, 3]
x.append(x.pop(1))
print(x)  # x 结果为132，先把第二个元素出栈，再在末尾入栈
#   8.remove方法：删除列表中指定内容的元素，但不范围任何值
x = ['to', 'be', 'number', 'one', 'bee']
x.remove('be')
print(x)
#   9.reverse方法：按相反的顺序排列列表中的元素,与reserved(x)差不多
x = [1, 4, 7, 3]
x.reverse()
y = reversed(x)
print(x)  # 结果为3 7 4 1
print(list(y))
#   8.sort方法：就地排序，对原有的列表进行修改，无返回值
x = [7, 5, 63, 2, 4]
x.sort()
# y = x.sort()   #Don't do this,because the fun'sort' dosen't have a return value
y = sorted(x)  # sorted函数有返回值可以替代上面的说法
print(y)
print(x)
# 列表部分结束，列表是python最常用且重要的数据类型
###############################################
###############################################
#   元组:不可修改的序列（列表是可修改的序列）
# 表示格式(1，2，3，4，5)，小括号中元素加逗号，注意只有一个元素时后面也要加逗号，例如(13,)
# 为什么已经有列表了还要使用元组？
#   1.元组用作映射中的键（以及集合的成员）
#   2.python很多内置函数返回值为元组

print(3 * (40 + 2))  # 不加逗号，结果为126
print((3 * (40 + 2,)))  # 加逗号，结果为(42,42,42)
#   1.tuple方法:将序列作为一个参数，并将其转换为元组
print(tuple(['a', 'b', 'dsadsa']))

#################################################################################################################
# 序列：列表和元组小节：
#     序列：序列是一种数据结构，其中的元素带编号（编号从0开始）。列表、字符串和元组都属于序列
#         其中列表是可变的，而元组和字符串是不可变的（一旦创建内容就是固定的）
#         要访问序列的一部分，可采用'切片'操作
#         修改列表，给元素赋值也可采用切片操作
#     成员资格：要确定特定的值是否在序列（或其他容器）中，可使用运算符in。将运算符in用于字符串时情况比较特殊--查找字串
#     常用函数：
#         len(seq):   返回序列长度
#         list(seq):   将序列转换为列表
#         max(args):      返回序列或一组参数中的最大值
#         min(args)：      与max相反
#         reversed(seq):  返回反向迭代序列
#         sorted(seq):    返回列表排序
#         tuple(seq):     将序列转换为元组
#################################################################################################################
#   第三章：字符串
#################################################################################################################
#   与前面的元组、列表相同，所有标准序列操作（索引、切片、乘法、成员资格检查、长度、最小值和最大值）都适用于字符串，但
#   字符串是不可变的，“因此所有的元素赋值和切片赋值都是非法的”
#   1.format方法：对字符串中需要填充的位置进行相应的填充
#   规则：每个替换字段都用花括号括起，其中可能包含名称，还可能包含有关如何对相应的值进行转换和格式设置的信息
# examples：
#   最简单的情况：替换字段没有名称或将索引用作名称
a = "{},{} and {}".format("first", "second", "third")
print(a)  # 执行结果为 first,second and third
a = "{0},{1} and {2}".format("first", "second", "third")
print(a)  # 加入索引后执行结果依然为 first,second and third
a = "{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to")
print(a)  # 执行结果为:to be or not to be

from math import pi

# 关键字参数的排列顺序无关紧要，  .2f指定了value变量的格式，并使用冒号将其与字段名隔开。
a = "{name} is approximately {value:.2f}.".format(value= pi, name="π")
print(a)
#   替换字段名
a = "{foo}{}{bar}{}".format(1, 2, bar=4, foo=3)
print(a)
#   使用索引替换字段名
fullname = ["Alfred", "Smoketoomuch"]
a = "Mr {name[1]}".format(name=fullname)
print(a)
#   基本转换：指定要在字段中包含的值后，就可添加有关如何设置其格式的指令了
print("{pi!s} {pi!a} {pi!r}".format(pi="π"))
# 上述三个标志（s，a，r）指定分别使用str、repr和ascii进行转换。
#   str：创建外观普通的字符串版本
#   repr：尝试创建给定值的python表示
#   ascii：显示ASCII字符的表示
#   设置字段宽度、精度和千分位分隔符
#   设置浮点数格式时，默认在小数点后显示6位小数，并根据需要设置字段的宽度，而不进行任何形式的填充。
#   宽度设置以及小数点后的位数设定: 宽度使用整数进行指定，小数点后使用 .f设定
a = "{num:10.2f}".format(num=3.1514)
print(a)
#   可用逗号指出来你要添加千位分隔符，没三位一个，
a = 'One googol is {:,}'.format(10 ** 10)  # a**b表示a的b次方
print(a)
#   练习1：字符串格式设置实例
#   根据指定的宽度打印格式良好的价格列表
width = int(input("Please enter width:"))
price_width = 10
item_width = width - price_width
header_fmt = '{{:{}}}{{:>{}}}'
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('-' * width)
print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots(16 oz.)', 8))
print(fmt.format('PrUnes(4 lbs.)', 12))
print('=' * width)
# 字符串方法：
#   center函数：通过在两边添加填充字符（默认为空格）让字符居中
a = "WZN is a Pig".center(30)
print(a)
a = "WZN是猪".center(35, '\N{pig}')  # 可指定符号进行填充
print(a)
#   find方法：在字符串中查找字串，如果找大返回字串第一个字符的索引，否则返回-1
a = "With a moo-moo here, and a moo-moo there".find('moo')
b = "With a moo-moo here, and a moo-moo there".find('With')
c = "With a moo-moo here, and a moo-moo there".find('mmo')
d = "With a moo-moo here, and a moo-moo there".find('moo', 4, 20)   #find可以添加两个参数，分别为起始和终止位置
print("a = {a},b = {b},c = {c},d = {d}".format(a=a, b=b, c=c, d=d))  # 不要忘记format的用法
#   join方法：join是一个非常重要的字符串方法，与solit相反，用于合并'序列'的元素
#   split方法：作用于join相反，用于将字符串拆分为序列
a = '1+2+3'
b = a.split('+')
print(b)
#   lower方法：返回字符串的小写版本
print('Trondheim Hammer Dance.'.lower())
#   replace：将指定字串都替换为另一个字符串
print('Wzn is a pig'.replace('pig','lazy pig'))
#   strip方法：将字符串开头和结尾的空白（不包括中间的空白）删除，并返回删除后的结果,用的很多！！！
print('     dsadsad dsadsa daa d   ds a 1  A'.strip().lower())
#   translate方法：与replace方法一样替换字符串的特定部分，但不同的是它只能进行单字符替换，这个方法可以同时替换多个字符
#   因此效率比replace更高
#   使用方法：首先要创建一个转换表，这个转换表指出了不同Unicode码点之间的转换关系，通过对字符串类型str调用方法 maketrans，
#   maketrans方法有两个参数：两个长度相同的字符串，他们指定要将第一个字符串中每个字符都替换为第二个字符串中的相应字符
#   example：
table = str.maketrans('cs','kz')    #不是将cs替换为kz，而是c替换为k，s替换为z！
print(table)    #可以打印table项查看Unicode的对应 ，{99: 107, 115: 122}
print('this is an incredible test'.translate(table))    #通过translate调用转换表对字符串进行替换
table2 = str.maketrans('cs','kz',' ')   #maketrans方法有第三个参数，用于删除那些‘字母’，此处删除空格
print('this is an incredible test'.translate(table2))
#   判断字符串是否满足特定条件的函数：
#   很多字符串都是以is打头，如isspace、isdigit和isupper，他们判断字符串时候具有特定的性质（如包含的字符全为空白、数字、或大写）
#   如果字符串具备特定的性质，这些方法就返回True，否则返回False

########################################################################################################################
#第三章:字符串的相关概念及方法小节
# 本章介绍了字符串的两个重要方面
# 1.字符串的格式设置: 求模运算（%）可用于将值合并为包含转换标志（如%s）的字符串，这让你能够以众多方式设置值的格式，
# 如左对齐或右对齐，指定字段宽度和精度，添加符号（正好或负号）以及在左边填充0等。
# 2.字符串方法:字符串有很多方法，有些很有用（split、join、strip等）

#下章预告：列表、字符串和字典是三种最重要的python数据类型。下个章节将介绍字典，它不仅支持整数索引，还支持其他类型的键（字符串、元组）
########################################################################################################################
#################################################################################################################
#   第四章：当索引行不通时：字典
#################################################################################################################
#   backgroud；需要将一系列值组合成数据结构并通过编号来访问各个值时，列表很有用。本章介绍一种可通过‘名称’来访问其各个值的
#   数据结构。这种数据结构成为映射（mapping）。字典是Python中唯一的内置映射类型，其中的值不按顺序排列，而是存储在‘键’下。
#   键可能是“数、字符串或元组”
#   字典（日常生活中的字典或Python中的字典）旨在让你能够轻松找到特定的单词（键），以获悉其定义（值）。
#   在很多情况下，使用字典都比使用列表更合适。下面是字典的一些用途：
#       1.表示棋盘的状态，其中每个键都是由坐标组成的元组
#       2.存储文件修改时间，其中键为文件名
#       3.数字电话/地址簿
##################################################################################################################
#   字典的创建和使用:
#   字典由键及其相应的值组成，这种键-值对称为项（item）。每个键与其值之间都用冒号（：）分隔，项之间用逗号分隔，而整个字典都放在
#   花括号内。空字典（没有任何项）用两个花括号表示：{}
#   dict函数：用元组创建字典
item = [['name', 'Ljy'], ['age', 23]]  # 内层括号可以为()也可以为[]
print(item[1][1])
d = dict(item)
print("Dictionary is {} \nname is {}".format(d, d['name']))
#   还可使用关键字实参来调用这个函数
d = dict(name='ljy', age=23)
print(d)
#   字典的基本行为很多方面类似于序列
#   1.len(d)返回字典中包含的键值对个数
#   2.d[k]返回与键k相关联的值
#   3.del d[k]删除键为k的项
#   4.k in d检查字典d是否包含键为k的项
#   练习1 ：字典实例，一个简单的数据库(Important and tricky)
#   问题描述：一个将人名用作键的字典，每个人都用一个字典表示，
#   字典包含键"phone"和"addr"，他们分别与电话号码和地址相关联
people = {
    'Alice': {
        'phone': '1213132',
        'addr': 'Foo drive 23'
    },
    'Sam': {
        'phone': '12314878',
        'addr': 'CETC'
    },
    'Wzn': {
        'phone': '778777',
        'addr': '478454'
    }
}
label = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input("Please input you name:")
request = input("Input (p) to get the phone number and (a) to get the address: ")
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'
if name in people:
    print("{}'s {} is {}".format(name, label[key], people[name][key]))
#   将字符串格式设置功能用于字典 format_map
phonebook = {
    "wzn": 47877,
    "dasda": 78878,
    "dasdas": 778787878
}
print("wzn's phone number is {wzn}".format_map(phonebook))  # 此处的{}中键名不能省略，因为需要根据键名进行匹配
#   Important Part：字典中常用的方法
#   1. clear方法: d.clear()删除字典的所有字典项
#   2. copy方法：返回一个新字典，其包含的键值对与原来的字典相同（这个方法执行的是浅复制）
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'wzn'
y['machines'].remove('bar')
print("{} \n{}".format(y, x))
#   有上面例子可知，在替换副本的值时，原件不受影响。然而，如果"修改（删除）"副本中的值而不是替换，原件也将发生改变，因为
#   原件指向的也是被修改的值
#   为了解决以上问题，一种办法是执行"深复制"，即同时复制值以及其包含的所有值，等等。为此可使用copy模块的deepcopy
from copy import deepcopy

d = {}  # 建立空字典
d['names'] = ['Alice', 'Sam']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Waa')
print("{}{}".format(c, dc))

#   3.fromkeys方法：创建一个新字典，其中包含指定的键，且每个键对应的值都是None
d = {}.fromkeys(['name', 'age'], 'Unkown')  # fromkeys([序列]，'值')
#   4.get方法：为访问字典项提供了宽松的环境。通常，如果试图访问字典中没有的项将引发错误，get方法可以避免这一点
d = {}
d['names'] = ['Alice', 'Sam']
#   print(d['age'])  #字典中不存在age，引发错误
print(d.get('age', 'Not in dictionary!'))  # age键在字典中返回其值，否则返回Not in dictionary
print(d.get('names', 'Not in dictionary!'))  # age键在字典中返回其值，否则返回Not in dictionary
print(d)
#   练习2 ：字典方法示例：
#   与上个例子差不多，用get方法替代
people = {
    'Alice': {
        'phone': '1213132',
        'addr': 'Foo drive 23'
    },
    'Sam': {
        'phone': '12314878',
        'addr': 'CETC'
    },
    'Wzn': {
        'phone': '778777',
        'addr': '478454'
    }
}
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name: ')
request = input('Phone number(p) or address(a)?')
#   使用正确的键：
key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
# 使用get提供默认值
person = people.get(name)  # 这里的person是一个子字典 ，而非只是一个名字，因此下面得用person.get而不能直接用name.get
label = labels.get(key, key)
result = person.get(key, 'not available')
print("{}'s {} is {}".format(name, label, result))
#   5.item方法;方法item返回一个包含所有字典项的列表，其中每个元素都为（key，value）的形式。字典项在列表中的排列顺序不一定
d = {'title': 'Python web site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())
#   6.key方法：返回一个字典视图，其中包含指定字典的键
print(d.keys())
#   7.pop方法：可用于获取与指定键相关联的值，并将该键值对从字典删除。
print(d.pop('title'))
#   9.setdefault方法：与get相似，因为他也获取与指定键相关联的值，但除此之外，setdefault还在字典不包含指定的键时，在字典中添加
#   指定的键值对
d = {}
d.setdefault('name', 'N/A')
print(d)
d['name'] = 'Sam'
d.setdefault('name', 'N/A')  # 若存在则返回其值，不存在则初始化其值为N/A
print(d)
#   10.update: 使用一个字典的项来更新另一个字典
#   更新规则：对于参数提供的字典，将其项添加到当前字典中；当前字典已经包含的相同项，替换其值
d = {
    'title': 'Python Web Site',
    'Url': 'http://www.python.org',
    'Changed': 'Mar 14 22:09:15 MET 2016'
}
x = {
    'title': 'Python Language Website',
    'Country':'China'
}
d.update(x)
print(d)
#   11.values方法：返回一个由字典中的值组成的字典视图，不同于方法keys，方法values返回的是值而不是键，所以可能有重复值
print(d.values())
# ######################################################################################################################
# 第四章：字典小结
#     1.映射：映射让你能够使用任何“不可变的对象”（最常用的是字符串和元组，不能为序列）来标识其元素。Python只有一种
#     内置的映射类型，那就是字典
#     2.将字符串格式设置功能用于字典：要对字典执行字符串格式设置操作，不能使用format和命名参数，而必须使用format_map
#     3.字典方法：字典有很多方法，这些方法的调用方式与列表和字符串的方法相同
#     4.dist(seq):从键值对、映射或关键字参数创建字典
# ######################################################################################################################
######################################################################################################################
# 第五章:条件、循环与其他语句
# 已经见过几种语句（print语句，import语句和赋值语句），先来看看这些语句的其他一些用法，再来深入探讨条件语句和循环语句。
# 然后，我们将介绍列表推导，他们虽然是表达式，但工作原理几乎与条件语句和循环语句相同。最后我们将介绍pass、del和exec
######################################################################################################################
# 再识print：print()可以同时打印多个表达式，条件是用逗号分隔他们
#   from numpy.core import number

print('age', 42)
name = 'Glummy'
salution = 'Mr'
greeting = 'Hello,'
print(greeting, salution, name)
print(greeting + 'ljy', name, salution)  # 可以使用+连接要打印的字符串
print('I', 'wish', 'to', 'dadsada', sep='_')  # 默认分隔符为‘，’ 可用sep自定义分隔符
#   import用法：导入函数重命名
# 从模块导入时，通常使用：
#     import somemodule
# 或使用
#     from somemodule import somnefunction
# 或使用
#     from somemodule import somefunction,anotherfunction,yetanotherfunction
# 或
# import somemodule import *
import math as foobar

print(foobar.sqrt(4))
from math import sqrt as foobar

print(foobar(4))  # 上述两个import后的重命名作用效果相同
# ****  对于两个不同模块含有相同名字的函数的引用
# from module1 import open as open1
# from module2 import open as open2
#   赋值魔法：
#       1.序列解包 2.链式赋值 3.增强赋值
#   1.序列解包：将一个序列（或任何可迭代对象）解包，并将得到的值存储到一系列变量中。follow examples
x, y, z = (1, 2, 3)
print(x)
x, y = y, x
print(x, y, z)
values = 1, 2, 3
print(values)  # 单独打印values变量还是一个元组，但是分开打印就是元素
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()  # 将队尾元素出栈
print(key)
print(value)
#   可使用星号运算符（*）来收集多余的值，这样无需确保值和变量的个数相同，例子如下
a, b, *rest = ['dsa', 1, 'dasdasd', 44487]
print(rest)
#   *位置可任意放置，例如
name = "Albus Percival Wulfric Brian Dumbledore"
first, *middle, last = name.split()
print(middle)
#   赋值语句的右边可以是任何类型的序列，但带星号的变量最终包含的总是一个列表。在变量和值的个数相同时亦是如此
a, *b, c = (1, 2, 3)
print(b)
#   2.链式赋值：是一种快捷的赋值方式，用于将多个变量关联到同一个值。
# x = y =somefunction()
# 上述代码与下面的代码等价:
# y = somefunction()
# x = y
#   3.增强赋值：
x = 2
x += 1
x *= 2
print(x)
#   增强赋值也可用于其他数据类型（只要使用双目运算符可用于这些数据类型）
fnord = 'foo'
fnord += 'bar'
fnord *= 2
print(fnord)
#   条件和条件语句：
#   1.布尔值的用武之地:用作布尔表达式（如用作if语句中的条件）时，下面的值都将被解释器视为假：
#   False None 0 "" () [] {}，其他所有情况都为真
#   布尔值True和False属于类型bool，而bool与list、str和tuple一样，可用来转换其他的值。
print(bool("dasdasdadsasda"))
print(bool(0), bool({}), bool(' '))  # 注意空格在字符串中也算字符，但是bool({ })为假
#   2.条件表达式：即c语言三目元算符的python版本  ？：
#   status = "friend" if name.endwith("Gumby") else "stranger"
# ** python支持链式比较，如0<age < 100
a = 116
if 0 < a < 19:
    print("Awaresome!")
elif a >= 19:
    print("sb")
else:
    print("dsadsa")
#   '=='与'is:相同运算符'的比较，tricky！
x = y = [1, 2, 3]
z = [1, 2, 3]
print(bool(x == y), bool(x == z), bool(x is y), bool(x is z))  # x is z :False, the others are true
# 解释上面代码：is 是用来检查两个对象是否相同（而不是相等）。变量x和y指向同一个列表，而z指向另一个列表，
#   这两个列表虽然相等，但并非同一个对象。
#   总之，==用来检查两个对象是否相等，而is用来检查两个对象是否相同（同一个对象）

#   字符串和序列的比较：字符串是根据字符的字母排列顺序进行比较的，原理上是比较Unicode编码大小
print(bool("alpha" < 'beta'))
#   序列比较大小规则与字符串类似，从第一个开始比较
print([2, [1, 2, 3, 4]] > [2, [0, 5, 6]])  # return true
#   布尔运算符：and ,or ,and not
number = int(input('Enter a number between 1 and 10: '))
if number <= 10 and number >= 1:  # 其实可以用更简单的链式比较1 <= number <= 10
    print('Great!')
else:
    print("Wrong!")

if number <= 10 and not number <= 5:  # 注意not不能单独使用而是与and一起使用
    print('Great!')
else:
    print("Wrong!")
# #   断言:  多用于调试和程序错误即刻返回
# if 语句有一个很有用的"亲戚"，其工作原理类似于下面的伪代码：
# if not condition:
#     crash program
# 问题是，为何要编写类似于这样的代码呢？因为让程序在错误条件出现时立即崩溃胜过以后再崩溃。基本上，你可要求某些条件得到满足（如
# 核实函数参数满足要求或为初始测试和调试提供帮助），为此可在语句中使用关键词assert
age = 10
assert 0 <= age <= 100
# age = -1
# # assert 0<=age <=100 #   AssertionError
# 如果知道必须满足特定的条件才能正确的运行，可在程序中添加assert语句充当检查点，这很有帮助。
# 还可在条件后添加一个字符串，对断言做出说明。
# age = -1
# assert 0<=age <=100,'The age must be realistic!' # error return 'The age must be realistic!'

#   循环：while for
#   while :while语句非常灵活，在用于在条件为真时反复执行代码块。
name = ''
while not name.strip():
    name = input("Please input your name and typer enter to continue: ")
print("Your name is", name)  # 别忘记前面学的format,也可以用print("Your name si {}".format(name))
#   for：根据需要定制循环，一种这样的需求是为序列（或其他可迭代对象）中每个元素执行代码块
#   注意:基本上，可迭代对象是可使用for循环进行遍历的对象，后面的章节将详细介绍可迭代对象和迭代器，就目前而言，
#   只需要将可迭代对象视为序列即可。
#   examples:
words = "This is an ex parrot".split()
for word in words:
    print(word)
#   鉴于迭代（也就是遍历）特定范围内的数是一种常见的任务，python提供了一个创建范围的内置函数。range（x,y,z）:从起始坐标
#   x起，迭代y次（注意y不是终止迭代坐标，而是次数），z为步长，x,z可以省略
for number in range(0, 101, 2):  # 打印0到100
    print(number)
#   迭代字典：遍历字典中的所有关键字，可像遍历序列那样使用普通的for语句
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])
#   for循环的优点之一是，可在其中使用序列解包：
for (key, values) in d.items():  # 此处的key values可以用作列表，也可以用作元组
    print(key, 'corrsponds to', values)
#   并行迭代：有时你可能想同时迭代两个序列，假设有下面两个列表：
names = ['anne', 'beth', 'geoge', 'damon']
ages = [11, 23, 432, 45]
for i in range(len(names)):
    print(names[i], '\'s age is', ages[i])
#   zip函数（将两个序列合并为元组对）：一个很有用的并行迭代工具，它将两个序列"缝合"起来，并返回一个由"元组"组成的序列。返回值是一个适合迭代的对象，
#   要查看其内容，可使用list将其转换为列表
a = zip(names, ages)
print(list(a))
#   缝合后可在循环中将元组解包
for name, age in zip(names, ages):
    print(name, 'is', age, 'year\'s old')
# 函数zip可用于”缝合“任意数量的序列。需要指出的是，当序列长度不同时，函数zip将在最短的序列用完之后停止"缝合"
print(list(zip(range(6), range(10000))))
#   break 和contine 与C中的相同，理解原理即可
#   while True与C中while 1语句相同，可以消除函数中没用的哑值
#   循环语句中的if else
#   练习1：找出0到99中最大的开方值
from math import sqrt

for n in range(99, 81, -1):
    if n == sqrt(n):
        print(n)
        break
else:
    print("Not find!")
#   三人行：结束本章之前大致介绍一下另外三条语句：pass、del和exec
#   1.  pass：什么都不做。在你编写代码时，可将其用作占位符。例如，你可能编写了一条if语句并想尝试运行它但其中缺少一个代码块，
#   这将导致代码运行出错，此时可以使用pass语句
name = input("Please input your name: ")
if name == 'Ralph Auldus Melish':
    print('Welcome !')
elif name == 'Enid':
    # 此处代码还未想好
    pass
elif name == 'Bill Gates':
    print("Access Denied!")
#   2.  del:用于垃圾回收，x y同时指向一个列表，用del x只会删除x而对y无影响。
#   python智慧无穷，对于漂浮在计算机内存中没有任何名称与之关联的"东西"，python会自动将其删除，称为"垃圾回收"
#   exec和eval执行字符串及计算其结果
#   警告: 本节介绍如何执行存储在字符串中的Python代码，这样做可能带来严重的安全隐患。如果将部分内容由用户提供的字符串作为代码
# 执行，将无法控制代码的行为。在网络应用程序，如通用网关接口（CGI）脚本中，这样做尤其危险
#   exec：函数exex将字符串作为代码执行
exec("print('Hello World')")

#   然而，调用函数exec时只给他提供一个参数绝非好事，在大多数情况下，还应向他传递一个”命名空间“，
#   否则代码将污染你的命名空间，即修改你的变量。例如：
# from math import sqrt
# exec ('sqrt = 1')
# sqrt(4)
#   由于执行了exec中的sqrt赋值代码，导致后面的sqrt函数失效，可用添加命名空间解决,
#   为此可以添加第二个参数---字典，用作代码字符串的命名空间
from math import sqrt

scope = {}
exec('sqrt = 1', scope)  # 可以理解为将sqrt： 1 添加到名为scope的字典中
print(sqrt(4), scope['sqrt'])
#   eval是一个类似于exec的内置函数。exec执行一系列Python语句，而eval计算用字符串标识的Python表达式的值，并返回结果（exec
#   什么都不返回，因为他本身就是条语句）。例如可以使用下面代码创建一个Python计算器：
eval(input("Enter an arithmetic expression : "))

#######################################################################################################################
# 第五章：print语句import语句以及条件循环等
# 1.打印语句:可以使用print语句打印多个用逗号分隔的值。
# 2.导入语句:使用import ... as ...
# 3.赋值语句:通过奇妙的序列解包和链式赋值。可同时用于多个变量的赋值，通过增强赋值，可就地修改变量
# 4.代码块(代码对齐)：代码块用于通过缩进将语句编组。代码块可用于条件语句和循环中，还可用于函数和类的定义中
# 5.条件语句：if elif else
# 6.断言：断言判断某件事（一个布尔表达式）为真，可包含说明为何如此的字符串。如果指定表达式为假，断言就将导致程序停止执行。最好
#     尽早将错误揪出来，免得它潜藏在程序中，直到带来麻烦。
# 7.循环：你可针对序列中的每个元素（如特定范围内的每个数）执行代码块，也可在条件为真时反复执行代码块。break contine语句
# 8.推导：推导并不是语句，而是表达式，他们看起来很像循环。通过列表推导，可从既有列表创建出新列表，这是通过对列表元素调用函数、
#     剔除不想要的函数等实现的。推导功能强大，但在很多情况下，使用普通循环和条件语句也能完成任务，且代码可读性更高。
# 9.pass、del、exec和eval：pass语句什么都不做，但适合用作占位符。del语句用于删除变量或数据结构的成员，但不能用于删除值。函数
#     exec用于将字符串作为Python程序执行。函数eval计算用字符串标识的表达式并返回结果。
#######################################################################################################################
#   预告：至此已经学完了基础知识，能够实现任何想象得到的算法，还能够读取参数并打印结果。在接下来的两章，将学习”抽象“。在编写较大
#的程序时，抽象可避免你只见树木不见森林
######################################################################################################################

####################################################################################################################
# 第六章：函数、参数和作用域
# 本章将介绍将语句组合成函数，详细介绍参数和作用域，还将讨论递归是什么及其在程序中的用途
# 抽象的结构:抽象是程序能够被人理解的关键所在，组织计算机程序时，你也采取类似的方式，程序就应非常抽象，要使人看到这些代码
# 任何人都知道这个程序是做什么，至于这些操作的细节，将在其他地方（独立的函数定义）中给出
####################################################################################################################
#   1.函数的定义：def
def hello(name):
    return 'hello,' + name + '!'  # 由于此处采用了字符串合并，因此name只能为字符型


print(hello('Sam'))


#   编写斐波那契函数：
def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


# print(fibs(1000))


#   空返回函数：不包含return语句或者包含return语句但没有在return后面指定值
def test():
    print('This is printed')
    return


#   2.参数魔法：编写函数旨在为当前程序（甚至其他程序）提供服务，你的职责是确保他在提供的参数正确时完成任务，并在参数不对时
#   以显而易见的方式失败。（为此，通常使用断言或者异常）
#   注意：在def语句中，位于函数名后面的变量称为"形参"，而调用函数时提供的值称为实参，但本书基本不会对此做严格的区分。在很重要
#   的情况下，我会将实参称为值，以便将其与类似于变量的形参区分开来。    参数存储在局部作用域内。

#   抽象的关键在于隐藏所有的更新细节，为此可使用函数。
#   在提高程序的抽象程度方面，使用函数来修饰数据结构（如列表或字典）是一种不错的方式
# 练习1：假设你要编写一个程序，让他存储姓名，并让用户能够根据名字、中间名或姓找人。为此可以采用以下方法：两层字典
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):  # data为两层结构的字典，label name为两层键
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):  # zip函数将labels和names对应元素组合成元组对序列
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


# 函数store的执行如下步骤:
# (1): 将参数data 和full_name提供给函数。这些参数被设置为外部获得的值
# (2)：通过分析full_name创建一个名为names的列表
# (3)：如果names长度为2（只有名字和姓），就将中间名设置为空字符串
# (4)：将'first' 'middle' 'last'存储在元组label中（也可以使用列表，这里使用元组只是为了省略方括号）
# (5): 使用zip函数将标签和“对应”的名字合并，以便对每个标签-名字对执行如下操作
#     获取属于该标签和名字的列表
#     将full_name附加到该列表末尾或插入一个新列表
#
# 下面调用执行测试程序功能：
MyNames = {}
init(MyNames)
store(MyNames, 'Mdsa lie Hetland')
print(lookup(MyNames, 'middle', 'lie'))
store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
print(lookup(MyNames, 'first', 'Robin'))
store(MyNames, 'Mr. Gumby')
print(lookup(MyNames, 'middle', ''))


#   其实这种程序非常适合使用面向对象编程，下章将学习

#   3.关键字参数和默认值
# 前面使用的参数都是“位置参数”，因为他们至关重要。本节介绍关键字参数，可以让你完全忽略位置，要熟悉这种技巧需要一段时间，
# 但随着程序规模的增大，很快作用就会凸显出来。
def hello_1(greeting, name):
    print('{},{}!'.format(greeting, name))


hello_1(name='Sam', greeting='Hello')


#   如上方这样使用名称指定的参数为关键字参数，主要优点是有助于澄清各个参数的作用，这样做虽然输入量多些，但每个参数的作用都
#   清晰明了，参数顺序错误也没有关系

#   除此之外，关键字参数最大的优点在于：可以指定默认值
def hello_2(name='World', greeting='Hello,'):  # 指定了默认值
    print('{},{}!'.format(greeting, name))


# 像这样给参数指定了默认值后，调用函数时可不提供它！可以根据需要，一个参数也不提供或者提供部分或者全部参数
hello_2()
hello_2(name='New World')


#   位置参数和关键字参数可以结合使用，更加提高了灵活性，但是不推荐，容易出错

#   4.收集参数：函数定义时加*号，有时候允许用户提供任意数量的参数很有用，
#   例如前面的练习中，每次只能存储一个姓名，如果能同时存储多个姓名就好了
#   收集参数将为你解决这个问题。*（收集的参数构成元组），   **（手机的参数构成字典）
#   收集参数有点类似于C/C++中的指针类型的参数
def print_params(title, *params):
    print(title)
    print(params)


print_params('Param', 1212, 33, 33)
#   * 意味着手机余下的位置参数。如果没有可供收集的参数，params将是一个空元组。
print_params('Nothing:')


#   与赋值时一样，带星号的参数也可以放在其他位置（而不是最后），但不同的是，在这种情况下，你需要做些额外操作：使用名称
#   来指定后续参数
def in_the_middle(x, *y, z):
    print(x, y, z)


in_the_middle(1, 2, 3, 4, 5, 6, z=7)  # 1 (2, 3, 4, 5, 6) 7 注意，此处必须指定z的值，否则将会报错


#   可用双星号收集关键字参数
def print_params_3(**params):
    print(params)


print_params_3(x=1, y=2, z=3)  # {'x': 1, 'y': 2, 'z': 3} 双星收集后变为字典，单星收集为元组，注意区别


#   练习2：结合位置参数，关键字参数，收集参数
def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)


print_params_4(1, 2, 3, 4, 5, 6, 7, foo=1, bar=2)


# 执行结果如下：
# 1 2 3
# (4, 5, 6, 7)
# {'foo': 1, 'bar': 2}

# 练习3：如何在姓名存储示例中使用这种技术？
def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2: names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):  # zip函数将labels和names对应元素组合成元组对序列
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


d = {}
init(d)
store(d, 'Luke Skysad', 'Anakin Skysad')
lookup(d, 'last', 'Skysad')
print(lookup(d, 'last', 'Skysad'))


#   4.分配参数: 函数调用时加*
#   前面介绍了如何将参数收集到元组和字典中，但用同样的两个运算符（*和**）也可以执行相反的操作。例子如下
def add(x, y):
    return x + y


params = (1, 2)
print(*params, params)  # 注意*params 和 params的区别
print(add(*params))

params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_1(**params)


# tips：使用这些拆分运算符来传递参数很有用，因为这样无需操心参数个数之类的问题，如下所示：
def foo(x, y, z, m=0, n=0):
    print(x, y, z, m, n)


def call_foo(*args, **kwds):
    print("Calling foo")
    foo(*args, **kwds)  # **为关键字参数的收集调用


call_foo(1, 2, 3, m=1, n=2)


#   练习使用参数：面对如此多的参数提供和接受方式，很容易犯晕。下面来看一个综合示例。首先来定义一些函数
def story(**kwds):
    return 'Once upon a time, there was a {job} called {name}.'.format_map(kwds)  # 字典用format_map 不要忘了


def power(x, y, *others):
    if others:
        print('Received redundant parameters: ', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() for step >0'
    if stop is None:  # 如果没有给参数stop指定值
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


print(story(job='King', name='Sam'))  # 参数调用1
params = {'job': 'King', 'name': 'Sam'}
print(story(**params))  # 参数调用2
del params['job']
print(story(job='King', **params))  # 参数调用3
print(power(2, 3))  # 参数调用4
print(power(3, 2))
print(power(x=2, y=3))
params = [5, ] * 2  # (5,)和[5,]都可，但是不能省略逗号
print(power(*params))
power(3, 3, 'hello world')
print(interval(10))  # 参数调用4
print(interval(1, 5))
print(interval(3, 12, 4))
print(*interval(3, 7))  # 3 4 5 6
print(power(*interval(3, 7)))  # 参数调用5


#   所以请大胆尝试使用这些函数以及自己的创建的函数，知道你觉得自己掌握了所有相关的工作

#   5.作用域：又叫做命名空间，除了全局作用域外，每个函数都将创建一个作用域，函数之间不发生冲突
def combine(parameter):
    print(parameter + external)


external = 'berry'
combine('Stra')

#   警告：像这样访问全局变量是众多bug的根源，务必慎用全局变量
#   “遮盖”的问题：如果一个局部变量或参数与你要访问的全局变量同名，就无法直接访问全局变量，因为它被局部变量遮住了
#   结局“遮盖”问题：如果需要可使用函数globals来访问全局变量。
#   这个函数类似于vars，返回一个包含全局变量的字典。（locals返回一个包含局部变量的字典）,例子如下：
x = 1
parameter = 'berry'


def combine(parameter):
    print(parameter + globals()['parameter'])  # 读入全局变量的值用globals()函数
    global x;  # 改变全局变量，需要先用global声明，注意与读入全局变量的区别
    x = 11


combine('Shrub')
print(x)


#   6.作用域嵌套，Python可以嵌套，即可将一个函数放在另一个函数内
#   7.递归:   递归意味着引用或者调用自身
#   无穷递归的函数式定义:
def recursion():
    return recursion()


#   普通递归的组成：
#       1.基线条件（针对最小的问题）：满足这种条件时函数将返回一个值。
#       2.递归条件：包含一个或多个调用，这些调用旨在解决问题的一部分
# 练习4：用非递归和递归的方式计算n的阶乘
#   (1)非递归:
def factorial_1(n):
    result = n
    for i in range(1, n):  # 必须为1到n，不能从0开始
        result *= i
    return result


#   (2)递归：
def factorail_2(n):
    if n == 1:
        return 1
    else:
        return factorail_2(n - 1) * n


print('非递归：{}，递归：{}'.format(factorial_1(10), factorail_2(10)))


#   练习5：二分法查找
def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search((sequence, number, lower, middle))


######################################################################################################################
# 第六章小结: 函数、参数和作用域
# 1.
# 抽象: 抽象是隐藏不必要细节的艺术。通过定义处理细节的函数，可让程序更抽象
# 2.
# 函数定义：函数是使用def语句定义的。函数由语句块组成，他们从外部接受值（参数），并可能返回一个或多个值（计算结果）
# 3.
# 参数：函数通过参数（调用函数时被设置的变量）接受所需的信息。在Python中，参数有两类：位置参数和关键字参数。通过给
# 参数指定默认值，可使其变成可选的。
# 4.
# 作用域：变量存储在作用域（也叫做命名空间）中。在Python中，作用域分为两大类：全局作用域和局部作用域。作用域可以嵌套
# 5.
# 递归：函数可以调用自身，称为递归。可使用递归完成的任务都可使用循环来完成，但有时使用递归函数可读性更高
# 6.
# 函数式编程：Python提供了一些函数式编程工具，其中包括lambda表达式以及函数map、filter和reduce
#
# 本章介绍的新函数:
# map(func, seq[, seq, ...])                  对序列中所有元素执行函数
# filter(func, seq)                           返回一个列表，其中包含对其执行函数时结果为真的所有元素
# reduce(func, seq[, initial])                等价于func(func(func(seq[0], seq[1], seq[2]), ...), ...)
# sum(seq)                                    返回seq中所有元素的和
# apply(func[, args[, kwargs]])               调用函数（还提供要传递给函数的参数）
#
# 下章预告：
#     下一章将介绍“面向对象编程”，让你能够进一步提高程序的抽象程度。将学习如何创建自定义类型（类），并将其与Python提供的类型
#    （如字符串、列表和字典）一起使用，这让你能够编写出质量更高的程序。
#     阅读完下一章，你建个能够编写出大型程序，同时不会在源代码中迷失方向
#######################################################################################################################

#####################################################################################################################
# 第七章：再谈抽象，面向对象编程
#     1.创建自定义对象（尤其是对象类型或类）是一个Python核心概念。
#     2.本章中，将开始学习如何创建对象，还将学习多态，封装，方法，属性，超类和继承。
#     3.注意：本章不会讨论构造函数
####################################################################################################################
# 1.对象：表示一系列数据属性以及一套访问和操作这些数据的方法
#     对象的三个主要特征：多态，封装，继承
#     （1）多态:对不同类型的对象执行相同的操作，这些对象都可正常运行
#     （2）封装：对外部隐藏有关对象工作原理的细节
#     （3）继承：可基于通用类创建出专用类
#      repr(object):函数将对象转化为供解释器读取的形式，返回一个对象的string
######################################################################################################################
#   (1)多态: 多态形式是Python编程方式的核心，有时称为"鸭子类型"。这个术语源于以下说法："如果走起来像鸭子，那么它就是鸭子"

#   (2)封装：封装不同于多态，多态让你无需知道对象所属的类（对象的类型）就能调用其方法，而封装让你无需知道对象的
#   构造就能使用它
#   当调用方法时，无需操心其他事情，如避免干扰全局变量。那如何将名称”封装“在对象中呢？将其设置为一个属性即可
#   属性：属性是归属对象的变量，就像方法一样。实际上，方法差不多就是与函数相关联的属性。
#   (3)继承：更巧妙的偷懒方式，获取被继承类的属性和方法，并根据自身需要添加新的属性和方法
######################################################################################################################
#   2.类：每个对象都属于特定的类，并被称为该类的实例
# EXAMPLE：如果你在窗外看到一只鸟，这只鸟就是”鸟类“的一个实例，鸟类是一个非常通用（抽象）的类，它有多个子类：你看到的那只鸟
# 可能属于子类”云雀“。你可将鸟类视为所有的鸟组成的集合，而云雀是其中一个子类。“一个类的对象为另一个类的子集时，前者就是后者
# 的子类”。因此“云雀”为“鸟类”的子类，而“鸟类”为“云雀”的超类。
#   类的所有实例都有该类的所有方法，因此子类的所有实例都有超类的所有方法。有鉴于此，要定义子类，只需定义多出来的方法（或改写
#   一些既有的方法）

#   3.创建自定义类:  一个简单的实例
class Person:
    def set_name(self, name):
        self.name = name  # self指向对象本身

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello World! I'm {}.".format(self.name))


foo = Person()
bar = Person()
foo.set_name("Sam")  # 类中的方法必须有self参数指向自己，但在调用时可以省略这个参数
print(foo.get_name(), foo.name)
foo.greet()


#   4.属性，函数和方法
#   （1）方法和函数的区别主要表现在前一节提到的参数self上，方法（更准确地说是关联的方法）将其第一个参数关联到他所属的实例，
#    因此无需提供这个参数。
class Bird:
    song = 'quakauada'

    def sing(self):
        print(self.song)


bird = Bird()
bird.sing()
birdsong = bird.sing  # 用birdsong指向bird.sing这个类中方法，注意此处不是调用，所以bird.sing后没有()!
birdsong()


#   5.再谈隐藏：很多程序员都认为应该“完全对外部隐藏”对象的状态（即不能从外部访问它们）。因为其他程序员可能不知道（也不应
#   知道）对象内部发生的情况，例如，ClosedObject可能在对象修改其名称时向管理员发送电子邮件。这种功能可能包含在方法set_name
#   中。但如果直接设置c.name，结果将如何呢？什么都不会发生--根本不会发送电子邮件。为避免这类问题，可将属性定义为“私有”。
#   “私有属性”不能从对象外部访问，而只能通过“存取器”方法（如get_name和set_name）来访问
#   要让方法或属性称为私有的（不能从外部访问），只需让其名称以两个下划线打头即可
class Secretive:
    def __inaccessible(self):  # 私有方法
        print("Bet you can not see me...")

    def accessible(self):  # 公有方法
        print("The secret message is {}:".format(self.__a))
        self.__inaccessible()  # 类内部可以调用私有方法

    __a = 'dasdasd'  # 私有变量
    b = __a  # 公有变量


s = Secretive()
print(s.b)
s.accessible()  # 可通过共有方法调用私有方法
#   s.__inaccessibel()  #不能再类外部调用私有方法
#   小技巧：如何从类外部访问类内的属性或者方法？在类定义中，对所有以两个下划线打头的名称都进行转换，即在开头加上一个
#   下划线和类名。
#   格式：Secretive._Secretive__inaccessible
s._Secretive__inaccessible()  # . _  __的格式可以在类外访问类内的私有方法和属性
s._Secretive__a = 'ab'
print(s._Secretive__a)


#   总之，你无法禁止别人访问对象的私有方法和属性，但这种名称的修改方式发出了强烈的信号，让他们不要这么做
#   如果你不希望名称被修改，又想发出不要从外部修改属性或方法的信号，可用一个下划线打头。这虽然是一种约定，
#   但也有些作用。例如，from moudule import *不会导入以一个下划线打头的名称。
#   注：对于成员变量（属性），有些语言支持多种私有程度。例如，Java支持四种不同的私有程度。Python没有提供这样的
#   支持，不过从某种程度上说，以一个和两个下划线打头相当于两种不同的私有程度

#   类的命名空间：在class语句中定义的代码都是在一个特殊的命名空间（类的命名空间）内执行的，而类的所有成员都可访问
#   这个命名空间。
class MemberCounter:
    members = 0

    def set_name(self, name):
        print("my name is", name)

    name = 'Sam'

    def init(self):
        MemberCounter.members += 1


p1 = MemberCounter()
p2 = MemberCounter()
p1.set_name("Sam")
p1.init()
print(p1.members)
p2.set_name("Mike")
p2.init()
print(p2.members)


#   上述代码在类作用域内定义了一个变量，所有的成员（实例）都可访问它，这里使用它来计算类实例数量。这里使用它来计算类实例
#   的数量。注意到这里使用了init来初始化所有实例，第九章将把这个初始化过程自动化，也就是将init转换为合适的构造函数
#   6.指定超类：即子类指定父类class 子类（父类）
class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]  # 选出sequence中有但block中没有的返回


class SPAMFilter(Filter):  # SPAMFilter是Filter的子类
    def init(self):  # 重写超类Filter的方法init
        self.blocked = ['SPAM']


f = Filter()
f.init()
print(f.filter([1, 2, 3]))
s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))

#   7.深入探讨继承：
#   （1）要确定一个类是否是另一个类的子类，可使用内置方法issubclass
print(issubclass(SPAMFilter, Filter), issubclass(Filter, SPAMFilter))
#   （2）如果你有一个类，想知道它的基类，可访问其特殊属性__bases__
print(SPAMFilter.__bases__, Filter.__bases__)
#   （3）要确定对象是否是特定类的实例，可使用isinstance
s = SPAMFilter()
print(isinstance(s, SPAMFilter), isinstance(s, Filter), isinstance(s, int))

#   （4）如果你要熟悉对象属于那个类，可使用属性__class__
print(s.__class__)


#   8.多个超类：又被称为多重继承，前一节，肯定已经注意到了__base__属性可以获取类的基类，而积累可能有多个
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)  # eval返回字符串中代码执行结果


class Talker:
    def talk(self):
        print('Hi,my value is', self.value)


class TalkingCalculator(Calculator, Talker):
    pass


s = Talker()
s.dasdasd = 2  # 无论class中有没有这个属性，都可以加
s.value = 3
s.talk()

tc = TalkingCalculator()  # TalkingCalculator继承了Calcular和Talker两个超类，变成了可说话的计算器
tc.calculate("1+2*6")
tc.talk()
#   多重继承是一个功能强大的工具。然而。除非万不得已，否则应该避免使用多重继承，因为在有些情况下，他可能带来以外的“并发症”。
#   使用多重继承时，有一点务必注意:如果多个超类以不同的方式实现了同一个方法（即有多个同名方法），必须在class语句中小心排列
#   这些超类，因为位于前面的类的方法将覆盖位于后面的类的方法。因此，在前面的实例中，如果Calculator类包含方法talk，那么这个方法
#   将覆盖Talker类的方法talk（导致其不可访问）。若像下面这样反转超类的排列顺序：
#           class TalkingCalculator(Talker, Calculator): pass
#   将导致Talker的方法talk是可以访问的。多个超类的超类方法相同时，查找特定方法或属性时访问超类的顺序称为“方法解析顺序（MRO）”
#   它使用的算法非常复杂。但是效果极好，用户可能根本无需担心

#   9.抽象基类：Python通过引入模块abc提供了官方解决方案，这个模块为所谓的抽象基类提供了支持。一般而言，抽象类是不能（至少
#   不应该）实例化的类，其职责是定义子类应该实现的一组抽象方法
from abc import ABC, abstractmethod


class Talker(ABC):  # 继承抽象类
    @abstractmethod
    def talk(self):
        pass


#   形如@this的东西被称为装饰器，使用@abstractmethod来将方法标记为抽象的--在子类中必须实现的方法
class KKnigget(Talker):
    pass  # 使用了pass,没有重写抽象方法，依然没有对方法进行实例化，因此还是错误


# k = KKnigget()  #无法实例化，因为类中只有抽象方法
# print(isinstance(k, int))

class Knigget(Talker):
    def talk(self):
        print("Ni!")


a = Knigget()
print(isinstance(a, Talker))
a.talk()  # 重写了超类中的抽象方法，因此不会报错


# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
#     isinstance() 与 type() 区别：
#         type() 不会认为子类是一种父类类型，不考虑继承关系。
#         isinstance() 会认为子类是一种父类类型，考虑继承关系。
#      如果要判断两个类型是否相同推荐使用 isinstance()。
# 以下是 isinstance() 方法的语法:
# isinstance(object, classinfo)
# 参数：
#     object -- 实例对象。
#     classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
# 返回值：如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False

#   10.类注册：将一个类注册为另一个类，更加的多态
class Herring:
    def talk(self):
        print("Blub")


h = Herring()
print(isinstance(h, Talker))  # False
#   上述isinstance验证为false，但你可从Talker派生出Herring，这样就万事大吉了，但Herring可能是从他人的模块中导入的。
#   在这种情况下，就无法采取这样的做法。为解决这个问题，你可将Herring注册为Talker（而不从Herring和Talker派生出子类），
#   这样所有的Herring对象都将被视为Talker对象。
Talker.register(Herring)
print(Talker.register(Herring))
print(isinstance(h, Talker))


#   特例：
class Clam:
    pass


print(Talker.register(Clam))
print(issubclass(Clam, Talker))
c = Clam()
print(isinstance(c, Talker))
# c.talk()  #此处方法调用失败，因为c对象所对应的类中实际没有talk方法
#   换而言之，应将isinstance返回True视为一种“意图”表达，在这里，Clam有成为Talker的意图，本着鸭子类型的精神，我们相信
#   它能承担Talker的职责，但可悲的是它失败了~

#   关于面向对象的一些思考：
# 1.将相关的东西放在一起，如果一个函数操作一个全局变量，最好将他们作为一个类的属性和方法
# 2.不要让对象之间过去亲密。方法应只关心其所属实例的属性，对于其他实例的状态，让他们自己去管理就好了
# 3.谨慎继承，尤其是多重继承。继承有时很有用，但在有些情况下可能带来不必要的的复杂性。要正确地使用多重继承很难。
# 4.保持简单。让方法小而紧凑
#
# 确定需要哪些类以及这些类应包含哪些方法时，尝试像下面这样做：
# 1.将有关的问题的描述（程序需要什么）记录下来，并给所有的名词、动词和形容词加上标记
# 2.在名词中找出可能的类
# 3.在动词中找出可能的方法
# 4.在形容词中找出可能的属性
# 5.将找出的方法和属性分配给各个类
# 有了“面向对象模型”的草图后，还需考虑类和对象之间的关系（如继承或协作）以及他们的职责。为了进一步改进模型，可像下面这样做：
# 1.记录（或设想）一系列用例，即使用程序的场景，并尽力确保这些用例涵盖了所有的功能。
# 2.透彻而仔细地考虑每个场景，确保模型包含了所需的一切

#################################################################################################################
# 第七章小结：
# 1.对象:对象由属性和方法组成。属性不过是属于对象的变量，而方法是存储在属性中的函数。相比于其他函数，（关联的）方法有一个不同
# 之处，那就是他总是将其所属的对象作为第一个参数，而这个参数通常被命名为self
# 2.类类表示一组或一类对象，而每个对象都属于特定的类。类的主要任务是定义其实例将包含的方法
# 3.多态：多态指的是能够同样地对待不同的类型和类的对象，即无需知道对象属于哪个类就可调用其方法
# 4.封装：对象可能隐藏其内部状态。在有些语言中，这意味着对象的状态（属性）只能通过其方法来访问。在Python中，所有的属性都是
# 公有的，但直接访问对象的状态时程序员应该谨慎行事，因为这可能不经意间导致状态不一致
# 5.继承：一个类可以是一个或多个类的子类，在这种情况下，子类将继承超类的所有方法。你可指定多个超类，通过这样做可组合正交（独立
# 且不相关）的功能。为此，一种常见的做法是使用一个核心超类以及一个或多个混合超类。
# 6.接口和内省：一般而言，你无需过于深入地研究对象，而只依赖于多态来调用所需的方法。然而，如果要确定对象包含哪些方法或属性，
# 有一些函数可供你来完成这种工作
# 7.抽象基类:使用模块abc可创建抽象基类。抽象基类用于指定子类必须提供哪些功能。
#
# 本章介绍的新函数：
# callable(object)                                  判断对象是否可调用
# getattr(pbject,name[,default])                    获取属性的值，还可提供默认值
# hasattr(object，name)                             确定对象是否有指定的属性
# isinstance(object,class)                          确定对象是否是指定类的实例
# issubclass(A,B) 确定A是否是B的子类
# random.choice(sequence)                           从一个非空序列中随机选择一个元素
# setattr(object,namemvalue)                        将对象的指定属性设置为指定的值
# type(object)                                      返回对象的类型
#   下章预告：本章深入的学习了如何创建自定义对象，下章将介绍异常处理。
####################################################################################################################
###################################################################################################################
# 第八章：异常
#     将介绍Python的异常处理机制，学习如何创建和引发异常，以及各种异常处理方式
##################################################################################################################
#   1.什么是异常：Python使用异常对象来表示异常状态，并在遇到错误是引发异常。异常对象未被处理（或捕获）时，程序将终止并返回
#   一条错误信息（traceback）
#   事实上，异常都是某个类，你能以各种方式引发和捕获这些实例，从而逮住错误并采取措施，而不是放任整个程序失败
#   2.主动引发异常：raise函数
#   采用raise语句主动引发异常，参数为一个类（必须为Exceotion的子类）或实例作为参数，将类作为参数时，会自动创建一个实例。
#   一些Python内置的异常类
#   类名                                   描述
# Exception                   几乎所有的异常类都是从它派生而来
# AttributeError              引用属性或给它赋值失败时引发
# OSError                     操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
# IndexError                  使用序列中不存在索引时引发，为LookUpError的子类
# KeyError                    使用映射中不存在的键时引发，为LookUpError的子类
# NameError                   找不到名称变量时引发
# SyntaxError                 代码不正确时引发
# TypeError                   将内置操作或函数用于类型不正确的对象时引发
# ValueError                  将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适
# ZeroDivisionError           在除法或求模运算的第二个参数为0时引发

#   3.自定义的异常类：自定义异常类有时比内置异常类更容易说明错误类型
#   和创建其他类一样，但是务必直接或间接地继承Exception（这意味着从任何内置异常类派生都可以）。因此，自定义异常类代码如下：
class SomeCustomException(Exception):
    pass  # 工作量真的不大，如果你愿意，可以在自定义异常类中添加方法


#   4.异常捕获：使用try/except语句
#   练习1：让用户输入两个数，再将它们相除：
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(x / y)
#   为了捕获除0造成的错误，可改写上述代码为以下方式
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!")  # 触发除0则打印字符串中的内容，否则和不加try/except没区别


#   注意：异常从函数向外传播到调用函数的地方。如果在这里也没有被捕获，异常将向程序最顶层传播，这意味着你可使用
#   try/except来捕获他人所编写的函数引发的异常。相依内容，8.4讲解
#   4.1不提供参数的raise
#   有时抑制异常发生很有用，但有时引发异常是更佳的选择，下面的练习改进上方计算机，增加异常抑制/引发开关
class MuffledCalulaor:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Divison by zero is illegal!")
            else:
                raise  # 若无法处理异常，在except中使用不带参数的raise是不错的选择


#   注意:发生除零行为时，如果启用了“抑制”功能，方法cal将（隐式地）返回None。换言之，如果开启了“抑制”功能就不该依赖于返回值
calculator = MuffledCalulaor()
print(calculator.calc('40/45'))
# print(calculator.calc('10/0'))  #此时关闭了抑制功能，程序出错
calculator.muffled = True
print(calculator.calc('10/0'))  # 此时开启了抑制功能，程序可正常执行

#   4.2.多个except子句:一个try可跟多个except子句，用于处理多种异常
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!")  # 触发除0则打印字符串中的内容，否则和不加try/except没区别
except TypeError:
    print("That wasn't a number ,was it?")
#   4.3. 一箭双雕：如果要使用一个except子句捕获多种异常，可在一个元组中指定这些异常，如下所示：
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x / y)
except (ZeroDivisionError, NameError, TypeError):
    print('Your number were bogus...')

#   4.4. 捕获对象:要在except子句中访问异常对象本身，可使用两个而不是一个参数。（请注意，即便是你在捕获多个异常时，也只向
#   except提供了一个参数---一个元组。）需要让程序继续运行并记录错误时，这很有用。
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x / y)
except (ZeroDivisionError, NameError, TypeError) as e:
    print('Your number were bogus...', e)

#   4.5  一网打尽：如果你就是要使用一段代码捕获所有异常，你只需在except语句中不指定任何异常类即可
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x / y)
except:
    print('Your number were bogus...')
#   以上操作以后，用户怎么操作都可以
#   但是像这样捕获所有的异常很危险，因为这不仅会隐藏你有心理准备的错误，还会隐藏你没有考虑过的错误。
#   在大多数情况下，更好的选择是使用except Exception as e并对异常对象进行检查。这样做将让不是从Exception派生而来的为数不多的
#   异常成为漏网之鱼，其中包括SystemExit和KeyboardInterrupt，因为他们都是从BaseException（Exception）的超类派生来的

#   4.6 万事大吉时：在有些情况，在没有出现异常时执行一个代码块很有用。为此，可以像条件语句和循环一样，给try/except
#   语句添加一个else子句
try:
    print("A simple task")
except:
    print("What? Something went wrong?")
else:
    print("Ah...It went as planned.")

# 练习2：修改前面输入x / y的例子实现循环检错直到输入参数符合要求
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x/y is ', value)
    except:
        print('Invalid input .Please try again.')
    else:
        break
#   tips：前面说过仅当没有异常发生时，才会跳出循环（这是由else子句中的break语句实现的）换言之，只要出现错误，程序就会要求
#   用户提供新的输入
#   改进:一种更佳的替代方案是使用空的except子句来捕获所有属于类Exception（或其子类的）的异常，并结合except Exception as e
#   打印出更有用的错误消息
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x/y is ', value)
    except Exception as e:
        print('Invalid input: ', e)
        print('Please try again')
    else:
        break
#   4.7.最后，finally子句：可用于在发生异常时的清理工作，与try子句配套使用
#   finally子句非常适合用于确保文件或网络套接字等得以关闭，将在网络编程章节详细介绍
#   也可以一条语句中同时包含try、except、finally和else（或其中的三个）
try:
    1 / 0
except NameError:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print("Cleaning up.")


#   5.异常和函数：异常和函数有着天然的联系，如果不处理函数中引发的异常，它将向上传播到调用函数的地方。如果在那里也未得到
#   处理，异常将继续传播，直至到达主程序（全局作用域）。如果主程序中也没有异常处理程序，程序将终止并显示栈跟踪消息。
def faulty():
    raise Exception('Something is wrong')


def ignore_exception():
    faulty()


def handle_exception():
    try:
        faulty()
    except:
        print('Exception handle!')


#   faulty中引发的异常依次从faulty和ignore_exception向外传播，最终导致显示一条栈跟踪消息。调用handle_exception时，一场最终
#   传播到handle_exception，并被这里的try/except语句处理

#   6.异常之禅：
#   异常处理并不是很复杂。如果你知道代码可能引发某种异常，且不希望出现这种异常时程序终止并显示栈跟踪消息，可添加必要的try/except
#   或者try/finally（或结合使用）来处理它。
#   练习3：将if/else语句简化为tyr/except
def describe_person(person):
    print('Description of', person['name'])
    print('Age', person['age'])
    if 'occupation' in person:
        print('Occupation: ', person['occupation'])


# 这段代码很直观，但是效率不高，因为它必须查找两次'occupation'键：一次检查这个键是否存在（在条件中），另一次获取这个键关联
# 的值，以便将其打印出来。下面是另一种解决方案：

def describe_person(person):
    print('Description of person ', person['name'])
    print('Age:', person['age'])
    try:
        print('Occupation :', person['occupation'])
    except KeyError:
        pass


#   改成try/except之后的代码只查询一次字典，正确就打印，否则就pass，效率更高

#   7.不那么异常的情况:如果你只想发出“警告”，指出情况偏离了正轨，可使用模块warning中的函数warn
from warnings import warn

warn("I have got a bad feeling about this.")
#   警告只显示一次，如果再次运行最后一行代码，什么事情都不发生
#   filterwarnings方法等不详细介绍，可用时查阅

####################################################################################################################
# 第八章：异常处理小结
# 1.异常对象：异常情况（如发生错误）是用异常对象表示的。对于异常情况，有多种处理方式：如果忽略,将导致程序终止
# 2.引发异常：可使用raise语句来引发异常。它将一个异常类或异常实例作为参数，但你也可提供两个参数（异常和错误消息）。
# 如果在except子句中调用raise时没有提供任何参数，它将重新引发该子句捕获的异常。
# 3.自定义异常类：你可通过Exception派生来创建自定义的异常
# 4.异常捕获:要捕获异常，可在try语句中使用except子句。在except子句中，如果没有指定异常类，将捕获所有异常。你可指定
# 多个异常类，方法是将它们放在元组中。如果向except提供两个参数，第二个参数将关联到异常对象。在同一条try/except语句
# 中，可包含多个except子句，以便对不同的异常采取不同的措施。
# 5.else子句：除except子句外，你还可使用else子句，它在主try块没有引发异常时执行。
# 6.finally：要确保代码块（如清理代码）无论是否引发异常都将执行，可使用try/finally，并将代码放在finally子句中
# 7.异常和函数：在函数中引发异常时，异常将传播到调用函数的地方（对方法来说亦是如此）。
# 8.警告：警告类似于异常，但（通常）只打印一条错误信息。你可指定警告类别，他们是warning的子类。

# 本章介绍的新函数：
# warnings.fliterwarning(action,category = Warning,...)               用于过滤警告
# warning,warn(message,category=None)                                 用于发出警告
######################################################################################################################
