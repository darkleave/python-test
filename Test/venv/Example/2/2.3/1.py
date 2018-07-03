#因为字符串不能像列表一样被修改,所以有时根据字符串创建列表会很有用,list函数可以实现这个操作

listTest = list('Hello')
print(listTest)

strTest = '$'.join(listTest)
print(strTest)