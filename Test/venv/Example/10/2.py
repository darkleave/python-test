#10.2 探究模块

#使用dir函数

import copy
import pprint
test = dir(copy)
pprint.pprint(test)

test = [n for n in dir(copy) if not n.startswith('_')]
print(test)

#__all__变量
#这个变量定义了copy模块 的公有接口(public interface)
#更准确地说,它告诉解释器：从模块导入所有名字代表什么含义


print(copy.__all__)

#from copy import *

#如果没有设定__all__,用import * 语句默认将会导入模块中所有不以下划线开头的全局名称

#help 函数

help(copy.copy)

print(copy.copy.__doc__)

#使用help与直接检查文档字符串相比,它的好处在于会获得更多信息,比如函数签名（也就是所带的参数)
print('-----------help copy')
help(copy)

#10.2.3 文档

print(range.__doc__)



#10.2.4 使用源代码

#检查模块的__file__属性，查找源代码的位置

#python 3.0可能移除了，通过help可以查看文件位置

help(range)

