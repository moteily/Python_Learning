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
print(copy.__file__)    #打印相应源码位置
#   有些源码你可能都不懂，特们可能是解释器的组成部分（如模块sys），还可能是使用c语言编写的

#   2.标准库：一些受欢迎的模块
