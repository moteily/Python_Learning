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
#   相比于函数property,这些魔法方法使用起来要ji'shou'xie

