import socket

port = 1234

for i in range(10):

    print('---------------------------:' + str(i))
    s = socket.socket()

    host = socket.gethostname()
    port += i
    print((host, port))
    s.connect((host, port))
    print(s.recv(1024))



