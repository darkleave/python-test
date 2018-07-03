#6.6递归

#递归的定义(包括递归函数定义)包括它们自身定义内容的引用.
'''
def recursion():
    return recursion()
#recursion()
'''
#每次调用函数都会用掉一点内存,在足够的函数调用发生后，空间就不够了,
#程序会以一个“超过最大递归深度"的错误信息结束.
#这类递归被称为”无穷递归“


#一般的递归函数一般包含两个特性
#当函数直接返回值时有基本实例（最小可能性问题）
#递归实例，包括一个或者多个问题较小部分的递归调用

#6.6.1 两个经典：阶乘和幂

#将n个人排成一行

def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

test = factorial(10);
print(test)

#递归版本

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#计算幂
def power(x,n):
    result = 1
    for i in range(n):
        print('i:' + str(i))
        result *= x
    return result

#递归版本

print(power(2,0))

def power2(x,n):
    if n == 0:
        return 1
    else:
        return x * power2(x,n-1)

result = power2(2,0)

print(result)

#递归在大多数情况下可以用循环代替,递归的优点在于 递归更多易读，有时会大大提高可读性.

#6.6.2 二分法查找

#这个算法的本身就是递归的定义，亦可用递归实现

#如果上下限相同,那么就是数字所在位置，返回.
#否则找到两者的中点（上下限的平均值），查找数字是在左侧还是右侧,继续查找数字所在的那半部分.

#二分法查找实现

def search(sequence,number,lower,upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,middle)

seq = [34,67,8,123,4,100,95]
seq.sort()
print(seq)
result = search(seq,34,1,7)
print(result)
result = search(seq,100,1,7)
print(result)




