#5.5 循环

#5.5.1 while 循环

x = 1
while x <= 100:
    print(x)
    x +=1
'''
name = ''
while not name or name.isspace():
    name=input('Please enter your name:')
print('Hello,%s!' % name)
'''
#5.5.2 for 循环

words = ['this','is','an','ex','parrot']
for word in words:
    print(word)

numbers = [0,1,2,3,4,5,6,7,8,9]
for number in numbers:
    print(number)

#range函数的工作方式类似于分片，它包含下限（本例中为0），但不包含上限
#如果希望下限为0，可以只提供上限
rangeTest = range(0,10)
print(rangeTest)
rangeTest = range(10)
print(rangeTest)

for number in range(1,101):
    print(number)

#5.5.3 循环遍历字典元素

d={'x':1,'y':2,'z':3}
for key1 in d:
    print(key1,'corresponds to',d[key1])

for key,value in d.items():
    print(key,'corresponds to',value)

#5.5.4 一些迭代工具

#1.并行迭代

names = ['anne','beth','george','damon']
ages = [12,45,32,102]

for i in range(len(names)):
    print(names[i],'is','ages[i]','years old')

#内建的zip函数可以用来进行并行迭代，可以把两个序列“压缩”在一起，然后返回一个元组的列表

zipTest = zip(names,ages)
print(zipTest)

for name,age in zip(names,ages):
    print(name,'is',age,'years old')

#zip函数可以作用于任意多的序列
#zip可以处理不等长的序列，当最短的序列“用完”的时候就会停止：
zipTest = zip(range(5),range(100000000))

print('zipTest:' + str(zipTest))

for num1,num2 in zipTest:
    print(num1,',',num2)

#2 按索引进行迭代
#粗糙方案1
strings = ['test']

for string in strings:
    if 'xxx' in string:
        index = strings.index(string) #Search for the string in the list of strings
        strings[index] = '[censored]'

#粗糙方案2


index = 0
for string in strings:
    if 'xxx' in string:
        strings[index] = '[censored]'
    index+=1

#正确方案3 使用内建的enumerate 函数,这个函数可以在提供索引的地方迭代索引-值对

for index,string in enumerate(strings):
    if 'xxx' in string:
        strings[index] = '[censored]'

#3. 翻转和排序迭代
#reversed和sorted,它们同列表的reverse和sort(sorted和sort使用同样的参数)方法类似，但作用于任何序列
#或可迭代对象上，不是原地修改对象，而是返回翻转或排序后的版本
sortedTest = sorted([4,3,6,8,3])

print(sortedTest)

sortedTest = sorted('Hello,;world!')

print(sortedTest)

reversedTest = reversed('Hello,world!');

print(reversedTest)

listTest = list(reversed('Hello,world!'))

print(listTest)

joinTest = ''.join(reversed('Hello,world!'))
print(joinTest)

#虽然sorted方法返回列表，reversed方法却返回一个更加不可思议的可迭代对象
#如果想要对它进行索引，分片以及调用list方法，可以使用list函数转换返回的对象

#5.5.5 跳出循环

#1.break
#结束(跳出)循环可以使用break语句，假设需要寻找100以内的最大平方数，那么程序可以从100往下迭代到0
#当找到一个平方数时就不需要继续循环了，所以可以跳出循环:
from math import sqrt
for n in range(99,0,-1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

#2 continue
#continue 语句比break语句用得要少得多，它会让当前的迭代结束，“跳”到下一轮的循环开始，
#它最基本的意思是“跳过剩余的循环体，但是不结束循环”

'''
for x in seq:
    if condition1:continue
    if condition2:continue
    if condition3:continue
    
    do_something()
    do_something_else()
    do_another_thing()
    etc()
'''

#3 while True/break 语句

'''


word = 'dummy'
while word:
    word = input('Please enter a word:')
    #处理word:
    if word:
        print('The word was ' + word)
    else:
        print('no word!')

#避免使用哑值

word = input('Please enter a word: ')
while word:
    #处理word:
    print('The word was ' + word)
    word = input('Please enter a word: ')


#避免一样的赋值语句在两个地方进行两次调用

while True:
    word = input('Please enter a word:')
    if not word:break
    #处理 word:
    print('The word was ' + word)

'''

#while True的部分实现了一个永远不会自己停止的循环，但是在循环内部的if语句中加入语句可以的
#在条件满足时调用break语句，这样一来就可以在循环内部任何地方而不是只在开头(像普通的while循环一样)终止循环.
#if/break语句自然地将循环分为两部分：第一部分负责初始化(在普通的while循环中，这部分需要重复),
#第2部分则在循环条件为真的情况下使用第1部分内初始化好的数据

#else 居然可以放在循环外！这是什么操作？
from math import sqrt
for n in range(99,81,-1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

else:
        print("Didn't find it !")

#5.6 列表推导式——轻量级循环

#列表推导式(list comprehension)是利用其他列表创建新列表(类似于数学术语中的集合推导式)的一种方法
#工作方式类似与for循环

comprehensionTest = [x*x for x in range(10)]
print(comprehensionTest)

#这个语句可以通过增加一个if部分添加到列表推导式中:
comprehensionTest = [x*x for x in range(10) if x % 3 == 0]
print(comprehensionTest)

#也可以增加更多for语句的部分:(从以下示例结果可以看出，这两个循环并非并列的，而是类似嵌套循环)
comprehensionTest = [(x,y) for x in range(3) for y in range(3)]
print(comprehensionTest)

#作为对比，下面的代码使用两个for语句创建了相同的列表：
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

#也可以和if子句联合使用
girls = ['alice','bernice','clarice']
boys = ['chris','arnold','bob']
comprehensionTest = [b+'+'+g for b in boys for g in girls if b[0] == g[0]]
print(comprehensionTest)

#更高效率的方式

girls = ['alice','bernice','clarice']
boys = ['chris','arnold','bob']

letterGirlds = {}
for girl in girls:
    defaultTest = letterGirlds.setdefault(girl[0],[])
    print(defaultTest)
    defaultTest.append(girl)
    print(defaultTest)
print(letterGirlds)
print([b +'+'+g for b in boys for g in letterGirlds[b[0]]])
