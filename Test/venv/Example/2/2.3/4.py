#高级排序
#内建函数cmp
cmpTest = cmp(42,32)
print(cmpTest)
cmpTest1 = cmp(99,100)
print(cmpTest1)
cmpTest2 = cmp(10,10)
print(cmpTest2)
numbers = [5,2,9,7]
numbers.sort(cmp)
print(numbers)
#sort方法可选参数   key和reverse(关键字参数)
#参数key与参数cmp类似,必须提供一个在排序过程中使用的函数,
#然而该函数并不是直接用来确定对象的大小，而是为每个元素创建一个键，
#然后所有元素根据键来排序,因此,如果要根据元素的长度进行排序,那么可以使用len作为键函数
x = ['aardvark','abalone','acme','add','aerate']
x.sort(key=len)
print(x)

#另一个关键字参数reverse是简单的布尔值(True或者False)，用来指明列表是否要进行反向排序
x = [4,6,2,1,7,9]
x.sort(reverse=True)
print(x)

