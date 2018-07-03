#5. has_key
#has_key 方法可以检查字典中是否含有特定的键，表达式d.has_key(k)相当于表达式k in d.
#使用哪个方式很大程度上取决于个人的喜好，python3.0不包括这个函数
'''
d={}
hasTest = d.has_key('name')
print(hasTest)
d['name'] = 'Eric'
hasTest = d.has_key('name')


'''

#6 items和iteritems
#items方法将字典所有的项以列表方式返回，列表中的每一项都表示为(键，值)的形式,,
#但是在项在返回时并没有遵循特定的次序
d = {'title':'Python Web Site','url':'http://www.python.org','spam':0}
itemTest = d.items()
print(itemTest)
#iteritems 方法的作用大致相同，但是会返回一个迭代器对象而不是列表 python3.0废弃
#it = d.iteritems()
#print(it)

#7. keys和iterkeys
#keys和iterkeys将字典中的键以列表形式返回,而iterkeys则返回针对键的迭代器

print(d.keys())

#print(d.iterkeys()) python3.0废弃

#8. pop
#pop方法用来获得对应于给定键的值，然后将这个键值对从字典中移除
d = {'x':1,'y':2}
popTest = d.pop('x')
print(popTest)
print(d)

#9. popitem
#popitem方法类似于list.pop,后者会弹出列表的最后一个元素，但不同的是，popitem弹出随机的项，
#因为字典并没有“最后的元素”或者其他有关顺序的概念
#若想一个接一个地移除并处理项，这个方法就非常有效了(因为不用首先获取键的列表)

d = {'url':'http://www.python.org','spam':0,'title':'Python Web Site'}
popTest = d.popitem()
print(popTest)
print(d)
#尽管popitem和列表的pop方法很类似，但字典中并没有与append等价的方法，因为字典是无序的，类似于append的
#方法是没有任何意义的

#10. setdefault
#setdefault方法在某种程度上类似于get方法，能够获得与给定键相关联的值，
#除此之外，setdefault还能在字典中不含有给定键的情况下设定相应的键值。
d = {}
defaultTest = d.setdefault('name','N/A')
print('defaultTest:' + str(defaultTest))
print(d)
d['name'] = 'Gumby'
defaultTest = d.setdefault('name','N/A')
print(defaultTest)
print(d)
#可以看到，当键不存在的时候，setdefault返回默认值并且相应地更新字典，如果键存在，
#就返回与其对应的值，但不改变字典，默认值是可选的，这点和get一样，如果不设定，会默认使用none

d = {}
print(d.setdefault('name'))
print(d)

#11. update
#update方法可以利用一个字典项更新另外一个字典
#提供的字典中的项会被添加到旧的字典中，若有相同的键则会进行覆盖
d = {
    'title':'Python Web Site',
    'url':'http://www.python.org',
    'changed':'Mar 14 22:09:15 MET 2008'

}
x = {'title':'Python Language Website','a':'aaaa'}
updateTest = d.update(x)
print('updateTest:' + str(updateTest))
print(d)

#12. values和itervalues

#values方法以列表的形式返回字典中的值(itervalues返回值的迭代器)
#与返回键的列表不同的是，返回值的列表中可以包含重复的元素
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
print(d.values())

