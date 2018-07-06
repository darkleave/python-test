#第14章 网络编程
#Python提供了强大的网络编程支持,有很多库实现了常见的网络协议以及基于这些协议的抽象层.

#14.1 几个网络模块

#14.1.1 模块socket

#网络编程的一个基本组件是套接字(socket),套接字基本上是一个信息通道，两端各有一个程序.
#这些程序可能位于(通过网络相连的)不同的计算机上，通过套接字向对方发送信息.

#套接字分为两类: 服务器套接字和客户端套接字. 创建服务器套接字后，让它等待连接请求的到来.
#这样，它将在某个网络地址(由IP地址和端口号组成)处监听,直到客户端套接字建立连接.

#套接字是模块socket中socket类的实例.实例化套接字最多可指定三个参数：一个地址族(默认为socket.AF_INET);
#是流套接字(socket.SOCK_STREAM,默认设置)还是数据报套接字(socket.SOCK_DGRAM);协议(使用默认值0就好).
#创建普通套接字时,不用提供任何参数


#最简单的服务器

import socket
s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host,port))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from',addr)
    c.send(b'Thank you for connecting')
    c.close()


