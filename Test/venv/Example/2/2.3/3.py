#列表方法
#append方法用于在列表末尾追加新的对象
lst = [1,2,3]
lst.append(4)
print(lst)
#count方法用于统计某个元素在列表中出现的次数
countTest = ['to','be','or','not','to','be'].count('to')
print(countTest)
x = [[1,2],1,1,[2,1,[1,2]]]
countTest1 = x.count(1)
countTest2 = x.count([1,2])
print(countTest1)
print(countTest2)
#extend方法可以在列表的末尾一次性追加另一个序列中的多个值，换句话说，可以用新列表扩张原有的列表
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
#这个操作看起来很像链接操作，两者的主要区别在于：extend方法修改了被扩张的序列(在这个例子中就是a)
#而原始的链接则不然，它会返回一个全新的列表:
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
print(a)
#原始的链接操作创建了一个包含a和b副本的新列表,因此，一般情况下链接操作的效率会比extend方法低

#可以使用分片赋值来实现相同的结果

a = [1,2,3]
b = [4,5,6]
a[len(a):] = b
print(a)

#index方法,index方法用于从列表中找出某个值第一个匹配项的索引位置

knights = ['We','are','the','knights','who','say','ni']
indexTest = knights.index('who')
print(indexTest)
#找不到对应索引时抛出异常
#knights.index('herring')

#insert
#insert方法用于将对象插入到列表中
numbers = [1,2,3,4,5,6,7]
numbers.insert(3,'four')
print(numbers)
#与extend方法一样,insert方法的操作也可以用分片赋值来实现
numbers = [1,2,3,4,5,6,7]
numbers[3:3] = ['four']
print(numbers)

#pop
#pop方法会移除列表中的一个元素(默认是最后一个),并且返回该元素的值
#tip:pop方法是唯一一个既能修改列表又返回元素值(除了None)的列表方法
#使用pop方法可以实现一种常见的数据结构--栈，使用pop方法和append方法来实现出栈和入栈的操作
x = [1,2,3]
popTest = x.pop()
print(popTest)
print(x)
popTest1 = x.pop();
print(popTest1)
print(x)

#remove
#remove方法用于移除列表中某个值的第一个匹配项
x = ['to','be','or','not','to','be']
x.remove('be')
print(x)
#移除元素找不到的情况下抛出异常
#x.remove('bee')
#remove是一个没有返回值的原位置改变方法,它修改了列表却没有返回值,这与pop方法相反

#reverse
#reverse方法将列表中的元素反向存放
x = [1,2,3]
x.reverse()
print(x)

#sort
#sort方法用于在原位置对列表进行排序,在"原位置排序"意味着改变原来的列表,从而让其中的元素能按一定的顺序排序，
#而不是简单的返回一个已排序的列表副本
x = [4,6,2,1,7,9]
x.sort()
print(x)

#当用户需要一个排好序的列表副本，同时又保留原有列表不变的时候

x = [4,6,2,1,7,9]
y = x[:]
y.sort()
print(x)
print(y)
#列表类似java的引用变量,如果直接如下将x赋值给y,会让x和y都指向同一个列表
y=x
y.sort()
print(x)
print(y)
#另一种获取已排序的列表副本的方法,使用sorted函数
x = [4,6,2,1,7,9]
y = sorted(x)
print(x)
print(y)
#sorted函数实际上可以作用于任何序列,却总是返回i一个列表
sortedTest = sorted('Python')
print(sortedTest)

