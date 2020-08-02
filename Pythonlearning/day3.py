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
