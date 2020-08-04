#   被day10.py所引用
#   一个包含有条件执行的测试代码的模块
#   __name__：当程序以当前文件执行，那么__name__为main，若被其他.py  import后执行，则表示函数名
#   如果将这个模块作为程序运行，将执行函数hello；如果导入它，其行为将像普通模块一样
def hello():
    print("Hello World!")


def test():
    hello()

def test2():
    hello()

if __name__ == '__main__':
    test()