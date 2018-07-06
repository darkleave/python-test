#分叉服务器,windows 不支持分叉，所以会提示:ImportError: cannot import name 'ForkingMixIn'

from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler


class Server(ForkingMixIn,TCPServer): pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from',addr)
        self.wfile.write('Thank you for connecting')


server = Server(('', 1234), Handler)
server.serve_forever()
