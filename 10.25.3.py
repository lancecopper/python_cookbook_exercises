import weakref

class CachedSpamManager:

    def __init__(self):
        self._cache=weakref.WeakValueDictionary()
        
    def get_spam(self,name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name]=s
        else:
            s = self._cache[name]
        return s
        
    def clear(self):
        self._cache.clear()
        
class Spam:
    manager = CachedSpamManager()
    def __init__(self, name):
        self.name = name
        
    def get_spam(name):
        return Spam.manager.get_spam(name)
