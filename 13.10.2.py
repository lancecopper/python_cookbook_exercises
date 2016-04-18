import ssl
from xmlrpc.server import SimpleXMLRPCServer
from sslmixin import SSLMixin


class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass
    
class KeyValueServer:
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']
    def __init__(self, *args, **kwargs):
        self._data = {}
        self._serv = SSLSimpleXMLRPCServer(*args, allow_none=True, **kwargs)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))
        
    def get(self, name):
        return self._data[name]
        
    def set(self, name, value):
        self._data[name] = value
        
    def delete(self, name):
        del self._data[name]
    
    def exists(self, name):
        return name in self._data
        
    def keys(self):
        return list(self._data)
        
    def serve_forever(self):
        self._serv.serve_forever()
        
if __name__ == '__main__':
    # Private key of the server
    KEYFILE = '/home/lancecopper/code/python/cookbook/server_key.pem' 
    # Server certificate (given to client)     
    CERTFILE = '/home/lancecopper/code/python/cookbook/server_cert.pem'
    kvserv = KeyValueServer(('localhost', 15000),
                            keyfile=KEYFILE,
                            certfile=CERTFILE
                            )
    print('server running...')
    kvserv.serve_forever()
