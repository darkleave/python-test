#元组:不可变序列
#元组与列表一样,也是一种序列,唯一的不同是元组不能修改
#元组创建语法,如果你用逗号分隔了一些值,那么你就自动创建了元组
metaArrayTest = 1,2,3
#元组大部分时候是通过圆括号括起来的
print(metaArrayTest)
#空元组可以使用没有包含内容的两个圆括号来表示
metaArrayTest1 = ()
#实现包括一个值的元组,实现方法：必须加个逗号,即使只有一个值
metaArrayTest2 = 42,
print(metaArrayTest2)
metaArrayTest3 = (42,)
print(metaArrayTest3)
#metaArrayTest4 = (42)  即使是用括号括起来也必须加逗号
#print(metaArrayTest4)
wrongMetaArray = 3 * (40+2)
print(wrongMetaArray)
metaArrayTest5 = 3 * (40+2,)
print(metaArrayTest5)

#tuple函数
#tuple函数的功能与list函数基本上是一样的:以一个序列作为参数并把它转换为元组
#如果参数就是元组,那么该参数就会被原样返回
tupleTest = tuple([1,2,3])
print(tupleTest)
tupleTest1 = tuple('abc')
print(tupleTest1)
tupleTest2 = tuple((1,2,3,))
print(tupleTest2)

#基本元组操作:创建元组以及访问元组元素
x = 1,2,3
print(x[1])
#元组的分片还是元组，就像列表的分片还是列表一样
metaTag = x[0:2]
print(metaTag)




