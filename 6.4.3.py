class Node2:
    def __init__(self, value):
        self._value=value
        self._children=[]
    
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
        
    def add_child(self, node):
        self._children.append(node)
        
    def __iter__(self):
        return iter(self._children)
        
    def depth_first(self):
        return DepthFirstIterator(self)
        
        
class DepthFirstIterator:
    
    def __init__(self, start_node):        
        self._node = start_node
        self._children_iter = None
        self._child_iter = None
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._children_iter is None:
   #         print('test',self._node,'\n')
            print('##1##/n')
            self._children_iter = iter(self._node)
            print('##2##/n')
  #          print(self,self._children_iter,self._child_iter,'\n')
            return self._node
        elif self._child_iter:
            try:
                print('##3##/n')
                nextchild = next(self._child_iter)
                print('##4##/n')
    #            print(self,self._children_iter,self._child_iter,'\n')
                return nextchild
            except StopIteration:
                print('##5##/n')
                self._child_iter = None
                print('##6##/n')
   #             print(self,self._children_iter,self._child_iter,'\n')
                return next(self)
        else:
            print('##7##/n')
            self._child_iter =  next(self._children_iter).depth_first()
            print('##8##/n')
 #           print(self,self._children_iter,self._child_iter,'\n')
            return next(self)
         
if __name__ == '__main__':
    root = Node2(0)
    child1 = Node2(1)
    child2 = Node2(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node2(3))
    child1.add_child(Node2(4))
    child2.add_child(Node2(5))
    for ch in root.depth_first():
        print(ch)