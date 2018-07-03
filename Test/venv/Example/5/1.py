#5.1 print 和 import的更多信息

#print打印多个表达式,输出的每个参数之间都插入了一个空格符

print('Age:',42)

#同时输出文本和变量值

name = 'Gumby'
salutation = 'Mr.'
greeting = 'Hello,'
print(greeting,salutation,name)

#如果在结尾处加上逗号，那么接下来的语句会与前一条语句在同一行打印，例如:

print('Hello,',
      'world!')

#5.1.2 把某件事作为另一件事导入
#从模块导入函数的时候，通常可以使用 import somemodule 或者 from somemodule import somefunction
#或者 from somemodule import somefunction,anotherfunction,yetanotherfunction 或者 from somemodule import *
#如果两个模块都有open函数，只需要使用第一种方式导入,然后像下面这样使用函数:
#module1.open(...)
#module2.open(...)

#或者，在语句末尾增加一个as子句，在该子句后给出想要使用的别名
#例如为整个模块提供别名
import math as foobar
print(foobar.sqrt(4))
#或者为函数提供别名
from math import sqrt as foobar
print(foobar(4))
#对于open函数，可以像下面这样使用:
#from module1 import open as open1
#from module2 import open as open2


