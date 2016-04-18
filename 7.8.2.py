from socketserver import StreamRequestHandler, TCPServer
from functools import partial

class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)
        
    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)

print("server is running")
serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
serv.serve_forever()
