class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kargs.items():
            self.register(name,url)
    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'
    def __call__(self,path):
        return path.format_map(self.namespaces)