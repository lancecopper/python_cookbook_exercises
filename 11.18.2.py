import operator
import types
import sys

def named_tuple(classname, fieldnames):
    #Populate a dictionary of field property accessors
    cls_dict = {name: property(operator.itemgetter(n))}
    
    #Make a __new__ function and add to the class dict
    def __new__(cls, *args):
        if len(args) != len(fieldnames)
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)
        
    cls_dict['__new__'] = __new__
    
    #Make the class
    cls = types.new_class(classname, (tuple,), {}, lambda ns: ns.update(cls_dict))
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls
