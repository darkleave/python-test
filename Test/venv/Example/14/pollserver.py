import socket,select

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))
fdmap = {s.fileno():s}
s.fileno()
s.listen(5)
p = select.poll()
p.register(5)
while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c.addr = s.accept()
            print('Got connection from',addr)
            p.register(c)
            fdmap[c.s.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data: #没有数据--关闭连接
                print(fdmap[fd].getpeername(),'disconnected')
                p.unregister(fd)
                del fdmap[fd]
        else:
            print(data)