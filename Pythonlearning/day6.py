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
# issubclass(A,B)                                   确定A是否是B的子类
# random.choice(sequence)                           从一个非空序列中随机选择一个元素
# setattr(object,namemvalue)                        将对象的指定属性设置为指定的值
# type(object)                                      返回对象的类型
#   下章预告：本章深入的学习了如何创建自定义对象，下章将介绍异常处理。
####################################################################################################################