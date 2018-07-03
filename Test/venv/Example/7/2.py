#7.2.2 创建自己的类

#__metaclass__ = type #确定使用新式类

class Person:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print("Hello,world! I'm %s." % self.name)



#所谓的旧式类和新式类之间是有区别的，除非实在Python 3.0之前版本中默认附带的代码，否则再继续使用旧式类已无必要
#新式类的语法中，需要在模块或者脚本开始的地方放置赋值语句__metaclass__ = type
#在Python 3.0中，旧式类已经不存在了
#由类创建对象
foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anak in Skywalker')
foo.greet()
bar.greet()

#从外部访问特性

name = foo.name
print(name)
name = bar.name
print(name)
bar.greet()

#7.2.3 特性，函数和方法

#self参数事实上正是方法和函数的区别.
#方法（更专业一点可以称为绑定方法）将它们的第一个参数绑定到所属的实例上，因此无需显示提供该参数
#也可以将特性绑定到一个普通函数上，这样就不会由特殊的self参数了:

class Class:
    def method(self):
        print('I have a self')

def function():
    print("i don't...")
instance = Class()
instance.method()
instance.method = function
instance.method()

#self 参数并不依赖于调用方法的形式:

class Bird:
    song = 'Squaawk!'
    def sing(self):
        print(self.song)
bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()

#尽管最后一个方法调用看起来与函数调用十分相似,但是变量birdsong引用绑定方法bird.sing 上，
#也就意味着还是会对self参数进行访问(也就是说，它仍旧绑定到类的相同实例上)

#私有化
#默认情况下，程序可以从外部访问一个对象的特性.这样破坏了封装的原则
#对象的状态对于外部应该是完全隐藏的

#比如,ClosedObject可能会在其他对象更改自己名字的时候，给一些管理员发送邮件，
#这应该是setName方法的一部分，但是如果直接使用c.name设置名字，就什么都不会发生了.
#为了避免这种事情的发生，应该使用私有(private)特性，这时外部对象无法访问私有特性，只能通过
#getName和setName访问器(accessor)来访问特性.

#Python 并不直接支持私有形式，可以用一些小技巧来达到私有特性的效果
#为了让方法或者特性变为私有(从外部无法访问），只要在名字前面加上双下划线即可:
class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me...")
    def accessible(self):
        print("The secret message is：")
        self.__inaccessible()
s = Secretive()
s.accessible()

#类的所有定义中，所有以双下划线开始的名字都被翻译成前面加上单下划线和类名的形式
#Secretive._Secretive__inaccessible
s._Secretive__inaccessible()

#所以实际上还是能在类外访问这些私有方法,尽管不应该这么做
#简而言之，确保其他人不会访问对象的特性和方法和特性是不可能的，加双下划线相当于起到一个标志的作用

#如果不需要使用这种方法但是又想让其他对象不要访问内部数据，那么可以使用单下划线.
#这不过是个习惯，但的确有实际效果，例如，前面有下划线的名字都不会被带星号的import 语句
#(from module import *)导入.

#7.2.4 类的命名空间

#所有位于class语句中的代码都在特殊的命名空间中执行--类命名空间（class namespace)
#这个命名空间可由类内所有成员访问
#类的定义其实就是执行代码块,比如，在类的定义区并不只限定只能使用def语句:
class C:
    print('Class C begin define...')

c = C()

#在类作用域内定义了一个可供所有成员（实例）访问的变量members,用来计算类的成员数量.

class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1#如果是用类命MemberCounter来对特性进行赋值，则它属于类作用域，若是self，则是对象作用域
m1 = MemberCounter()
m1.init()

print(MemberCounter.members)

print(m1.members)

m2 = MemberCounter()
m2.init()

print(MemberCounter.members)

#在实例中重新绑定members 特性
#新numbers值被写到m1的特性中，屏蔽了类范围内的变量，但并不影响真正的类变量
m1.members = 'Two'
print(m1.members)
print(m2.members)

#7.2.5 指定超类

#子类可以扩展超类的定义,将其他类命写在class语句后的圆括号内可以指定超类:

class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter): #SPAMFilter 是Filter的子类
    def init(self): #重写Filter超类中的init方法
        self.blocked = ['SPAM']

#Filter 是个用于过滤序列的通用类，事实上它不能过滤任何东西

f = Filter()
f.init()
result = f.filter([1,2,3])
print(result)

s = SPAMFilter()
s.init()
result = s.filter(['SPAM','SPAM','SPAM','SPAM','eggs','bacon','SPAM'])

print(result)

#SPAMFilter 定义的两个要点
#这里用提供新定义的方式重写了Filter的init定义
#filter 方法的定义是从Filter类中拿过来（继承）的，所以不用重写它的定义

#7.2.6 检查继承

#使用issubclass函数检查一个类是否是另一个类的子类
result = issubclass(SPAMFilter,Filter)
print(result)

result = issubclass(Filter,SPAMFilter)
print(result)

#通过特殊特性__bases__，查看已知类的基类
baseResult = SPAMFilter.__bases__

print(baseResult)

#使用isinstance方法检查一个对象是否是一个类的实例:
s = SPAMFilter()
result = isinstance(s,SPAMFilter)
print(result)
result = isinstance(s,Filter)
print(result)

result = isinstance(s,str)
print(result)
#如果只想知道一个对象属于哪个类，可以使用__class__特性:
result = s.__class__
print(result)
#如果使用__metaclass__=type 或从object继承的方式来定义新式类，那么可以使用type(s)查看实例所属的类

result = type(s)
print(result)
#可见在python3.0可以直接使用type(s)

#7.2.7 多个超类

class Calculator:
    def calculate(self,expression):
        self.value = eval(expression)
    def talk(self,param):
        print('Calculator talk:',self.value,param)
class Talker:
    def talk(self):
        print('Hi,my value is ',self.value)
#tTest = Talker()
#tTest.talk() 提示value属性不存在

class TalkingCalculator(Calculator,Talker):
    pass
#居然还能这样组合。。
tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk(32)

#python支持多重继承，这点与java单继承就大不同了
#这种行为称为多重继承(multiple inheritance)

#当使用多重继承时，有个需要注意的地方，如果一个方法从多个超类继承(也就是你有两个具有相同名字的不同方法)
#那么必须要注意一下超类的顺序,先继承的类中的方法会重写后继承的类中的方法,
#不存在java的重载行为，即使参数不同，仍然会覆盖

#7.2.8

#“接口”的概念与多态有关，在处理多态对象时，只要关心它的接口（或称协议）即可，也就是公开的方法和特性.

#在Python中，不用显式地指定对象必须包含哪些方法才能作为参数接收
#例如，不用(像在java中一样)显示地编写接口,可以在使用对象的时候假定它可以实现你所要求的行为
#如果它不能实现的话，程序就会失败

#检查方法是否已存在

result = hasattr(tc,'talk')
print(result)

result = hasattr(tc,'fnord')
print(result)

result = hasattr(getattr(tc,'talk',None),'__call__')
print('方法是否可调用:' + str(result))
result = hasattr(getattr(tc,'fnord',None),'__call__')

print('方法是否可调用:' + str(result))

result = callable(getattr(tc,'talk',None))
print('方法是否可调用:' + str(result))
result = callable(getattr(tc,'fnord',None))
print('方法是否可调用:' + str(result))

#setattr ,可以用来设置对象的特性:
setattr(tc,'name','Mr.Gumby')
print(tc.name)

#查看对象所存储的值
result = tc.__dict__
print(result)
#查看对象是由什么组成的,可以查看inspect模块

