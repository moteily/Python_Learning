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
