import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host,port))
s.listen(5)
inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], [])
    print(rs,ws,es)
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print('Got connection from', addr)
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
                print(disconnected)
            except socket.error:
                disconnected = True
