#第九章 魔法方法，属性和迭代器

#在Python中有的名称会在前后加上两个下划线，比如__future__,这种拼写表示名字有特殊含义
#所以绝壁不要在自己的程序中使用这种名字.
#在Python中,由这些名字组成的集合所包含的方法称为魔法(或特殊）方法.如果对象实现了这些方法中的一个,
#那么这个方法会在特殊的情况下(确切地说是根据名字)被Python调用,而几乎没有直接调用它们的必要.

#9.1

#在Python3.0中没有“旧式”的类，也不需要显式地子类化object或者将元类设置为type.
#所有的类都会隐式地成为object地子类——如果没有明确超类地话，就会直接子类化；否则会间接子类化

#9.2 构造方法
'''

class FooBar:
    def __init__(self):
        self.somevar = 42

f = FooBar()
print(f.somevar)

'''
#构造方法添加参数

class FooBar:
    def __init__(self,value=42):
        self.somevar = value

f = FooBar()
print(f.somevar)

f = FooBar(30)
print(f.somevar)
f = FooBar('some test')
print(f.somevar)

#9.2.1 重写一般方法和特殊的构造方法

#每个类都可能拥有一个或者多个超类,它们从超类那里继承行为方式，
#如果一个方法在B类的一个实例中被调用(或一个属性被访问),但在B类中没有找到该方法,那么就会区它的超类A里面找

class A:
    def hello(self):
        print('Hello,i A')
class B(A):
    pass

a = A()
b = B()
a.hello()
b.hello()

#B类重写hello方法

class B(A):
    def hello(self):
        print('hello,i B')

b = B()
b.hello()

#子类调用超类构造方法

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry=False
        else:
            print('No,thanks!')
b = Bird()
b.eat()
b.eat()

class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()

#没有正确初始化超类属性
#sb.eat()

#9.2.2 调用未绑定的超类构造方法


class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

print('right SongBird')
sb = SongBird()
sb.eat()

sb.eat()

#在调用一个实例的方法时，该方法的self参数会被自动绑定到实例上(这称为绑定方法)
#如果直接调用类的方法(Bird.__init__),那么就没有实例会被绑定,这样就可以自由地提供需要的self参数,
#这样的方法称为未绑定(unbound)方法

#通过将当前的实例作为self参数提供给未绑定方法,SongBird就能够使用其超类构造方法的所有实现，也就是属性hungry被设置
#相当于Bird.__init__(sb);sb.hungry=True

#9.2.3 使用super函数

#super 函数只能在新式类中使用

#当前的类和对象可以作为super函数的参数使用,调用函数返回的对象的任何方法都是调用超类的方法，而不是当前类的方法.
#例: super(SongBird,self)
#在Python3.0中，super函数可以不带任何参数进行调用,super()

class SongBird(Bird):
    def __init__(self):
        #super().__init__()
        super(SongBird,self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()

#super 函数非常智能，即使类已经继承多个超类，也只需要使用一次super函数，
#但要确保所有的超类的构造方法都使用了super函数
#super函数实际上返回一个super对象，这个对象负责进行方法解析，当对其特性进行访问时，
#它会查找所有的超类（以及超类的超类),直到找到所需的特性为止(或者引发一个AttributeError异常)

