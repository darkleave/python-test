#字符串格式化：完整版
#简单转换

formatTest1 = 'Price of eggs: $%d' % 42
print(formatTest1)

formatTest2 = 'Hexadecimal price of eggs: %x' % 42
print(formatTest2)

from math import pi
formatTest3 = 'Pi:%f...' % pi
print(formatTest3)
formatTest4 = 'Very inexact estimate of pi: %i' % pi
print(formatTest4)
#Python3.0之后采用不同的语法，在长整数方面已经取消在整数后面添加L的语法，
# 因为所有数字会自动识别为短整数，还是长整数，不需要增加L了
formatTest5 = 'Using str: %s' % 42
print(formatTest5)
formatTest6 = 'Using repr: %r' % 42
print(formatTest6)

