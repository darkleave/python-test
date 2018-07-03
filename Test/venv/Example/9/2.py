#9.3 成员访问

#9.3.1 基本的序列和映射规则

#序列和映射时对象的集合，为了实现它们的基本的行为(规则),如果对象是不可变的，
#那么就需要使用两个魔法方法，如果是可变的就需要使用4个

#__len__(self):这个方法应该返回集合中所含项目的数量。对于序列来说，这就是元素的个数；
#对于映射来说，则是键值对的数量，如果__len__返回0（并且没有实现重写该行为的__nonzero__),
#对象会被当作一个布尔变量中的假值(空的列表，元组，字符串和字典也一样）进行处理.

#__getitem__(self,key):这个方法返回与所给键对应的值.对于一个序列，
#键应该是一个0-n-1的整数(或者像后面所说的负数),n是序列的长度；对于映射来说，可以使用任何种类的键
#__setitem__(self,key,value):这个方法应该按一定的方式存储和key相关的value,该值随后可使用
#__getitem__来获取,当然，只能为可以修改的对象定义这个方法.

#__delitem__(self,key):这个方法在对一部分对象使用del语句时被调用，同时必须删除和键相关的键。
#这个方法也是为可修改的对象定义的（并不是删除全部的对象，而只删除一些需要移除的元素)

#附加要求:

#对于一个序列来说，如果键是负整数，那么要从末尾开始计数，换句话说就是x[-n]和x[len(x)-n]是一样的.

#如果键是不合适的类型(例如，对序列使用字符串作为键),会引发一个TypeError异常

#如果序列的索引是正确的类型，但超出了范围,应该引发一个IndexError异常.
#https://www.cnblogs.com/idontknowthisperson/archive/2016/08/21/5792690.html
#python 3整型没有限制大小，因此可以当作long类型使用，因此python3没有python2的long 类型
def checkIndex(key):
    if not isinstance(key,(int)):raise TypeError
    if key<0: raise IndexError

class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        self.start = start
        self.step = step
        self.changed = {}
    def __getitem__(self, key):
        checkIndex(key)

        try: return self.changed[key]
        except KeyError:
            return self.start + key*self.step
    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value

s = ArithmeticSequence(1,2)
print(s[4])
s[4] = 2
print(s[4])
print(s[5])

#9.3.2 子类化列表，字典和字符串

# 当子类化一个内建类型——比如list的时候，也就简介地将object子类化了,因此该类就自动称为新式类,
#这就意味着可以使用像super函数这样的特性了

class CounterList(list):
    def __init__(self,*args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super().__getitem__(index)

cl = CounterList(range(10))
print(cl)
cl.reverse()

print(cl)
del cl[3:6]
print(cl)
print(cl.counter)
cl[4] + cl[2]
print(cl.counter)

#9.4 更多魔力

#特殊函数的更多内容参考 http://www.python.org/doc/ref/specialnames.html)

#9.5 属性

#Python 能隐藏访问器方法,让所有特性看起来一样，这些通过访问器定义的特性被称为属性

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width,self.height = size
    def getSize(self):
        return self.width,self.height

r = Rectangle()
r.width = 10
r.height = 5
print(r.getSize())
r.setSize((150,100))
print(r.width)

#9.5.1 property 函数

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width,self.height = size
    def getSize(self):
        return self.width,self.height
    size = property(getSize,setSize)

r = Rectangle()
r.width = 10
r.height = 5
print(r.size)
r.size = 150,100
print(r.width)

#size 特性虽仍然取决于getSize和setSize中的计算,但它们看起来就像普通的属性一样.

#理论上说，在新式类中应该使用property函数而不是访问器方法

#9.5.2 静态方法和类成员方法

#静态方法和类成员方法分别在创建时分别被装入staticmethod类型和classmethod类型的对象中,
#静态方法的定义没有self参数，且能够被类本身直接调用，类方法在定义时需要名为cls的类似于self的参数,
#类成员方法可以直接用类的具体对象调用,但cls参数是自动被绑定到类的

class MyClass:
    def smeth():
        print('This is a static method')
    smeth = staticmethod(smeth)
    def cmeth(cls):
        print('this is a class method of',cls)
    cmeth = classmethod(cmeth)

m = MyClass()
MyClass.smeth()

MyClass.cmeth()

class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')
    @classmethod
    def cmeth(cls):
        print('This is a class method of ',cls)
    def test(self):
        print('test:',self)
m = MyClass()
MyClass.smeth()

MyClass.cmeth()

m.test()


#静态方法和类成员方法在Python中向来不是很重要，主要的原因是大部分情况下可以使用函数或者绑定方法代替.

#9.5.3 __getattr__,__setattr__和它的朋友们

#拦截(intercept)对象的所有特性访问是可能的，这样可以用旧式类实现属性(因为property方法不能使用),
#为了在访问特性的时候可以执行代码,必须使用一些魔法方法,下面的4中方法提供了需要的功能

#__getattribute__(self,name):当特性name被访问时自动被调用(只能在新式类中使用)
#__getattr__(self,name):当特性name被访问切对象没有相应的特性时被自动调用.
#__setattr__(self,name,value):当试图给特性name赋值时会被自动调用
#__delattr__(self,name):当试图删除特性name时被自动调用

#尽管和使用property函数相比有点复杂(而且在某些方面效率更低),但这些特殊方法是强大的,因为可以
#对处理很多属性的方法进行再编码

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width,self.height = value
        else:
            self.__dict__[name] = value
    def __getattr__(self, name):
        if name == 'size':
            return self.width,self.height
        else:
            raise AttributeError

r = Rectangle()
r.test = '111'

r.size = (100,50)

print(r.test)

print(r.size)

#__setattr__方法在所涉及的特性不是size也会被调用,因此这个方法必须把两方面都考虑进去:
#如果属性是size,那么就像前面那样执行操作,否则就要使用特殊方法__dict__,该特殊方法包含一个字典
#字典里面是所有实例的属性,为了避免方法__setattr__方法被再次调用(这样会使程序陷入死循环),__dict__方法
#被用来代替普通的特性赋值操作

#__getattr__方法只在普通的特性没有被找到的时候调用,这就是说如果给定的名字不是size，这个特性不存在，
#这个方法就会引发一个AttributeError异常.


