#hello3.py
def hello():
    print('Hello333,World!')

#A test
#导入时这个测试代码会自动执行
#hello()
#为了避免导入程序时执行hello()方法，需要添加__main__变量判断

def test():
    hello()

if __name__ == '__main__': test()