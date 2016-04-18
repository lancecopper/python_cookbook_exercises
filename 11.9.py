class foo:
    @property
    def bar(self):
        return self._bar
    
    @bar.setter
    def bar1(self, value):
        self._bar = value
        
    @bar.deleter
    def bar2(self):
        print("Can't delete")
        
a=foo()
a.bar1=1
print(a.bar1)
print(a.bar)
print(a.bar2)
print(a.bar1==a.bar2)
print(a.bar1 is a.bar2)
print(a.bar1 is a.bar)
print(a.bar2 is a.bar)
a.bar2

print(dir(a))
print(type(a.bar1))
