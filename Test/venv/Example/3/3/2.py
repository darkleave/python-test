#字段宽度和精度
from math import pi
formatTest = '%10f' % pi
print(formatTest)
formatTest1 = '%10.2f' % pi
print(formatTest1)
formatTest2 = '%.2f' % pi
print(formatTest2)
formatTest3 = '%.5s' % 'Guido van Rossum'
print(formatTest3)
#可以使用*(星号)作为字段宽度或者精度(或者两者都使用*),此时数值会从元组参数中读出:
formatTest4 = '%.*s,%s,%.*s' % (5,'Guido van Rossum','test',4,'Helloman')
print(formatTest4)
