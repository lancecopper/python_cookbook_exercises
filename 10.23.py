import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.childre = []
    
    def __repr__(self):
        return 'Node({!r:})'.format(self.value)
        
    #property that manages the parent as a weak_reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()
           
    @parent.setter
    def paretn(self, node):
        self._parent = weakref.ref(node)
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        

