#字符串格式化

#在%的左侧放置一个字符串(格式化字符串),而右侧则放置希望被格式化的值,
#可以使用一个值，一个字符串或者数字，也可以使用多个值的元组或者字典，一般使用元组
format = 'Hello,%s,%s, enough for ya?'
values = ('world','hot')
print(format % values)

#格式化浮点数
#使用f说明转换说明符的类型,同时提供所需要的精度,一个句点再加上希望保留的小数位数
#因为格式化转换说明符总是以表示类型的字符结束,所以精度应该放在类型字符前面
format = 'Pi with three decimals:%.3f'
from math import pi
print(format % pi)
