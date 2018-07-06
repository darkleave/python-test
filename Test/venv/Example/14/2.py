#14.1.2 模块 urllib 和 urllib2

#1. 打开远程文件

from urllib.request import urlopen
from urllib.request import urlretrieve
import re

webpage = urlopen('http://www.python.org')
text = webpage.read()
m = re.search(b'<a href="([^"]+)" .*?>about</a>',text,re.IGNORECASE)
result = m.group(1)
print(result)

#获取远程文件

urlretrieve('http://www.python.org','D:\\python_webpage.html')

#14.1.3 其它模块

#标准库中一些与网络相关的模块

#asynchat 包含补充asyncore的功能
#asyncore 异步套接字处理程序
#cgi 基本的cgi支持
#Cookie    Cookie 对象操作,主要用于服务器
#cookielib 客户端cookie支持
#email 电子邮件(包括MIME)支持
#ftplib ftp 客户端模块
#gopherlib Gopher 客户端模块
#httplib HTTP 客户端模块
#imaplib IMAP4 客户端模块
#mailbox 读取多种邮箱格式
#mailcap 通过mailcap文件访问MIME配置
#mhlib 访问MH邮箱
#nntplib NNTP客户端模块
#poplib POP 客户端模块
#robotparser 解析Web服务器robot文件
#SimpleXMLRPCServer 一个简单的XML-RPC服务器
#smtpd SMTP 服务器模块
#smtplib SMTP 客户端模块
#telnetlib Telnet 客户端模块
#urlparse 用于解读URL
#xmlrpclib XML-RPC客户端支持

#14.2 SocketServer 及相关的类
#模块SocketServer 是标准库提供的服务器框架的基石，
#这个框架包括BaseHTTPServer,SimpleHTTPServer,CGIHTTPServer,SimpleXMLRPCServer和DocXMLRPCServer,
#它们在基本服务器的基础上添加了各种功能

#SocketServer包含4个基本的服务器: TCPServer(支持TCP套接字流),UDPServer(支持UDP数据报套接字)
#以及更难懂的UnixStreamServer 和 UnixDatagramServer .

