#5.2 赋值魔法

#5.2.1 序列解包

#多个赋值操作同时进行,也成为并行赋值
x,y,z = 1,2,3

print(x,y,z)
#交换两个或多个变量
x,y = y,x
print(x,y,z)

#事实上，这里所做的事情叫做序列解包(sequence unpacking)或递归解包--将多个值的序列解开，然后放到变量的序列中,比如

values = 1,2,3
print(values)
x,y,z = values
print(x)
#当函数或者方法返回元组(或者其他序列或可迭代对象)时，这个特性尤其有用,
#假设需要获取(和删除)字典中任意的键值对，可以使用popitem方法，这个方法将键值作为元组返回，
#那么这两个元组就可以直接赋值到两个变量中

scoundrel = {'name':'Robin','girlfriend':'Marion'}
key,value = scoundrel.popitem()
print(key)
print(value)

#序列中的元素数量必须和放置在赋值符号左边的变量数量完全一致，否则Python会在赋值时引发异常:
#x,y,z = 1,2

#python 3.0支持*号运算符,例如
a,b,*rest=[1,2,3,4]
print(rest)

#5.2.2 链式赋值
#链式赋值(chained assignment) 是将同一个值赋给多个变量的捷径,有些类似并行赋值，不过这里只处理一个值

#x = y = somefunciton()
#等同于
#y = somefunction()
#x = y
#如示例所示，可以直接将函数赋值给变量
from math import sqrt
x = y = sqrt
print(x(5))

#5.2.3 增量赋值

#这里没有将赋值表达式写为x = x + 1,而是将表达式运算符(本例中是+-)放置在赋值运算符=的左边，写成x+=1
#这种写法叫做增量赋值(augmented assignment),对于*,/,%等标准运算符都适用：
x = 2
x +=1
x *= 2
print(x)
#对于其他数据类型也适用（只要二元运算符本身适用于这些数据即可）：
fnord = 'foo'
fnord += 'bar'
fnord *= 2
print(fnord)

#增量赋值可以让代码更加紧凑和简练，很多情况下会更易读

#5.3 语句块：缩排的乐趣

#语句块是在条件为真(条件语句)时执行或者执行多次(循环语句)的一组语句,在代码前放置空格来缩进语句即可创建语句块

#使用tab字符也可以缩进语句块,python将一个tab字符解释为到下一个tab字符位置的移动，而一个tab字符位置为8个空格，
#但是标准且推荐的方式是只用空格，尤其是在每个缩进需要4个空格的时候

#块中的每行都应该缩进同样的量，下面的伪代码展示了缩进的工作方式
#this is a line
#this is aother line:
#   this is another block
#   continuing the same block
#   the last line of this block
#phew,there we escaped the inner block

#在Python中，冒号(:)用来标识语句块的开始，块中每一个语句都是缩进的（缩进量相同),
#当回退到和已经闭合的块一样的缩进量时，就表示当前块已经结束了



