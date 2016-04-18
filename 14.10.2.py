from queue import Queue
from threading import Thread, Event

# Sentinel used for shutdown
class ActorExit(Exception):
    pass
    
class Actor:
    def __init__(self):
        self._mailbox = Queue()
        
    def send(self, msg):
        '''
        Send a message to the actor
        '''
        self._mailbox.put(msg)
        
    def recv(self):
        '''
        Receive an incoming message
        '''
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg
        
    def close(self):
        '''
        Close the actor, thus shutting it down
        '''
        self.send(ActorExit)
        
    def start(self):
        '''
        Start concurrent execution
        '''
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()
        
    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()
            
    def join(self):
        self._terminated.wait()
        
    def run(self):
        '''
        Run method to be implemented by the user
        '''
        while True:
            msg = self.recv()
            

class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self,'do_'+tag)(*payload)

    # Methods correponding to different message tags
    def do_A(self, x):
        print('Running A', x)

    def do_B(self, x, y):
        print('Running B', x, y)

# Example
a = TaggedActor()
a.start()
a.send(('A', 1))            # Invokes do_A(1)
a.send(('B', 2, 3))         # Invokes do_B(2,3)
a.close()
a.join()
