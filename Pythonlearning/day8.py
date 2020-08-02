###################################################################################################################
# 第九章：魔法方法，特性和迭代器
#     在Python中，有些名称很特别，开头和结尾都有两个下划线。这样的拼写表示名称有特殊意义，因此绝不要在程序中创建这样的名称。
# 这样的名称中很大一部分都是魔法（特殊）方法的名称。如果你的对象实现了这些方法，他们将在特定的情况下（具体是哪种情况取决于方法
# 的名称）被Python调用，而几乎不需要直接调用
#     本章讨论几个重要的魔法方法，其中最重要的是__init__以及一些处理元素访问的方法（他们能够让你创建序列或映射），本章还将讨论
# 两个相关的主题：特性（property）和迭代器（iterator）。前者以前是通过魔法方法处理的，但现在通过函数property处理，而后者使用
# 魔法方法__iter__,这样其可用在for循环。
###################################################################################################################
#   1.构造函数：实质是初始化方法，命名为__init__，构造函数不同于普通方法的地方在于，将在对象创建后自动调用它们。
#   在Python中，创建构造函数很容易，只需将方法init的名称从普通的init改为魔法版__init__即可


class Foobar:
    def __init__(self):
        self.somevar = 42


f = Foobar()
print(f.somevar)


class Foobar2:
    def __init__(self, value=42):
        self.somevar = value


f = Foobar2('This is a constructor argument')  # 创建对象的同时就会调用初始化函数，对象的参数直接给__init__函数
print(f.somevar)


#   注意：Python提供了魔法方法__del__，也称作析构函数（destructor）。这个方法在对象被销毁（作为垃圾被收集）前被调用，
#   但鉴于你无法知道准确的调用时间，建议尽可能不要使用__del__

#   2.重写普通方法和特殊的构造函数
#   每个类都有一个或多个超类，并从它们那里继承行为。对类B的实例调用方法（或访问其属性）时，如果找不到该方法（或属性），将
#   将在其超类A中查找。请看下面两个类：
class A:
    def hello(self):
        print("Hello, I'm A.")


class B(A):
    pass


a = A()
b = B()
a.hello()
b.hello()


#   由于类B自己没有定义方法hello，因此对其调用方法hello时，打印的是消息“hello，I'm A.”。要在子类中添加功能，一种基本方式
#   是添加方法。然而，你可能想重写超类的某些方法，以定制继承而来的行为。例如，B可以重写方法hello：
class B(A):
    def hello(self):
        print("Hello, I'm B.")


b = B()
b.hello()


#   3.重写机制对构造函数来说尤其重要。重写构造函数时，必须调用超类（继承的类）的构造函数，否则无法争取的初始化对象。
#   有时子类重写了构造函数，但是新的构造函数没有包含其超类的初始化属性，就会发生错误。要消除这种错误，子类的构造函数必须调用其
#   超类的构造函数，以确保基本的初始化得以执行。为此，有两种方法，一种是调用未关联的超类构造函数，另一种使用函数super
#   3.1调用未关联的超类构造函数：
#   本节介绍的方法主要用于解决历史遗留问题。在较新的Python版本中，显然应使用函数super（这将在下一节讨论）。然而，调用未关联的
#   超类构造函数具有启迪意义，淋漓尽致说明了关联方法和未关联方法之间的差别。
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No, Thanks!')


class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()


#   这样做为何管用？对实例调用方法时，方法的参数self将自动关联到实例（成为关联的方法）。然而，如果你通过“类”调用方法（
#   如Bird.__init__）,就没有实例与其关联。在这种情况下，你可随便设置参数self。这样的方法成为“未关联的”

#   3.2 使用函数super:调用这个函数时，将当前类和当前实例作为参数。对其返回的对象调用方法时，调用的将是超类（而不是当前类）
#   的方法。因此，在SongBird的构造函数中，可不是用Bird，而使用super，如下

class SongBird(Bird):
    def __init__(self):
        super.__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


#   super相比未关联方法的优点：当有多个超类时，也只需调用super一次
#   super运行机制:super返回一个super对象，这个对象将负责为你执行方法解析。当你访问它的属性时，它将在所有的超类（以及超类的
#   超类，等等）中查找，直到找到指定的属性或引发AttributeError异常。
#   4.元素访问：
#   4.1基本的序列和映射协议：序列和映射基本上是“元素item”的集合，要实现他们的基本行为，不可变对象需要实现两个方法，
#   而可变对象需要实现四个：__len__(self),__getitem__(self,key),__setitem__(self,key,value),__delitem__
#   4.2 从list、dict和str派生
#   基本的序列/映射协议指定的四个方法能够让你走很远，但序列还有很多其他有用的魔法方法和普通方法，其中包括将在9.6节介绍的
#   方法__iter__。要实现所有这些方法，不仅工作量大，而且难度不小。如果只想定制某种操作的行为，就没有理由去重新实现其他所有
#   方法。那该如何做呢？ 继承！ 在标准库中，模块collections提供了抽象和具体的基类，但你也可以继承内置类型。因此，要实现
#   一种行为类似于内置列表的序列类型，可直接继承list。下面例子展示一个带访问计数器的列表！
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


c1 = CounterList(range(10))  # 这里的range（10）是给构造函数的参数
print(c1, c1.reverse(), c1[1] + c1[4], c1.counter)
print(c1, c1.reverse(), c1[1] + c1[4], c1.counter)


#   CounterList类深深地依赖于其超类（list）的行为。CounterList没有重写的方法（如append、extend、index等）都可以直接使用。在
#   两个被重写的方法中，使用super来调用超类的相应方法，并添加了必要的行为：初始化属性counter（在__init__中）和更新属性counyer\
#   (在__getitem__中)。
#   上面程序演示可知，CounterList的行为在大多数方面都类似于列表，但它有一个counter属性（其初始值为0）.每当你访问列表元素时，
#   这个属性的值都加1。执行加法运算c1[1]+c1[4]后，counter变成了2

#   5.特性property：Python能够替你隐藏存取方法，让所有的属性看起来都一样。通过存取方法定义的属性通常称为特性。
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)


r = Rectangle()
print(r.size)
r.width = 10
r.height = 5
# r.set_size([10, 18])
print(r.size)
r.size = 150, 100
print(r.width)
#   如你所见，属性size依然受制于get_size和set_size执行的计算，但看起来就像普通属性一样
#   事实上，调用函数property时，还可不指定参数，指定一个参数，指定三个参数或指定四个参数。如果没有指定任何参数，创建的特性
#   将既不可读也不可写。如果只指定一个参数（获取方法），创建的特性将是只读的。第三个参数是可选的，指定用于删除属性的方法（这个
#   方法不接受任何参数）。第四个参数也是可选的，指定一个文档字符串。这些参数分别名为fget、fset、fdel和doc。
#   如果你要创建一个只可写且带文档字符串的特性，可使用它们作为关键字参数来实现。
