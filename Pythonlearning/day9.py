# 接上一天的第九章
#   静态方法和类方法：
#   定义和表示：静态方法和类方法分别包装在staticmethod和classmethod类的对象中。
#   静态方法的定义中没有参数self，可直接通过类调用。类方法的定义中包含类似self的参数，
#   通常被命名为cls。对于类方法，也可通过对象直接调用，但参数cls将自动关联到类。如下
class Myclass:
    def smeth():
        print('This is a static method')
        smeth = staticmethod(smeth)

    def cmeth(cls):#类方法的特有参数
        print('This is a class method of ', cls)
        cmeth = classmethod(cmeth)

#   像这样手工包装和替换方法有点繁琐。引入了一种名为装饰器的新方法，可用于像这样包装方法.
#   (实际上,装饰器可用于包含任何可调用的对象,并且可用于方法和函数)可指定一个或多个装饰器
#   ,为此可在方法(或函数)前面使用运算符@列出这些装饰器(指定了多个装饰器,应用的顺序与列出
#   的顺序相反)
class Myclass:
    @staticmethod
    def smeth():
        print('This is a static method')

    @classmethod
    def cmeth(cls):
        print('This is a class method of',cls)
#   定义这些方法后,就像下面这样使用它们(无需实例化类):
Myclass.smeth()
Myclass.cmeth()

#   __getattr__ ,__setattr等方法
#   可以拦截对象对象属性的所有访问企图,其用途之一是在旧类中实现特性(在旧式类中,函数property的
#   的行为可能不符合预期)要在属性被访问时执行一段代码,必须使用一些魔法方法.
#   下面的四个魔法方法提供了你需要的所有功能(在旧式类中,只需使用后面三个)
#   __getattribute__(self,name):在属性被访问时自动调用(只适用于新式类)
#   __getattr__(self,name):在属性被访问而对象没有这样的属性自动调用
#   __setattr(self,name,value):试图给属性赋值时自动调用
#   __delattr__(self,name):试图删除属性时自动调用
#   相比于函数property,这些魔法方法使用起来要棘手些(从某种程度上说,效率也更低)

#   迭代器:__iter__,是迭代器的基础
#   生成器：关键字yield
#############################################################################################################################
#   第九章小结：
#   1.新式类和旧式类：新式类支持super和property，而旧式类不支持
#   3.构造函数:很多面向对象语言中都有构造函数，对于你自己编写的类，都可能需要为他实现一个构造函数。构造函数
#   名称为__init__,在对象创建后自动调用
#   4.重写：类可以重写其超类中定义的方法（以及其他任何属性）为此只需实现这些方法即可。要调用被重写的版本，，可直接通过超类调用未关联
#   版本（旧式类），也可以使用函数super调用（新式类）
#   5.序列和映射：要创建自定义的序列或映射，必须实现序列和映射协议指定的所有方法，其中包括__getitem__和__setitem__等魔法方法。通过list
#   （或UserList）和dict（或UserDict）派生，可减少很多工作量。
#   6.迭代器:简单的说，迭代器是包含方法__next__的对象，可用于迭代一组值。没有更多的值可供迭代时，方法__next__应引发StopIteration异常
#   可迭代对象包含方法__iter__，它返回一个像序列一样可用于for循环中的迭代器。通常，迭代器也是可迭代的，即包含返回迭代器本身的方法__iter__
#   7.生成器：生成器的函数是包含关键字yield的函数，它被调用时返回一个生成器，即一种特殊的迭代器，要与活动的生成器交互，可使用send throw close

# 本章介绍的新函数:
# iter(obj)                       从可迭代对象创建一个迭代器
# next(it)                        让迭代器前进一步并返回下一个元素
# property(fget,fset,fdel,doc)    返回一个特性，所有参数都是可选的
# super(class,obj)                返回一个超类的关联实例