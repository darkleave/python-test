#10.3 标准库

#10.3.1 sys
#sys这个模块让你能够访问与Python解释器联系紧密的变量和函数
import sys

#sys.argv 包含传递到python解释器的参数,包括脚本名称

#exit[arg]
#退出当前的程序,可选参数为给定的返回值或者错误信息,整数0表示退出成功

#modules
#映射模块名字到载入模块的字典

#path
#查找模块所在目录的目录名列表

#platform
#类似sunos5 或者win32的平台标识符

#stdin
#标准输入流——一个类文件(file-like)对象

#stdout

#标准输出流——一个类文件对象

#stderr

#标准错误流——一个类文件对象

#反序打印命令行参数
#sys.argv 第一个元素是脚本的名字
args = sys.argv[1:]

args.reverse()

print(' '.join(args))

#10.3.2 os

import os

#os 模块提供了访问多个操作系统服务的功能,os的子模块os.path还包括一些用于检查,
#构造，删除目录和文件的函数，以及一些处理路径的函数(例如,os.path.split和os.path.join)

#os 模块中一些环境变量和函数

#environ 对环境变量进行映射
#比如要访问系统变量PYTHONPATH,可以使用表达式os.environ['PYTHONPATH'],这个映射也可以用来更改系统环境变量,
#不过并非所有系统都支持.

print(os.environ['PYTHONPATH'])
pythonpath = os.environ['PYTHONPATH']
pythonpath += ';D:\\;'
os.environ['PYTHONPATH'] = pythonpath
print(os.environ['PYTHONPATH'])

#system(command) 在子shell中执行操作系统命令

#sep 路径中的分隔符

#pathsep 分隔路径的分隔符

#linsep 行分隔符('\n'unix,'\r' mac os,or '\r\n' windows

#urandom(n) 返回n 字节的加密强随机数据
#如果正在使用的平台不支持它，会抛出NotImplementedError异常

#os.startfile(r'C:\Users\钟汉忠\Desktop\快捷方式G\WeGame.lnk')

#启动浏览器,打开网页
import webbrowser

webbrowser.open('www.baidu.com')

#10.3.3 fileinput

#input([files[,inplace[,backup]])  便于遍历多个输入流中的行

#filename() 返回当前文件的名称
#lineno() 返回当前(累计)的行数
#filelineno() 返回当前文件的行数
#isfirstline() 检查当前行是否是文件的第一行
#isstdin() 检查文件最后一行是否来自sys.stdin
#nextfile() 关闭当前文件，移动到下一个文件
#close() 关闭序列

#为Python脚本添加行号
#rstrip 是可以返回字符串副本的字符串方法，右侧的空格都被删除
import fileinput

for line in fileinput.input(inplace=True,backup='aaa'):
    line = line.rstrip()
    num = fileinput.lineno()
    print('%-40s # %2i' % (line,num))

#inplace参数设为真值(inplace=True)以进行原地处理,对于要访问的每一行，需要打印出替代的内容,
#以返回到当前的输入文件中,在进行原地处理的时候,可选的backup参数将文件名扩展备份到通过原始文件创建的备份文件中.

#结果就是原文件逐行被替换了，在这个程序中是逐行添加了行号

#为已编号的行进行编号

import fileinput

for line in fileinput.input(inplace=1):
    line = line.rstrip()
    num = fileinput.lineno()
    print('%-40s # %2i' % (line,num))

