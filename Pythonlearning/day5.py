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