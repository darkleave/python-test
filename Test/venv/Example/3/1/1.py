#所有标准的序列操作(索引,分片，乘法，判断成员资格,求长度，取最小值和最大值对字符串同样适用
#但字符串始终不变,因此，如下所示的项或分片赋值都是不合法的
website = 'http://www.python.org'
test = website[-3:]
print(test)
website[-3:] = 'com'
