#10.3.4 集合，堆和双端队列

#Python 支持一些相对通用的数据结构类型,例如字典(或者说散列表),列表(或者说动态数组)

#1. 集合 (Set)

setTest = set(range(10))

print(setTest)

#集合是由序列(或者其他可迭代的对象)构建的,主要用于检查成员资格,因此副本是被忽略的，即不允许重复元素

setTest = set([0,1,2,3,0,1,2,3,4,5])

print(setTest)

#和字典一样，集合元素的顺序是随意的，因此我们不应该以元素的顺序作为依据进行编程:
setTest = set(['fee','fie','foe'])
#注意顺序发生了变化
print(setTest)

#标准集合操作，并集交集等

#并集
#a | b 等同于 a.union(b)
a = set([1,2,3])
b = set([2,3,4])
print(a.union(b))

setTest = a | b
print(setTest)

#交集
#a & b 等同于 a.interesection(b)
c = a & b
cTest = c.issubset(a)
print(c)
print(cTest)

print(c <= a)
print(c.issuperset(a))
#同样是求交集
c = a.intersection(b)
print(c)

#不相交的部分

c = a.difference(b)
print(c)
c = a - b
print(c)
#求两个集合不相交的部分的并集 symmetric_difference 等同于 a ^ b

c = a.symmetric_difference(b)
print(c)
c = a ^ b
print(c)

#copy 副本仅仅是值相同
b = a.copy()
print(b)
isTest = a.copy() is a
print(isTest)


#集合是可变的,所以不能用作字典中的键,另外一个问题就是集合本身只能包含不可变(可散列)的值,
#所以也就不能包含其它集合
#实际应用中，集合的集合的情况，需要使用frozenset 类型，用于代表不可变(可散列)的集合:

a = set()
b = set()

#a.add(b)
a.add(frozenset(b))
print(a)

#frozenset 构造函数创建给定集合的副本，不管是将集合作为其它集合成员还是字典的键,frozenset都很有用.

#2. 堆
#另外一个众所周知的数据结构是堆(heap),它是优先队列的一种.
#Python 中并没有独立的堆类型，只有一个包含一些堆操作函数的模块，这个模块叫做heapq(q是queue的缩写,即队列)
#包括6个函数，其中前4个直接和堆操作相关,你必须将列表作为堆对象本身.

#heapq模块中重要的函数

#heappush(heap,x) 将x入堆
#heappop(heap) 将堆中最小的元素弹出
#heapify(heap) 将heap属性强制应用到任意一个列表
#heapreplace(heap,x) 将堆中最小的元素弹出，同时将x入堆
#nlargest(n,iter) 返回iter中第n大的元素
#nsmallest(n,iter) 返回iter中第n小的元素

from heapq import *
from random import shuffle
data = range(10)
print(data)
data = list(data)
shuffle(data)

heap = []
for n in data:
    heappush(heap,n)
print(heap)

heappush(heap,0.5)
print(heap)

#堆的规则
#位于i位置上的元素总比i/2 位置处的元素大(反过来说就是i位置处的元素总比2*i以及2*i+1位置处的元素小
#这是底层堆算法的基础，而这个特性称为堆属性(heap property)

i = heappop(heap)
print(i)
i = heappop(heap)
print(i)
i = heappop(heap)
print(i)

heap = [5,8,0,3,6,7,9,1,4,2]
heapify(heap)
print(heap)

heapreplace(heap,0.5)

print(heap)

heapreplace(heap,10)

print(heap)

#3. 双端队列(以及其它集合类型)
#双端队列(double-ended queue,或称deque) 在需要按照元素增加的顺序来移除元素时非常有用.

#双端队列通过可迭代对象(比如集合)创建

from collections import deque
q = deque(list(range(5)))

q.append(5)
q.appendleft(6)
print(q)

popElement = q.pop()
print(popElement)
print(q)

element = q.popleft()
print(element)

q.rotate(3)
print(q)
q.rotate(-1)
print(q)
q.rotate(0)
print(q)

#10.3.5 time
#time 模块所包括的函数能够实现以下功能:获得当前时间，操作时间和日期，
#从字符串读取时间以及格式化时间为字符串.

#日期可以用实数的秒数或者时包含有9个整数的元组
#比如
#(2008,1,21,12,2,56,0,21,0).
#表示2008年1月21日12时2分56秒，星期一，并且是当年的第21天(无夏令时).
#其中秒的范围为0-61,为了应付闰秒和双闰秒

import time
print(time.asctime())

#与时间密切相关的模块
#datetime(支持日期和时间的算法)
#timeit (帮助开发人员堆代码段的执行时间进行计时)

#10.3.6 random
#random 模块包括返回随机数的函数,可以用于模拟或者用于任何产生随机输出的程序

#random模块所产生的数字都是伪随机,如果需要真的随机性
#应该使用os模块的urandom或者random模块内的SystemRandom,可以让数据接近真正的随机性.

from random import *
from time import *
date1 = (2008,1,1,0,0,0,-1,-1,-1)
time1 = mktime(date1)
date2 = (2009,1,1,0,0,0,-1,-1,-1)
time2 = mktime(date2)

print(time1)
print(time2)
random_time = uniform(time1,time2)
print(asctime(localtime(random_time)))

'''
from random import randrange
num = input('How many dice?')
num = int(num)
sides = input('How many sides per die?')
sides = int(sides)
sum = 0
for i in range(num): sum += randrange(sides) + 1
print('The result is',sum)
'''

import fileinput,random

#通过openhook设置文件处理编码
fortues = list(fileinput.input('./1.py',openhook=fileinput.hook_encoded('UTF-8')))
print(random.choice(fortues))

#洗牌例子

from pprint import pprint
from random import shuffle

values = list(range(1,11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
print(values)
print(suits)
deck = ['%s of %s' % (v,s) for v in values for s in suits]
pprint(deck[:12])
pprint(deck)

#洗牌- -。。
shuffle(deck)
pprint(deck[:12])

#拿牌
#while deck: input(deck.pop())


