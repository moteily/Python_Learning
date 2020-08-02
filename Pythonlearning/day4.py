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