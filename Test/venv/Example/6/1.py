#第6章 抽象

#斐波那契数列

def fibs(num):

    fibs = [0,1]
    for i in range(num):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs

print(fibs(10))

#6.3 创建函数
#函数是可调用的（可能带有参数，也就是放在圆括号中的值），它执行某种行为并且返回一个值，
#一般来说，内建的callbale函数可以用来判断函数是否可调用
import math
x = 1
y = math.sqrt
'''
#函数callable在Python3.0中不再可用，需要使用表达式hasattr(func,__call__)代替
callableTest = callable(x)
print(callableTest)
callableTest = callable(y)
print(callableTest)
'''
hasattrTest = hasattr(x,'__call__')
print(hasattrTest)
hasattrTest = hasattr(y,'__call__')
print(hasattrTest)


#创建函数 例
def hello(name):
    return 'Hello,' + name + '!'
print(hello('world!'))
print(hello('Gumby'))

#6.3.1 文档化函数
#注释以#开头，，或者在def语句后面以及在模块或者类的开头写下字符串，它就会作为函数的一部分进行存储
#这称为文档字符串

def square(x):
    'Calculates the square of the number x.'
    return x*x
#文档字符串可以按如下方式进行访问
docTest = square.__doc__
print(docTest)

#__doc__是函数属性,属性中的双下划线表示它是个特殊属性

#通过在交互式解释器中使用内建help函数，就可以得到挂怒函数包括它的文档字符串的信息
help(square)

#6.3.2 并非真正函数的函数
#python函数可以没有返回值，此时试图获取函数返回值时，将自动返回None

def test():
    print('This is printed')
    return
    print('This is not')

x = test()
print(x)

#6.4 参数魔法
#6.4.1 值从哪里来

#写在def语句中函数名后面的变量通常叫做函数的形参,而调用函数时提供的值时实参，或称为参数

#6.4.2 我能改变参数吗
#在函数内为不可变参数赋予新值不会改变外部任何变量的值
#示例
def try_to_change(n):
    n = 'Mr.Gumby'
name = 'Mrs.Entity'
try_to_change(name)
print(name)

#在try_to_change内，参数n获得了新值，但是它没有影响到name变量,n实际上是个完全不同的变量，如下:

name = 'Mrs.Entity'
n = name #这句的作用基本上等于传参数
n = 'Mr.Gumby' #在函数内完成的
print(name)

#参数 存储在局部作用域(local scope)内


#字符串(以及数字和元组)是不可变的，即无法被修改(也就是说只能用新的值覆盖)

def change(n):
    n[0] = 'Mr.Gumby'
names = ['Mrs.Entity','Mrs.Thing']
change(names)
print(names)

#不用函数示例
names = ['Mrs.Entity','Mrs.Thing']
n = names #再来一次，模拟传参行为
n[0] = 'Mr.Gumby' #改变列表
print(names)

#避免引用变量的影响，使用分片得到副本

names = ['Mrs.Entity','Mrs.Thing']
n = names[:]
print(n is names)
print(n == names)
#改变n不影响names
n[0] = 'Mr.Gumby'
print(n)
print(names)

change(names[:])
print(names)

#1.为什么要修改参数

#编写一个存储名字并且能用名字，中间名或姓查找联系人的程序:

storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}
me = 'Magnus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]

print(storage['last']['Hetland'])

#使用函数复用
#初始化函数
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

#获得名字的函数: 通过get避免抛出异常，查询不到的情况下返回None,data[label][name]会抛出异常
def lookup(data,label,name):
    return data[label].get(name)

#存储函数
def store(data,full_name):
    names = full_name.split()
    if len(names) == 2:names.insert(1,'')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames,'Magnus Lie Hetland')
lookupTest = lookup(MyNames,'middle','Lie')
print(lookupTest)

store(MyNames,'Robin Hood')
store(MyNames,'Robin Locksley')
result = lookup(MyNames,'first','Robin')
print(result)
store(MyNames,'Mr.Gumby')
result = lookup(MyNames,'middle','')
print(result)

#如果某些人的名字，中间名后者姓相同，那么结果中会包含所有这些人的信息











