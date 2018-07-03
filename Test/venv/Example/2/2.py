numbers = [1,2,3,4,5,6,7,8,9,10]
num1 = numbers[3:6]
print(num1)
num2 = numbers[0:1]
print(num2)
num3 = numbers[7:10]
print(num3)
num4 = numbers[-3:-1]
print(num4)
#使用0作为结尾索引无法取到想要的结果字符串
num5 = numbers[-3:0]
print(num5)
#如果分片所得部分包括序列结尾的元素,只需置空最后一个索引即可
num6 = numbers[-3:]
print(num6)
#这种方法同样适用于序列开始的元素
num7 = numbers[:3]
print(num7)
#如果要复制整个序列,可以将两个索引都置空
num8 = numbers[:]
print(num8)

