#第10章 自带电池

#10.1 模块
#10.1.1 模块是程序

import sys
print(sys.path)
#添加系统目录，除了从默认的目录中寻找外，还需要从目录c:\python 中寻找模块
#模块相当于java中的类
sys.path.append('c:/python')
#在导入模块的时候，其中的代码被执行了，输出Hello World
import hello
import hello
#模块导入一般只会导入一次，而不会重新导入，同时也能避免两个模块互相导入而产生的无限递归行为

#如果想要重复导入，可以使用reload函数,python 3.0已去除reload函数
#hello = reload(hello)

#10.1.2 模块用于定义

#模块在第一次导入到程序中时被执行,真正的用处在于它们(像类一样)可以保持自己的作用域,
#这就意味着所有类和函数以及赋值后的变量都成为了模块的特性.

#如果希望模块能够像程序一样被执行,可以对python解释器使用-m切换开关来执行程序,
#例如对progname.py 使用 python -m progname args 命令即可运行带命令行参数args的progname程序.

import hello2
hello2.hello()

#模块的意义
#模块的一个重要意义在于代码重用，将代码放在模块中，就可以在多个程序中使用这些代码了。

import hello3

#10.1.3 让你的模块可用

import sys,pprint
#pprint是一个智能打印函数，一般用来处理较大的数据结构
pprint.pprint(sys.path)

#python 可以从sys.path包含的目录中找到所需的模块
#尽管这些目录都可以使用，但site-packages 目录时最佳选择，因为它就是用来做这些事情的.

#除了直接在sys.path中添加模块存储目录外，还有更加通用的方法
#那就是在PYTHONPATH环境变量中包含模块所在的目录

#注意，你所使用的IDE可能会有自身的机制，用于设置环境变量和Python路径

#note:包含模块代码的文件的名字要和模块名一样，再加上.py扩展名

#10.1.4 包

#为了组织好模块, 你可以将它们分组为包(package),包基本上就是另外一类模块,但是它们能包含其他模块.
#当模块存储在文件中时(扩展名.py),包就是模块所在的目录.
#为了让Python将其作为包对待，它必须包含一个命名为__init__py的文件(模块),
#如果将它作为模块导入的话，文件的内容就是包的内容.

import constants
import constants.include
#无法导入带-的包名
#import package-test2.noInclude

