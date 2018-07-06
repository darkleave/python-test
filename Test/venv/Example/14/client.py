import socket
s = socket.socket()

host = socket.gethostname()
port = 1234
print((host, port))
s.connect((host, port))
print(s.recv(1024))

