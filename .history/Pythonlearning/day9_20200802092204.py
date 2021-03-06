# 接上一天的第九章
#   静态方法和类方法：
#   定义和表示：静态方法和类方法分别包装在staticmethod和classmethod类的对象中。
#   静态方法的定义中没有参数self，可直接通过类调用。类方法的定义中包含类似self的参数，
#   通常被命名为cls。对于类方法，也可通过对象直接调用，但参数cls将自动关联到类。如下

class Myclass:
    def smeth():
        print('This is a static method')
        smeth = staticmethod(smeth)

    def cmeth(cls)
        print('This is a class method of ', cls)
        cmeth = classmethod(cmeth)
