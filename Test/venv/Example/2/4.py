#步长示例
#步长通常都是隐式设置的,默认步长为1,分片操作就是按照这个步长逐个遍历序列的元素,然后返回开始和
#结束点之间的所有元素
numbers = [1,2,3,4,5,6,7,8,9,10]
num1 = numbers[0:10:2]
print(num1)
num2 = numbers[3:6:3]
print(num2)
num3 = numbers[::4]
print(num3)
num4 = numbers[8:3:-1]
print(num4)
num5 = numbers[10:0:-2]
print(num5)
num6 = numbers[0:10:-2]
print(num6)
num7 = numbers[::-2]
print(num7)
num8 = numbers[5::-2]
print(num8)
num9 = numbers[:5:-2]
print(num9)