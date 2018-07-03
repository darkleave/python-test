#4.2.2 基本字典操作

#字典的基本行为在很多方面与序列(sequence)类似:
#1. len(d)返回d中项(键-值对)的数量;
#2. d[k]返回关联到键k上的值;
#3. d[k]=v将值关联到键k上;
#4 del d[k]删除键味k的项;
#5. k in d检查d中是否有含有键为k的项

#键类型：字典的键不一定为整型数据(但也可以是),键可以是任意的不可变类型，比如浮点型(实型)，字符串或者元组

#自动添加:即使键起初在字典中并不存在，也可以为它赋值，这样字典就会建立新的项，而(在不使用append方法或者其他类似操作的情况下)
#不能将值关联到列表范围之外的索引上

#成员资格:表达式k in d(d为字典)查找的是键，而不是值，表达式v in l(l为列表)则用来查找值，而不是索引。

dicTest = {1:'xiaoming',2:'xiaohong',3:'xiaobai',4:'xiaoli'}
print(len(dicTest))
print(dicTest[1])
dicTest[1] = 'daming'
print(dicTest[1])
del dicTest[2]
print(dicTest)
if 1 in dicTest : print("hello,i'm here")

#自动添加例子，列表无法自动添加，字典在给不存在的key赋值时，会触发自动添加
x = []
#x[42] = 'Foobar' 报错，该列表索引不存在
x = {}
#该键不存在，自动进行添加
x[42] = 'Foobar'
print(x)

#示例

people = {

    'Alice':{
        'phone':'2341',
        'addr':'Foo drive 23'
    },
    'Beth':{
        'phone':'9102',
        'addr':'Bar street 42'
    },
    'Cecil':{
        'phone':'3158',
        'addr':'Baz avenue 90'
    }
}
#针对电话号码和地址使用的描述性标签,会在打印输出的时候用到
labels = {
    'phone':'phone number',
    'addr':'address'
}
name = input('Name: ')
#查找电话号码还是地址?
request = input('Phone number (p) or address (a)?')

#使用正确的键
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
#如果名字是字典中的有效键才打印信息:
if name in people:print("%s 's %s is %s." % \
                        (name,labels[key],people[name][key]))






