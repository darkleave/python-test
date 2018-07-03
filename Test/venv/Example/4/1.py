
#4.2 创建和使用字典
phoneCheck = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
#字典由多个键及其对应的值构成的键-值对组成(我们也把键值对称为项)

#4.2.1 dict函数
#可以用dict函数通过其他映射(比如其他字典)或者(键,值)对的序列建立字典

items = [('name','Gumby'),('age',42)]
d = dict(items)
print(d)
print(d['name'])

d = dict(name='Gumby',age=42)
print(d)
