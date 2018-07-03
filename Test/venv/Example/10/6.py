#10.3.8 re模块
#re 模块包含对正则表达式(regular expression)的支持.

#正则表达式是可以匹配文本片段的模式.

#通配符
# . 点号可以匹配“任何字符串”（除换行符之外的任意字符),因此点号就称为通配符(wildcard)
# 对特殊字符进行转义
#例: 'python\\.org' 或者使用原始字符串 r'python\.org'

#字符集
#[a-z] [^abc]

#选择符和子模式
#python|perl  'p(ython|erl)'

#可选项和重复子模式

#r'(http://)?(www\.)?python\.org'

#限制子模式出现次数的运算符:
#? 0次或1次
#* 0次或多次
#+ 1次或多次
#{m,n}  m-n次

#re 模块的内容

#compile(pattern[,flags]) 根据包含正则表达式的字符串创建模式对象
#search(pattern,string[,flags]) 在字符串中寻找模式
#match(pattern,string[,flags]) 在字符串开始处匹配模式
#split(pattern,string[,maxsplit=0]) 根据模式的匹配项来分割字符串
#findall(pattern,string) 列出字符串中模式的所有匹配项
#sub(pat,repl,string[,count=0]) 将字符串中所有pat的匹配项用repl替换
#escape(string) 将字符串中所有特殊正则表达式转义

import re

some_text = 'alpha,beta,,,,gamma delta'
splitTest = re.split('[,]+',some_text)

print(splitTest)
splitTest = re.split('[,]',some_text,maxsplit=2)
print(splitTest)
splitTest = re.split('[,]',some_text,maxsplit=1)
print(splitTest)

#re.findall 以列表形式返回给定模式的所有匹配项
pat = '[a-zA-Z]+'
text = '"Hmm .. Err -- are you sure?" he said, souding insecure.'
finadallTest = re.findall(pat,text)

print(finadallTest)

#查找标点符号
pat = r'[.?\-",]+'
findAllTest = re.findall(pat,text)
print(findAllTest)

#横线- 被转义了，所以Python不会将其解释为字符范围的一部分.比如[a-z]

#函数re.sub的作用在于：使用给定的替换内容将匹配模式的字符串(最左端并且非重叠的子字符串)替换掉.

pat = '{name}'
text = 'Dear {name}...'
text = re.sub(pat,'Mr. Gumby',text)

print(text)

#re.escape 函数可以对字符串中所有可能被解释为正则运算符的字符进行转义的应用函数

a = re.escape('www.python.org')
print(a)
a = re.escape('But where is the ambiguity?')
print(a)

#匹配对象和组
#对于re模块中那些能够对字符串进行模式匹配的函数而言，当能找到匹配项的时候，它们都会返回
#MatchObject匹配对象
#组就是放置在圆括号内的子模式
#例: There (was a (wee) (cooper)) who (lived in Fyfe)'
#0 There was a wee cooper who lived in Fyfe
#1 was a wee cooper
#2 wee
#3 cooper
#4 lived in Fyfe

m = re.match(r'www\.(.*)\..{3}','www.python.org')
#获取给定组的匹配项
test = m.group(1)
print(test)
#返回给定组的匹配项的开始位置
test = m.start(1)
print(test)
#返回给定组的匹配项的结束位置
test = m.end(1)
print(test)
#返回一个组的开始和结束位置
test = m.span(1)
print(test)

emphasis_pattern = r'\*([^\*]+)\*'
subTest = re.sub(emphasis_pattern,r'<em>\1</em>','Hello ,*world*!')

print(subTest)

#模板系统示例



