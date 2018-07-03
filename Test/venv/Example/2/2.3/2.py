#基本的列表操作

#改变列表，元素赋值
x = [1,1,1]
x[1] = 2
print(x)

#删除元素

names = ['Alice','Beth','Cecil','Dee-Dee','Earl']
del names[2]
print(names)

#分片赋值
name = list('Perl')
print(name)
#分片赋值超出的列表将自动进行扩充
name[2:] = list('ar')
print(name)
name = list('Perl')
name[1:] = list('ython')
print(name)
numbers = [1,5]
#分片赋值语句可以在不需要替换任何原有元素的情况下插入新的元素
numbers = [1,5]
numbers[1:1] = [2,3,4]
print(numbers)
numbers[1:4] = []
print(numbers)


