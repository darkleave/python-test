
#字符串方法

#find
#find方法可以在一个较长的字符串中查找子串,它返回子串所在位置的最左端索引,如果没有找到则返回-1
findTest1 = 'With a moo-moo here,and a moo-moo there'.find('moo')
print(findTest1)
title = "Monty Python's Flying Circus"
findTest2 = title.find('Monty')
findTest3 = title.find('Python')
print(findTest2)
print(findTest3)
findTest4 = title.find('Flying')
print(findTest4)
findTest5 = title.find('Zirquss')
print(findTest5)

subject = '$$$ Get rich now!!! $$$'
findTest6 = subject.find('$$$')
print(findTest6)
#这个方法还可以接收可选的起始点和结束点参数
subject = '$$$ Get rich now!!! $$$'
findTest7 = subject.find('$$$')
subject.find('$$$',1)#只提供起始点
subject.find('!!!')
subject.find('!!!',0,16)
print(subject)
#由起始和终止值指定的范围(第二个和第三个参事)包含第一个索引,但不包含第二个索引,这在python中是惯例

#join
#join方法是split方法的逆方法,用来连接序列中的元素,序列至少要有两个元素，只有一个元素的情况下返回本身
seq = [1,2,3,4,5]
sep = '+'
#sep.join(seq) #连接数字列表,报错,需要被连接的序列元素都必须是字符串
seq = ['1','2','3','4','5']
joinReturn = sep.join(seq) #连接字符串列表
print(joinReturn)
dirs = '','usr','bin','env'
print('/'.join(dirs))
print('C:' + '\\'.join(dirs))

test = 'a','b'
suffix = 'HHH'
returnS = suffix.join(test)
print('test:' + returnS)
onlyOne = 'a'
returnS = suffix.join(onlyOne)
print('now?:' + returnS)

#3.4.3 lower
#lower方法返回字符串的小写字符版
if 'Gumby' in ['gumby','simth','jones']: print('Found it!')
name = 'Gumby'
names = ['gumby','smith','jones']
if name.lower() in names: print('Found it!')

#3.4.4 replace
#replace方法 返回某字符串的所有匹配项均被替换之后得到字符串
replaceTest = 'This is a test'.replace('is','eez')
print(replaceTest)
#3.4.5 split
#split方法是join方法的逆方法,用来将字符串分割成序列
splitTest = '1+2+3+4+5'.split('+')
print(splitTest)
splitTest1 = '/usr/bin/env'.split('/')
print(splitTest1)
splitTest2 = 'Using the default'.split()
print(splitTest2)

#3.4.6 strip
#strip方法返回去除两侧(不包括内部)空格的字符串:
stripTest = '      internal whitespace is kept      '.strip()
print(stripTest)
names = ['gumby','smith','jones']
name = 'gumby '
if name in names: print('Found it!')
if name.strip() in names: print('Found it!')
#也可以指定需要去除的字符，将它们列为参数即可
stripTest = '*** SPAM * for * everyone!a!! ***'.strip(' *!')
print(stripTest)

#3.4.7 translate
#translate方法和replace方法一样,可以替换字符串中的某些部分,区别是
#translate方法只处理单个字符,它的优势在于可以同时进行多个替换，有些时候比replace效率高得多

#转换表
#from string import maketrans
table = str.maketrans('cs','kz')
print("lentable:" + str(len(table)))
#makeTest = table[97:123]
#print(makeTest)
#makeTest1 = str.maketrans('','')[97:123] #空转换包含一个普通的字母表
#print(makeTest1)
#创建转换表后可以将它用作translate方法的参数,进行字符串的转换
translateTest = 'this is an incrdible test'.translate(table)
print(translateTest)

#translate的第二个参数是可选的,这个参数用来指定需要删除的字符

translateTest1 = 'this is an incredible test'.translate(table,' ')
print(translateTest1)
