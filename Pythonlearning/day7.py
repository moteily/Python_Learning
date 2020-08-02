###################################################################################################################
# 第八章：异常
#     将介绍Python的异常处理机制，学习如何创建和引发异常，以及各种异常处理方式
##################################################################################################################
#   1.什么是异常：Python使用异常对象来表示异常状态，并在遇到错误是引发异常。异常对象未被处理（或捕获）时，程序将终止并返回
#   一条错误信息（traceback）
#   事实上，异常都是某个类，你能以各种方式引发和捕获这些实例，从而逮住错误并采取措施，而不是放任整个程序失败
#   2.主动引发异常：raise函数
#   采用raise语句主动引发异常，参数为一个类（必须为Exceotion的子类）或实例作为参数，将类作为参数时，会自动创建一个实例。
#   一些Python内置的异常类
#   类名                                   描述
# Exception                   几乎所有的异常类都是从它派生而来
# AttributeError              引用属性或给它赋值失败时引发
# OSError                     操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
# IndexError                  使用序列中不存在索引时引发，为LookUpError的子类
# KeyError                    使用映射中不存在的键时引发，为LookUpError的子类
# NameError                   找不到名称变量时引发
# SyntaxError                 代码不正确时引发
# TypeError                   将内置操作或函数用于类型不正确的对象时引发
# ValueError                  将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适
# ZeroDivisionError           在除法或求模运算的第二个参数为0时引发

#   3.自定义的异常类：自定义异常类有时比内置异常类更容易说明错误类型
#   和创建其他类一样，但是务必直接或间接地继承Exception（这意味着从任何内置异常类派生都可以）。因此，自定义异常类代码如下：
class SomeCustomException(Exception):
    pass  # 工作量真的不大，如果你愿意，可以在自定义异常类中添加方法


#   4.异常捕获：使用try/except语句
#   练习1：让用户输入两个数，再将它们相除：
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(x / y)
#   为了捕获除0造成的错误，可改写上述代码为以下方式
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!")  # 触发除0则打印字符串中的内容，否则和不加try/except没区别


#   注意：异常从函数向外传播到调用函数的地方。如果在这里也没有被捕获，异常将向程序最顶层传播，这意味着你可使用
#   try/except来捕获他人所编写的函数引发的异常。相依内容，8.4讲解
#   4.1不提供参数的raise
#   有时抑制异常发生很有用，但有时引发异常是更佳的选择，下面的练习改进上方计算机，增加异常抑制/引发开关
class MuffledCalulaor:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Divison by zero is illegal!")
            else:
                raise  # 若无法处理异常，在except中使用不带参数的raise是不错的选择


#   注意:发生除零行为时，如果启用了“抑制”功能，方法cal将（隐式地）返回None。换言之，如果开启了“抑制”功能就不该依赖于返回值
calculator = MuffledCalulaor()
print(calculator.calc('40/45'))
# print(calculator.calc('10/0'))  #此时关闭了抑制功能，程序出错
calculator.muffled = True
print(calculator.calc('10/0'))  # 此时开启了抑制功能，程序可正常执行

#   4.2.多个except子句:一个try可跟多个except子句，用于处理多种异常
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!")  # 触发除0则打印字符串中的内容，否则和不加try/except没区别
except TypeError:
    print("That wasn't a number ,was it?")
#   4.3. 一箭双雕：如果要使用一个except子句捕获多种异常，可在一个元组中指定这些异常，如下所示：
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x / y)
except (ZeroDivisionError, NameError, TypeError):
    print('Your number were bogus...')

#   4.4. 捕获对象:要在except子句中访问异常对象本身，可使用两个而不是一个参数。（请注意，即便是你在捕获多个异常时，也只向
#   except提供了一个参数---一个元组。）需要让程序继续运行并记录错误时，这很有用。
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x / y)
except (ZeroDivisionError, NameError, TypeError) as e:
    print('Your number were bogus...', e)

#   4.5  一网打尽：如果你就是要使用一段代码捕获所有异常，你只需在except语句中不指定任何异常类即可
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x / y)
except:
    print('Your number were bogus...')
#   以上操作以后，用户怎么操作都可以
#   但是像这样捕获所有的异常很危险，因为这不仅会隐藏你有心理准备的错误，还会隐藏你没有考虑过的错误。
#   在大多数情况下，更好的选择是使用except Exception as e并对异常对象进行检查。这样做将让不是从Exception派生而来的为数不多的
#   异常成为漏网之鱼，其中包括SystemExit和KeyboardInterrupt，因为他们都是从BaseException（Exception）的超类派生来的

#   4.6 万事大吉时：在有些情况，在没有出现异常时执行一个代码块很有用。为此，可以像条件语句和循环一样，给try/except
#   语句添加一个else子句
try:
    print("A simple task")
except:
    print("What? Something went wrong?")
else:
    print("Ah...It went as planned.")

# 练习2：修改前面输入x / y的例子实现循环检错直到输入参数符合要求
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x/y is ', value)
    except:
        print('Invalid input .Please try again.')
    else:
        break
#   tips：前面说过仅当没有异常发生时，才会跳出循环（这是由else子句中的break语句实现的）换言之，只要出现错误，程序就会要求
#   用户提供新的输入
#   改进:一种更佳的替代方案是使用空的except子句来捕获所有属于类Exception（或其子类的）的异常，并结合except Exception as e
#   打印出更有用的错误消息
while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x/y is ', value)
    except Exception as e:
        print('Invalid input: ', e)
        print('Please try again')
    else:
        break
#   4.7.最后，finally子句：可用于在发生异常时的清理工作，与try子句配套使用
#   finally子句非常适合用于确保文件或网络套接字等得以关闭，将在网络编程章节详细介绍
#   也可以一条语句中同时包含try、except、finally和else（或其中的三个）
try:
    1 / 0
except NameError:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print("Cleaning up.")


#   5.异常和函数：异常和函数有着天然的联系，如果不处理函数中引发的异常，它将向上传播到调用函数的地方。如果在那里也未得到
#   处理，异常将继续传播，直至到达主程序（全局作用域）。如果主程序中也没有异常处理程序，程序将终止并显示栈跟踪消息。
def faulty():
    raise Exception('Something is wrong')


def ignore_exception():
    faulty()


def handle_exception():
    try:
        faulty()
    except:
        print('Exception handle!')


#   faulty中引发的异常依次从faulty和ignore_exception向外传播，最终导致显示一条栈跟踪消息。调用handle_exception时，一场最终
#   传播到handle_exception，并被这里的try/except语句处理

#   6.异常之禅：
#   异常处理并不是很复杂。如果你知道代码可能引发某种异常，且不希望出现这种异常时程序终止并显示栈跟踪消息，可添加必要的try/except
#   或者try/finally（或结合使用）来处理它。
#   练习3：将if/else语句简化为tyr/except
def describe_person(person):
    print('Description of', person['name'])
    print('Age', person['age'])
    if 'occupation' in person:
        print('Occupation: ', person['occupation'])


# 这段代码很直观，但是效率不高，因为它必须查找两次'occupation'键：一次检查这个键是否存在（在条件中），另一次获取这个键关联
# 的值，以便将其打印出来。下面是另一种解决方案：

def describe_person(person):
    print('Description of person ', person['name'])
    print('Age:', person['age'])
    try:
        print('Occupation :', person['occupation'])
    except KeyError:
        pass


#   改成try/except之后的代码只查询一次字典，正确就打印，否则就pass，效率更高

#   7.不那么异常的情况:如果你只想发出“警告”，指出情况偏离了正轨，可使用模块warning中的函数warn
from warnings import warn

warn("I have got a bad feeling about this.")
#   警告只显示一次，如果再次运行最后一行代码，什么事情都不发生
#   filterwarnings方法等不详细介绍，可用时查阅

####################################################################################################################
# 第八章：异常处理小结
# 1.异常对象：异常情况（如发生错误）是用异常对象表示的。对于异常情况，有多种处理方式：如果忽略,将导致程序终止
# 2.引发异常：可使用raise语句来引发异常。它将一个异常类或异常实例作为参数，但你也可提供两个参数（异常和错误消息）。
# 如果在except子句中调用raise时没有提供任何参数，它将重新引发该子句捕获的异常。
# 3.自定义异常类：你可通过Exception派生来创建自定义的异常
# 4.异常捕获:要捕获异常，可在try语句中使用except子句。在except子句中，如果没有指定异常类，将捕获所有异常。你可指定
# 多个异常类，方法是将它们放在元组中。如果向except提供两个参数，第二个参数将关联到异常对象。在同一条try/except语句
# 中，可包含多个except子句，以便对不同的异常采取不同的措施。
# 5.else子句：除except子句外，你还可使用else子句，它在主try块没有引发异常时执行。
# 6.finally：要确保代码块（如清理代码）无论是否引发异常都将执行，可使用try/finally，并将代码放在finally子句中
# 7.异常和函数：在函数中引发异常时，异常将传播到调用函数的地方（对方法来说亦是如此）。
# 8.警告：警告类似于异常，但（通常）只打印一条错误信息。你可指定警告类别，他们是warning的子类。

# 本章介绍的新函数：
# warnings.fliterwarning(action,category = Warning,...)               用于过滤警告
# warning,warn(message,category=None)                                 用于发出警告
######################################################################################################################
