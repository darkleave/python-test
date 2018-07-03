#第11章：文件和流

#11.1 打开文件

#使用open函数打开文件
#open(name[,mode[,buffering]])

f = open(r'D:\work\zhzwork\pythonProject\Test\venv\Example\10\1.py')

#11.1.1 文件模式

#open 函数 mode 模式参数常用值
# 'r' 读模式
#'w' 写模式
#'a' 追加模式
#'b' 二进制模式(可添加到其它模式中使用)
#'+' 读/写模式(可添加到其它模式中使用)

#'b' 模式改变处理文件的方法，一般来说,Python 假定处理的是文本文件(包含字符).
#这样做通常不会有问题，但如果处理的是一些其它类型的文件(二进制文件)，比如声音剪辑或者图像,
#那么应该在模式参数中增加'b'. 参数'rb'可以用来读取一个二进制文件.

#11.1.2 缓冲

#11.2 基本的文件方法

#11.2.1 读和写

f = open('./somefile.txt','w')
f.write('Hello,')
f.write('World!')
f.close()

f = open('somefile.txt','r') #默认是r模式，可省略
test = f.read(4)#读取4个字符
print(test)
test = f.read()#读取剩余的全部
print(test)

#11.2.3 读写行

#11.2.4 关闭文件

#Open your file here
try:
    # Write data to your file
    pass
finally:
    #file.close()
    pass

#with 语句可以打开文件并且将其赋值到变量上,之后就可以将数据写入语句体中的文件(或许执行其它操作).
#语句在语句结束后会被自动关闭,即使是由于异常引起的结束也是如此.

with open('somefile.txt') as somefile:
     print('hhhhhhh')

#在写入了一些文件内容后，数据可能被缓存了(在内存中临时性地存储),直到关闭文件才会被写入到文件.
#如果需要继续使用文件(不关闭文件),又想将磁盘上地文件进行更新,以反映这些修改，那么就要调用
#文件对象的flush方法

#11.2.5 使用基本文件方法

#11.2.5 使用基本的文件方法

f = open(r'test.txt')
test = f.read(7)
print(test)
test = f.read(4)
print(test)
f.close()

f = open(r'test.txt')
print(f.read())
f.close()

f = open(r'test.txt')
for i in range(3):
    print(str(i) + ': ' + f.readline())

f.close()

import pprint
pprint.pprint(open(r'test.txt').readlines())

f = open(r'test.txt','w')
f.write('this\nis no\nhaiku')
f.close()

f = open(r'test.txt')
lines = f.readlines()
f.close()
lines[1] = "isn't a\n"
f = open(r'test.txt','w')
f.writelines(lines)
f.close()

pprint.pprint(open(r'test.txt').readlines())

#11.3 对文件内容进行迭代


#11.3.1 按字节处理

def process(string):
    print('Processing: ',string)

f = open(r'test.txt')
char = f.read(1)
while char:
    process(char)
    char = f.read(1)
f.close()

#去除重复代码

f = open(r'test.txt')
while True:
    char = f.read(1)
    if not char: break
    process(char)
f.close()

#11.3.2 按行操作

f = open(r'test.txt')
while True:
    line = f.readline()
    if not line: break
    process(line)
f.close()

#11.3.3 读取所有内容
#用read迭代每个字符
f = open(r'test.txt')
for char in f.read():
    process(char)
f.close()

#用readlines 迭代行

f = open(r'test.txt')
for line in f.readlines():
    process(line)
f.close()

#11.3.4 使用fileinput 实现懒惰行迭代

import fileinput
for line in fileinput.input(r'test.txt'):
    process(line)

#11.3.5 文件迭代器

f = open(r'test.txt')
for line in f:
    process(line)
f.close()

#只要是没有向文件写入内容，那么不关闭文件也是可以的

#对文件进行迭代而不使用变量存储文件对象
for line in open(r'test.txt'):
    process(line)

"""
import sys
for line in sys.stdin:
    process(line)
"""



f = open('somefile.txt','w')
f.write('First line\n')
f.write('Second line\n')
f.write('Third line\n')
f.close()

lines = list(open('somefile.txt'))
print(lines)
first,second,third = open('somefile.txt')
print(first)
print(second)
print(third)



