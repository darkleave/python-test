#序列相加,只有相同类型的序列才能进行链接操作
addList = [1,2,3] + [4,5,6]
print(addList)
addString = 'Hello, ' + 'world!'
print(addString)
#字符串和列表类型不同，无法进行链接
addListString = [1,2,3] + 'world!'
print(addListString)