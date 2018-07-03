#9.6 迭代器

#__iter__方法是迭代器规则的基础

#9.6.1 迭代器规则

#只要对象实现了__iter__方法就能进行迭代

#__iter__方法会返回一个迭代器,所谓的迭代器就是具有next方法(这个方法在调用时不需要任何参数)的对象
#在调用next方法时，迭代器会返回它的下一个值,如果next方法被调用，但迭代器没有值可以返回,
#就会引发一个StopIteration异常.

#python 3.0 迭代器对象应该实现__next__方法，而不是next.
#而新的内建函数next可以用于访问这个方法，换句话说，next(it)等同于3.0之前版本中的it.next().

#使用迭代器而不使用列表的理由，列表一次性获取所有值，会占用更多的内存，
#同时，使用迭代器更通用，更简单，更优雅

#一个实现了__iter__方法的对象时可迭代的，一个实现了next方法的对象则是迭代器

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        return self.a
    def __iter__(self):
        return self


fibs = Fibs()

for f in fibs:
    print(f)
    if f > 1000:
        break

class TestIterator:
     value = 0
     def __next__(self):
         self.value += 1
         if self.value > 20 : raise StopIteration
         return self.value
     def __iter__(self):
         return self

ti = TestIterator()
listTest = list(ti)

print(listTest)


#9.7 生成器
#生成器也叫简单生成器,生成器是一种用普通的函数语法定义的迭代器,可以帮助读者写出非常优雅的代码.
#任何包含yield语句的函数称为生成器,它的行为和普通的函数也有很大的差别
#它不通过return那样返回值,而是每次产生多个值,每次产生一个值(使用yield语句),函数就会被冻结:
#即函数停在那点等待被重新唤醒,函数被重新唤醒后就从停止的那点开始执行.

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1,2],[3,4],[5]]

for num in flatten(nested):
    print(num)

listTest = list(flatten(nested))
print(listTest)

#9.7.2 递归生成器

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

listTest = list(flatten([[[1],2],3,4,[5,[6,7]],8]))

print(listTest)

#对字符串进行递归会导致无穷递归，因为一个字符串的第一个元素是另一个长度为1的字符串,
#而长度为1的字符串的第一个元素就是字符串本身
#listTest = list(flatten('abcde'))

#添加字符串类型检查

def flatten(nested):
    try:
        #不要迭代类似字符串的对象:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

listTest = list(flatten(['foo',['bar',['baz']]]))
print(listTest)

#9.7.3 通用生成器

#生成器总结
#生成器是一个包含yield关键字的函数,当它被调用时,在函数体中的代码不会被执行,而会返回一个迭代器,
#每次请求一个值，就是执行生成器中的代码,直到遇到一个yield或者return语句,
#yield语句意味着应该生成一个值,return 语句意味着生成器要停止执行(不在生成任何东西，
#return 语句只有在一个生成器中使用时才能进行无参数调用).

#生成器的组成:生成器的函数和生成器的迭代器

def simple_generator():
    yield 1
print(simple_generator)

print(simple_generator())

#9.7.4 生成器方法

#外部作用域访问生成器的send方法,就像访问next方法一样,只不过前者使用一个参数(要发送的“消息"——任意对象)
#在内部则挂起生成器,yield现在作为表达式而不是语句使用,换句话说,当生成器重新运行的时候,yield方法返回一个值,
#也就是外部通过send方法发送的值,如果next方法被使用，那么yield方法返回None.

#throw 方法（使用异常类型调用，还有可选的值以及回溯对象)用于在生成器内引发一个异常(在yield表达式中)
#close方法(调用时不用参数)用于停止生成器


def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new

r = repeater(42)
print(r.__next__())
print(r.__next__())
sendTest = r.send("Hello,World!")

print(sendTest)
print(r.__next__())


#9.7.5 模拟生成器

def flatten(nexted):
    result = []
    try:
        #不要迭代类似字符串的对象:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result

#八皇后问题

#有一个棋盘和8个要放到上面的皇后，唯一的要求是皇后之间不能形成危胁

#9.8.4 寻找冲突

def conflict(state,nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False

#基本情况

def queens(num,state):
    if len(state) == num-1:
        for pos in range(num):
            if not conflict(state,pos):
                yield pos

#9.8.6 需要递归的情况

def queens(num=8,state=()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state) == num-1:
                yield(pos,)
            else:
                for result in queens(num,state + (pos,)):
                    yield (pos,) + result

#9.8.7 打包

def prettyprint(solution):
    def line(pos,length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))

import random
prettyprint(random.choice(list(queens(8))))