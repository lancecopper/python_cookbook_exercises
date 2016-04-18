from xmlrpc.client import SafeTransport, ServerProxy
import ssl

class VerifyCertSafeTransport(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        SafeTransport.__init__(self)
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._ssl_context.load_verify_locations(cafile)
        if certfile:
            self._ssl_context.load_cert_chain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED
        
def make_connection(self, host):
    # Items in the passed dictionary are passed as keyword
    # arguments to the http.client.HTTPSConnection() constructor.
    # The context argument allows an ssl.SSLContext instance to
    # be passed with information about the SSL configuration
    s = super().make_connection((host, {'context': self._ssl_context}))
    
    return s


# Create the client proxy
s = ServerProxy('https://localhost:15000',
                transport=VerifyCertSafeTransport('server_cert.pem'),
                allow_none=True)
    
