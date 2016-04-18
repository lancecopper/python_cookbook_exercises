class Spam:
    def bar(self, x:int, y:int):
        print('Bar 1:', x, y)
    
    def bar(self, s:str, n:int = 0):
        print('Bar 2:', s, n)

s = Spam()
print(s.bar(2, 3))
print(s.bar('hello'))
