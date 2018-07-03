#5.7 三人行
#另外三个语句，pass,del,exec

#5.7.1 什么都没发现
#pass
#Python中空代码块是非法的,解决方法是在语句块中加上一个pass语句
name = 'test'
if name == 'Ralph Auldus Melish':
    print('Welcome!')
elif name == 'Enid':
    #还没完。。
    pass
elif name == 'Bill Gates':
    print('Access Denied')

#5.7.2 使用del删除

#一般来说,Python会删除那些不再使用的对象(因为使用者不会再通过任何变量或者数据结构引用它们):

scoundrel = {'age':42,'first name':'Robin','last name': 'of locksley'}
robin = scoundrel

print(scoundrel)
print(robin)

scoundrel = None
print(robin)
robin = None
#首先，robin和scoundrel 都被绑定到同一个字典上,所以当设置scoundrel为None的时候，字典通过robin还是可用的
#当robin也被设置为None时,字典就“漂”再内存里面了，没有任何名字绑定在它上面，
#也就没有办法获取和使用它，因此python解释器会直接删除该字典，进行“垃圾收集”

#通过del语句同样能做到这一点，它不仅会移除一个对象的引用，也会移除那个名字本身
x = 1
del x
#print(x)   name 'x' is not defined

#另一个例子

x = ["hello",'world']
y =x
y[1] = 'Python'
print(x)
del x
print(y)

#x的删除并不影响y，原因就是删除的只是名称，而不是列表本身(值)
#事实上，在Python中是没有办法删除值的(也不需要过多考虑删除值的问题，因为在某个值不再使用的时候，
#Python解释器会负责内存的回收)

#5.7.3 使用exec和eval执行和求值字符串

#1.exec
#执行一个字符串的语句是exec
exec("print('Hello,world!')")

#命名空间或称作 作用域(scope)，可以想象成保存变量的地方，类似于不可见的字典
from math import sqrt
scope = {}
exec('sqrt = 1',scope)
sqrtTest = sqrt(4)
print(sqrtTest)
sqrtTest = scope['sqrt']
print(sqrtTest)

#原来的sqrt函数能正常工作，而通过exec赋值的变量sqrt只在它的作用域内有效

#打印scope，其中内建的__builtins__字典自动包含所有的内建函数和值:

print(str(len(scope)))
scopeTest = scope.keys()
print(scopeTest)

#2. eval
#eval (用于“求值”)是类似于exec的内建函数,exec语句会执行一系列Python语句,而eval会计算Python表达式(以字符串形式
#书写),并且返回结果值

#例
'''

evalTest = eval(input("Enter an arithmetic expression: "))
print(evalTest)
'''
#给exec或者eval语句提供命名空间时,可以在使用命名空间前放置一些值进去

scope = {}
scope['x'] = 2
scope['y'] = 3
evalTest = eval('x * y',scope)
print(evalTest)

scope = {}
exec('x=2',scope)

evalTest = eval('x*x',scope)
print(evalTest)

