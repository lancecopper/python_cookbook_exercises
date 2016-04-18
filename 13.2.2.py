from socketserver import StreamRequestHandler, TCPServer
class EchoHandler(StreamRequestHandler):
    print('Got connection from', self.client_address)
    # self.rfile is a file-like object for reading
    for line in self.rfile:
        # self.rfile is a file-like object for writing
        self.wfile.write(line)

if __name__ = '__main__':
    serv = TCPServer(('localhost', 20000), EchoHandler)
    serv.serve_forever
    
    
    
