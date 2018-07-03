#模板字符串
from string import Template
s = Template('$x,glorious $x!')
templateTest = s.substitute(x='slurm')
print(templateTest)

s = Template("It's ${x}tastic!")
templateTest1 = s.substitute(x='slurm')
print(templateTest1)


s = Template("Make $$ selling $x!")
templateTest2 = s.substitute(x='slurm')
print(templateTest2)

#使用字段变量提供值/名称对
s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
templateTest3 = s.substitute(d)
print(templateTest3)




