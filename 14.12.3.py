def gene1():
    n = yield 1000000
    print('n={}'.format(n))
    while n > 0:    
        n = yield n ** 2
    return 'over'
        
    
def gene():
    result = yield from gene1()
    print('result is {}'.format(result))
    
a=gene()
i = 10
c=a.send(None)
print('first:{}'.format(c))
while i > 0:
    ret = a.send(i)
    print('get {}'.format(ret))
    i -= 1
try:
    a.send(0)
except StopIteration as e:
    print('exception:{}'.format(e))
