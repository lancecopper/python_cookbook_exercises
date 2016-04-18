from socket import socket, AF_INET, SOCK_STREAM

class LasyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None
        
    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock
        
    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None
        
#Example use
from functiols import partial
conn = LasyConnectin(('www.python.org', 80))
with conn as s1:
    pass
    with conn as s2:
        pass
