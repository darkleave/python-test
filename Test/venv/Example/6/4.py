#函数式编程

#map,filter 和reduce函数,(Python 3.0中这些都被移至functools模块中)

#用map函数将序列中的元素全部传递 给一个函数
result = map(str,range(10)) #Equivalent to [str(i) for i in range(10)]
print(result)
#filter函数可以基于一个返回布尔值的函数对元素进行过滤.

def func(x):
    return x.isalnum()

seq = ['foo','x41','?!','***']
result = filter(func,seq)

print(seq)
print(result)

#使用列表推导式
result = [x for x in seq if x.isalnum()]
print(result)




