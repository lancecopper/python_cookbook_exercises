from threading import Thread

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = 0
        
    def run(self):
        while self.n > 0:
            print('T-mius', self.n)
            self.n -= 1
            time.sleep(5)
        
c = CountdownThread(5)
c.start
