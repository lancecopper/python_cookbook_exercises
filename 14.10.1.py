def print_actor():
    while True:
        try:
            msg = yield     # Get a messae
            print('Got:', msg)
        except GeneratorExit:
            print('Actor terminating')
            
# Sample use
p = print_actor()
next(p)     # Advance to the yield(ready to receive)
p.send('Hello')
p.send('World')
p.close()
