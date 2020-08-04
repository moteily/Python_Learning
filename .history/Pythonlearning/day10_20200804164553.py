############################################################################################################################
# 第十章：开箱即用（模块和程序）
############################################################################################################################
#   1.模块：模块就是程序，任何Python模块都可以作为模块导入
#   (1):可将模块hello.py保存到某个文件位置，然后通过:
#   import sys
#   sys.path.append('文件路径')
#   import hello(注意：此处去掉py就是模块)
#   sys.path.append函数告诉解释器，除了通常要查找的位置外，还要去刚才添加的目录中找
#   (2):模块是用来下定义的:让模块值得被创建的原因在于他们像类一样，有自己的作用域。这意味着在模块中定义的类和函数以及对其进行赋值
#   的变量都将成为模块的属性
import hello2
hello2.hello()
hello2.test()
print(hello2.__name__, __name__)
import sys, pprint
pprint.pprint(sys.path)  #Python解释器查找模块的目录列表
# [
#     'c:\\Users\\motei\\Desktop\\PyLearning\\Pythonlearning',
#     'D:\\Anaconda\\python37.zip', 'D:\\Anaconda\\DLLs', 'D:\\Anaconda\\lib',
#     'D:\\Anaconda',
#     'C:\\Users\\motei\\AppData\\Roaming\\Python\\Python37\\site-packages',
#     'D:\\Anaconda\\lib\\site-packages',
#     'D:\\Anaconda\\lib\\site-packages\\win32',
#     'D:\\Anaconda\\lib\\site-packages\\win32\\lib',
#     'D:\\Anaconda\\lib\\site-packages\\Pythonwin'
# ]
#   tips：如果打印的数据结构过大，一行容纳不下，可使用模块pprint中的函数pprint。pprint是一个卓越的打印函数
#   虽然以上路径中，你将自己建立的模块放到其中任意一个都可，但是目录site-packages是最佳的选择，因为它就是用来放置模块的（
#   例如可以直接将opencv模块导入到site-packages目录，解决了DLL load failed when import opencv）
#   除此之外，还可以将模块的路径加入到系统的环境变量中，环境变量并不是Python解释器的一部分，而是操作系统的一部分
#   除了环境变量外，还可以使用路径配置文件。这些文件的扩展名为.pth，位于一些特殊目录中，包含要添加到sys.path中的目录
#   3.包：为了组织模块，可将其编组为包（package）。包其实就是另一种模块，但有趣的是它们可包含其他模块。包是一个目录，
#   目录必须包含文件__init.py__，如果像普通模块一样导入包，文件init__.py的内容就将是包的内容
#   example:要将模块加入包，只需将模块文件放在包目录中即可。你还可以在包中嵌套其他包。例如要创建一个名为drawing的包，
#   其中包含模块shapes和colors，需要创建如下所示的文件和目录（unix）
#                     ~~~  一种简单的包布局   ~~~
# ~/python/                                                        PYTHPATH中的目录
# ~/python/drawing/                                                包目录（包drawing）
# ~/python/drawing/__init__.py                                     包代码（模块drawing）
# ~/python/drawing/colors.py                                       模块colors
# ~/python/drawing/shapes.py                                       模块shapes
#   完成上述操作后，下面的语句都是合法的：
#   import drawing
#   import drawing.colors
#   from drawing import shapes

import copy
from copy import PyStringMap  #以上两种import的区别:下面可直接调用PyStringMap,上面必须copy.PyStringMap
print(dir(copy), copy.__all__)  #__all__ = ['Error', 'copy', 'deepcopy']
#   dir函数将列出对象的所有属性（对于模块，它将列出所有的函数、类和变量等）
#   变量__all__:旨在定义模块中的公有接口。
#   若使用from copy import *将只能得到变量__all__中列出的4个函数。要导入PyStringMap，必须显式地：导入copy并使用copy.PyStringMap;
#   或者使用from copy import PyStringMap
#   编写自己的模块和包时，像这样设置__all__也很有用，因为模块可能包含大量其他程序不需要的变量、函数和类，比较周全的做法是将它们过滤掉，
#   如果不设置__all__，则会在以import *方式导入时，导入所有不以下划线大头的全局名称

#   (3):阅读Python模块的源码
#   通过模块的特性__file__阅读源码
print(copy.__file__)  #打印相应源码位置
#   有些源码你可能都不懂，特们可能是解释器的组成部分（如模块sys），还可能是使用c语言编写的

#   2.标准库：一些受欢迎的模块
#   在Python中，短语“开箱即用”最初是由Frank Stajano提出的，指的是Python丰富的标准库。这里对模块的描述并非面面俱到，只是将重点放在模块的
#   一些有趣功能上
#   1.sys模块:模块sys让你能够访问与Python解释器紧密相关的变量和函数，如下表：
#                     模块sys中一些重要的函数和变量
# 函数/变量                                                   描述
# argv                                                命令行参数，包括脚本名
# exit([arg])                                         退出当前程序，可通过可选参数指定返回值或错误信息
# modules                                             一个字典，将模块名映射到加载的模块
# path                                                一个列表，包含要在其中查找模块的目录的名称
# platform                                            一个平台标识符，如sunos5或win32
# stdin                                               标准输入流----一个类似于文件的对象
# stdout                                              标准输出流----一个类似于文件的对象
# stderr                                              标准错误流----一个类似于文件的对象

#   2.os模块：模块os让你能够访问多个操作系统服务
#                      模块os中一些重要的函数和变量
# environ                                               包含环境变量的映射
# system(command)                                       在shell中执行操作系统命令
# sep                                                   路径中使用的分隔符
# pathsep                                               分隔不同路径的分隔符
# linesep                                               行分隔符
# urandom(n)                                            返回n个字节的强加密随机数据

#   webbrowser模块：使用模块webbrowser模块，其包含一个open函数，让你能够启动web浏览器并打开指定url
#   import webbrowser
#   webbrowser.open('www.baidu.com')

#   3.fileinput模块：能够帮你轻松地迭代一系列文本文件中的所有行
#                       模块fileinput中一些重要的函数
# import fileinput
# input([files[,inplace[,backup]]])                       帮助迭代多个输入流中的行
# filename()                                              返回当前文件的名称
# lineno()                                                返回当前行号
# filelineno()                                            返回在当前文件中的行号
# isfirstline()                                           检查当前行是不是文件中的第一行
# isstdin()                                               检查最后一行是否来自sys.stdin
# nextfile()                                              关闭当前文件并移到下一个文件
# close()                                                 关闭序列
#   4.集合set:可用内置类函数set(序列)创建集合或者{1,2,3}，注意大括号中不能为空，否则会创建空字典
#   集合是用于判定成员权限等，集合进行各种交并补等逻辑运算
#   frozenset:集合是可变的，因此不能用作字典中的键，frozenset类型表示不可变（可散列）的集合。
#   构造函数frozenset创建给定集合的副本。在需要将集合作为另一个集合的成员或字典中的键时，frozenset很有用

#   5.堆；heap
#   堆特征：位置i出的元素总是大于位置i//2处的元素（反过来说就是小于位置2*i和2*i+1处的元素）
#   Python中没有独立的堆类型，只有一个包含一些堆操作函数的模块
#                                 模块heapq中一些重要的函数
# heappush(heap,x)                                         将X压入堆中
# heappop(heap)                                            从堆中弹出最小元素
# heapify(heap)                                            让列表具备堆特征
# heapreplace(heap,x)                                      弹出最小的元素，并将x压入堆中
# nlargest(n,iter)                                         返回iter中n个最大的元素
# nsmallest(n,iter)                                        返回iter中n个最小的元素
#   6.双端队列（及其他集合）
# 需要按添加元素的顺序进行删除时，双端队列很有用，在模块collection中，包含类型deque以及其他几个集合(collection)类型
# 双端队列很有用：因为它支持在队首（左端）高效地附加和弹出元素，而使用列表无法这样做。
# 另外，还可高效地旋转元素（将元素向右或向左移实现反转）

#   7.time模块：获取当前时间，操作时间和日期，从字符串中读取时间，将日期格式化为字符串的函数。
#                                模块time中一些重要函数
# 函数                                                        描述
# asctime([tuple])                                         将时间元组转化为字符串
# localtime([secs])                                        将秒数转换为表示当地时间的日期元组
# mktime(tuple)                                            将时间元组转换为当地时间
# sleep(secs)                                              休眠（什么都不做）secs秒
# strptime(string[,format])                                将字符串转化为时间元组
# time()                                                   当前时间（从新世纪之后的秒数）
# 模块datetime：提供了日期和时间算术支持
# 模块dateit:可帮助你计算代码段的执行时间

#   8.random模块：包含生成伪随机数的函数，有助于编写模拟程序或生成随机输出的程序。
#   如果你要求真正的随机（如用于加密或实现与安全相关的功能）,应考虑使用模块os中的函数urandom。模块random中
#   SystemRandom类基于的功能与urandom类似，可提供接近于真正随机的数据

#                              模块random中一些重要的函数
# random()                                                返回一个0~1的随机实数
# getrandbits(n)                                          以长整数方式返回n个随机的二进制
# uniform(a,b)                                            返回一个a~b的随机实数
# rangrange([start],stop,[step])                          从range(start,stop,step)中随机地选择一个数
# choice(seq)                                             从序列seq中随机地选择一个元素
# shuffle(seq[,random])                                   就地打乱序列seq
# sample(seq.n)                                           从序列seq中随机地选择n个值不同的元素

#   9.shelve和json：不详细记录了 暂时用不到

#   10.re模块:提供了对正则表达式的支持。正则表达式：可匹配文本片段的模式。最简单的正则表达式为普通字符串，他与自己匹配
#   正则表达式部分要点：
#   (1): '.'与除了'\'以外的所有字符匹配，被称为通配符
#   (2): 转义符的使用：r'python\.org'与'python\\.org'作用相同
#   (3):字符集：可以用方括号将一个子串扩起，创建一个所谓的字符集，字符集与其包含的字符都匹配。'[a-zA-Z0-9]'匹配大小写字母和数字
#   (4):脱字符:[^abc]与除a、b、c外其他任何字符都匹配
#   (5)二选一和子模式:管道字符'|',  'p(ython|erl)'匹配python和perl  ，小括号内的称为子模式
#   (6)可选模式和重复模式:子模式后面加上问号，可将其指定为可选的，即可包含可不包含。例子如下
#    r'(http://)?(www\.)?python\.org'只与下面这些字符串匹配：
#   'http://www.python.org'
#   'http://python.org'
#   'www.python.org'
#   'python.org'
#   对于这个示例需要注意以下几点:
#   对句点进行了转义，防止其成为通配符
#   为减少所需的反斜杆数量，我使用了原始字符
#   每个可选的子模式都放在括号内
#   每个可选的子模式都可出现也可不出现
#   指定字符串末尾用 $
#   其他与？作用类似的符号：
#   (pattern)*:pattern可重复0或1或多次
#   (pattern)+:pattern可重复1或多次
#   (pattern){m,n}:模式可重复m~n次

#   模块re的内容:包含了多个使用正则表达式的函数
# compile(pattern[,flags])                                        根据包含正则表达式的字符串创建模式对象
# search(pattern,string[,flags])                                  在字符串中查找模式
# match(pattern,string[,flags])                                   在字符串开头匹配模式
# split(pattern,string[,maxsplit= 0])                             根据模式来分割字符串
# findall(pattern,string)                                         返回一个包含所有字符串中与模式匹配的子串的列表
# sub(pat,repl,string[,count=0])                                  将字符串中与模式pat匹配的子串替换为repl
# escape(string)                                                  对字符串中所有的正则表达式特殊字符都进行转义

#   tip：函数match在模式于字符串开头匹配就返回True，而不要求模式与整个字符串匹配。如果要求与整个字符串匹配，需要在模式末尾加$
#   返回真都是指返回MatchObject，一个匹配字符串
#   11.匹配对象和编组:编组就是放在圆括号内的子模式，他们是根据左边的括号数编号的，编组0指整个模式
# 'There (was a (wee)(cooper)) who (lived in Fyfe)'
# 0 There was a wee cooper who lived in Fyfe
# 1 was a wee cooper
# 2 wee
# 3 cooper
# 4 lived in Fyfe

# re匹配对象的重要方法
# group([group1,...])                                                 获取与给定子模式（编组）匹配的子串
# start([group])                                                      返回与给定编组匹配的子串的起始位置
# end([group])                                                        返回与给定编组匹配子串的终止位置
# span([group])                                                       返回与给定编组匹配的子串的起始和终止位置

#   12.一个简单的模板系统实例
# 模板是一种文件，看似很复杂，但是有很多可供使用的工具。
# (1)可使用正则表达式来匹配字段并提取其内容
# (2)可使用eval来计算表达式字符串，并提供包含作用域的字典。可在try/except语句中执行这种操作。如果出现SystaxError异常，就说明
# 你处理的可能是语句(如赋值语句)而不是表达式，应用exec来执行它
# (3)可使用exec来执行语句字符串，并将模板的作用域存储到字典中
# (4)可使用re.sub将被处理的字符串替换为计算得到的结果
import fileinput, re
field_pat = re.compile(r'\[(.+?)\]')
scope = {}


def replacement(match):
    code = match.group(1)
    try:
        #若字段为表达式,就返回其结果
        return str(eval(code, scope))
    except SyntaxError:
        #否则在当前作用域内执行该赋值语句
        #并返回一个空字符串
        return ''


#获取所有文本并合并成一个字符串
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)
#替换所有与字段匹配的内容:
print(field_pat.sub(replacement, text))
# [x = 2]
# [y = 3]
# the sum of [x] and [y] is [x+y]
# 输出结果为:
# The sum of 2 and 3 is 5

# 简而言之:这个程序做了如下事情:
# (1)定义一个用于匹配字符串字段的模式
# (2)创建一个用作模板作用域的字典
# (3)定义一个替换函数,功能如下:
#     从match中获取与编组1匹配的内容,并将其存储到变量code中
#     将作用域字典作为命名空间,并尝试计算code,再将结果转换为字符串并返回它.如果成功,就说明这个字段是表达式,因此万事大吉,否则异常
#     在对表达式进行求值时使用的命名空间(作用域字典)中执行这个字段,并返回一个空串(因为赋值语句没有结果)
# (4)使用fileinput读取所有行,将它们放在一个列表中,再将其合并成一个大型字符串
# (5)调用re.sub来使用替换函数来替换所有与模式field_pat匹配的字段,并将结果打印出来

#   其他有趣的标准模块
# cmd:可以编写类似于Python交互式解释器的命令行解释器
# csv:CSV指的是逗号分隔符的值,很多程序(如很多电子表格程序和数据库程序)都使用这种简单格式来存储表格数据.这种
# 格式主要用于在不同的程序之间交换数据
# datetime:支持特殊的日期和时间对象,并让你能够以各种方法创建和合并这些对象
# difflib:可以确定两个序列的相似程度,让你能够从很多序列中找出与指定序列最为相似的序列
# enum:枚举类型
# functools:让你在调用函数时只提供部分参数,以后再填充其他参数
# statistics:计算标准差等
# timeit profile和trace:timeit是一个测量代码段执行时间的工具.profile可用于对代码段的效率进行更全面的分析.模块trace可帮助你进行覆盖率
# 分析(即代码的哪些部分执行了,哪些部分没有执行)

#################################################################################################################################
#           第十章小结:
#   本章介绍了如何创建模块,如何探索模块和如何使用python标准库中的一些模块
# 1.模块:模块基本上是一个子程序,主要作用是定义函数 类和变量等. 模块包含测试代码时,应将这些代码放在一条检查name == '__main__'的if语句中
# 2.包:包含其他模块的模块,包是使用包含文件__init__.py的目录实现的
# 3.探索模块:在交互式解释其中导入模块后,就可以众多不同的方式对其进行探索,其中包括使用dir 查看变量__all__以及函数help
# 4.标准库:
        # sys:访问多个与Python解释器关系密切的变量和函数
        # os:访问多个与操作系统关系密切的变量和函数
        # fileinput:让你轻松地迭代多个文件或流的内容行
        # sets,heapq,deque:集合,堆和双向队列
        # time:提供时间相关的函数
        # random:提供随机数函数
        # shelve:用于创建永久性映射,其内容存储在使用给定文件名的数据库中
        # re:支持正则表达式的模块

#################################################################################################################################