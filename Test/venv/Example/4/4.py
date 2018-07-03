#4.2.4 字典方法
#1. clear
#clear 方法清除字典中所有的项,这是个原地操作(类似于list.sort),所以无返回值(或者说返回None).

d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)
returned_value = d.clear()
print(returned_value)

#clear 方法的用途，两种情况
x = {}
y = x
x['key'] = 'value'
print(y)
x = {}
print(y)
#第二种情况
x = {}
y = x
x['key'] = 'value'
print(y)
x.clear()
print(y)
#两种情况中,x和y最初对应同一个字典,
#第一种情况,由于x和y都是引用变量，都是指向“实际内容”的指针，x清空并不影响y继续指向原先的内容
#第二种情况，x调用clear方法的情况下，可以看到y也同样被清空了，说明clear方法会影响到所有指向该内容的引用变量

#copy
#copy 方法返回一个具有相同键值对的新字典(这个方法实现的是浅复制(shallow copy),因为值本身就是相同的，而不是副本)
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x)
#可以看到，当在副本替换值的时候，原始字典不受影响，但是，如果修改了某个值(原地修改，而不是替换),原始的字典也会改变
#因为同样的值也存储在原字典中
#避免这个问题的一种方法就是使用深复制(deep copoy),复制其包含的所有值，可以使用copy模块的deepcode函数来完成操作:
from copy import deepcopy
d = {}
d['names'] = ['Alfred','Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)

#fromkeys
#fromkeys方法使用给定的键建立新的字典,每个键都对应一个默认的值None
{}.fromkeys(['name','age'])
#上述例子首先构造了一个空字典，然后调用fromkeys方法，建立另外一个词典，
#还可以直接在dict上面调用该方法，dict是所有字典的类型
dicTest = dict.fromkeys(['name','age'])
print(dicTest)

#get
#get方法是个更宽松的访问字典项的方法，一般来说，如果试图访问字典中不存在的项时会出错
d = {}
#print(d['name'])  报错
#而用get就不会
print(d.get('name'))

#当使用get访问一个不存在的键时，没有任何异常，而得到了None值，还可以自定义默认值，替换None:
getTest = d.get('name','N/A')
print(getTest)
#如果键存在，get用起来就像普通的字典查询一样
d['name'] = 'Eric'
getTest = d.get('name')
print(getTest)



