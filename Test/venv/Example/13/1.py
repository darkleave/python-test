#第13章 数据库支持

#13.1 python 数据库API

#由于所有数据库的大多数基本功能都相同，但是API接口却存在不同的地方，
#为了解决这个问题，使数据库的API接口更加统一规范化，python的标准数据库API(DB API)应运而生.

#13.1.1 全局变量
# 所有与DB API 2.2兼容的数据库模块都必须包含三个全局变量，它们描述了模块的特征.

#Python DB API 的模块属性

#apilevel 使用的Python DB API 版本

#API 级别是一个字符串常量，指出了使用的API版本。DB API 2.0指出，这个变量的值为'1.0'或'2.0'.
#如果没有这个变量，就说明模块不与DB API 2.0兼容，应假定使用的是DB API 1.0.

# threadsafety 模块的线程安全程度如何

#线程安全程度(threadsafety)是一个0-3(含)的整数.0表示线程不能共享模块，
#而3表示模块是绝对线程安全的.1表示线程可共享模块本身，但不能共享连接,
#而2表示线程可共享模块和连接，但不能共享游标.

#paramstyle 在SQL查询中使用哪种参数风格

#参数风格(paramstyle)表示当你查询多个类似的数据库查询时，如何在SQL查询中插入参数.
#'format'表示标准字符串格式设置方式(使用基本的格式编码),如在要插入参数的地方插入%s.
#'pyformat'表示扩展的格式编码，即旧式字典插入使用的格式编码，如%(foo)s.除这些Python 风格外,
#还有三种指定待插入字段的方式：'qmark'表示使用问号,'numeric'表示使用:1 和:2这样的形式表示字段
#(其中的数字是参数的编号)，而'named'表示使用:foobar这样的形式表示字段(其中foobar为参数名).

#13.1.2 异常

#DB API 定义了多种异常，这些异常构成了一个层次结构，因此使用一个except块就能捕获多种异常.

#13.1.3 连接和游标

#连接函数connect

# 函数connect 的常用参数
#dsn 数据源名称，具体含义随数据库而异
#user 用户名
#password 用户密码
#host 主机名
#database 数据库名称

# 连接对象的方法

#close() 关闭连接对象，之后，连接对象及其游标将不可用
#commit() 提交未提交的事务--如果支持的话; 否则什么都不做
#rollback() 回滚未提交的事务(可能不可用)
#cursor() 返回连接的游标对象

#方法rollback 可能不可用，因为并非所有的数据库都支持事务(事务其实就是一系列操作).
#可用时，这个方法撤销所有未提交的事务。

#方法commit总是可用的,但如果数据库不支持事务，这个方法就什么都不做.
#关闭连接时，如果还有未提交的事务，将隐式地回滚它们——仅当数据库支持回滚时才如此!

#游标对象的方法
#callproc(name[,params]) 使用指定的参数调用指定的数据库过程(可选）
#close()  关闭游标，关闭后游标不可用
#execute(oper[,params]) 执行一个SQL操作——可能指定参数
#executemany(oper,pseq) 执行指定的SQL操作多次
#fetchone() 以序列的方式取回查询结果中的下一行；如果没有更多的行，就返回None
#fetchmany([size]) 取回查询结果中的多行，其中参数size的值默认为arraysize
#fetchall() 以序列的方式取回余下的所有行
#nextset() 跳到下一个结果集，这个方法是可选的
#setinputsizes(sizes) 用于为参数预定义内存区域
#sestoutputsize(size[,col]) 为取回大量数据而设置缓存取长度

#游标对象的属性

#description 由结果列描述组成的序列(只读)
#rowcount 结果包含的行数(只读)
#arraysize fetchmany(返回的行数,默认为1)

#13.1.4 类型

#对于插入到某些类型的列中的值，为了能够与底层SQL数据库正确地互操作,
#DB API定义了一些构造函数和常量(单例)，用于提供特殊的类型和值.
#例如,要在数据库中添加日期，应使用相应数据库连接模块中的构造函数Date来创建它，
#这让连接模块能够在幕后执行必要的转换。

#DB API 构造函数和特殊值
#Date(year,month,day)  创建包含日期值的对象
#Time(hour,minute,second) 创建包含时间值的对象
#Timestamp(y,mon,d,h,min,s) 创建包含时间戳的对象
#DateFromTicks(ticks) 根据从新纪元开始过去的秒数创建包含日期值的对象
#TimeFromTicks(ticks) 根据从新纪元开始过去的秒数创建包含时间值的对象
#imestampFromTicks(ticks) 根据从新纪元开始过去的秒数创建包含时间戳的对象
#Binary(string) 创建包含二进制字符串的对象
#STRING  描述基于字符串的列(如CHAR)
#BINARY 描述二进制列(如LONG或ROW)
#NUMBER 描述数字列
#DATETIME 描述日期/时间列
#ROWID 描述行ID 列

#13.2 SQLite 和 PySQLite

#SQLite 作为一个小型数据库引擎，它不需要作为独立的服务器运行，
#且可直接使用本地文件，而不需要集中式数据库存储机制。

#在较新的Python版本(从2.5开始）中，SQLite更具优势，因为标准库包含一个SQLite包装器:
#使用模块sqlite3实现的PySQLite.


