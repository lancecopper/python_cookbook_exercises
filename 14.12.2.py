from collections import deque
from select import select
import logging
log=logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


# This class represents a generic yield event in the sheduler
class YieldEvent:
    def handle_yield(self, sched, task):
        pass
    def handle_resume(self, sched, task):
        pass

# Task Scheduler
class Scheduler:
    def __init__(self):
        self._numtasks = 0              # Total num of tasks
        self._ready = deque()           # Tasks ready to run
        self._read_waiting = {}         # Tasks waiting to read
        self._write_waiting = {}        # Tasks waiting to write

    # Poll for I/O events and restart waiting tasks
    def _iopoll(self):
        log.debug('***_iopoll*** is called\n')
        reset, wset, eset = select(self._read_waiting, self._write_waiting, [])
        for r in reset:            
            evt, task = self._read_waiting.pop(r)
            log.debug('pop ({},{}) from _read_waiting for handle_resume\n'.format(evt,task))
            evt.handle_resume(self, task)
        for w in wset:            
            evt, task = self._write_waiting.pop(w)
            log.debug('pop ({},{}) from _write_waiting for handle_resume\n'.format(evt,task))
            evt.handle_resume(self, task)
            
    def new(self, task):
        '''
        Add add newly started task to the scheduler
        '''
        log.debug('***New*** is called\n')
        self._ready.append((task,None))
        log.debug('append newly started task({},{}) to _ready\n'.format(task,None))
        self._numtasks += 1
        log.debug('_numtasks is {}\n'.format(self._numtasks))
        
    def add_ready(self, task, msg=None):
        '''
        Append an already started task to the ready queue. 
        msg is what to send into the task when it resumes. 
        '''
        log.debug('add_ready is called\n')
        self._ready.append((task, msg))
        log.debug('append already started task({},{}) to _ready\n'.format(task,msg))
        
    # Add a task to the reading set
    def _read_wait(self, fileno, evt, task):
        log.debug('_read_wait is called\n')
        self._read_waiting[fileno] = (evt, task)
        log.debug('add task({},{}) as[{}] to _ready_waiting\n'.format(evt, task, fileno))
        
    # Add a task to the write set
    def _write_wait(self, fileno, evt, task):
        log.debug('_wirte_wait is called\n')
        self._write_waiting[fileno] = (evt, task)
        log.debug('add task({},{}) as[{}] to _write_waiting\n'.format(evt, task, fileno))
    
    def run(self):
        '''
        Run the task scheduler until there are no tasks
        '''
        while self._numtasks:
            log.debug('run is called\n')
            if not self._ready:
                self._iopoll()
            task, msg = self._ready.popleft()
            log.debug('pop ({},{}) from _ready\n'.format(task, msg))
            
            try:
                # Run the coroutine to the next yield
                r = task.send(msg)
                log.debug('get {}\n'.format(r))
                if isinstance(r, YieldEvent):
                    r.handle_yield(self, task)
                else:
                    log.debug('********unrecognized yield event')
                    raise RuntimeError('unrecognized yield event')
            except StopIteration:
                log.debug('********StopIteration')
                self._numtasks -= 1
                log.debug('_numtasks is {}\n'.format(self._numtasks))
                
# Example implementation of coroutine-based socket I/O
class ReadSocket(YieldEvent):
    def __init__(self, sock, nbytes):
        self.sock = sock
        self.nbytes = nbytes
    def handle_yield(self, sched, task):
        log.debug('handle_yield, ReadSocket')
        sched._read_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        log.debug('handle_resume, ReadSocket')
        data = self.sock.recv(self.nbytes)
        sched.add_ready(task, data)
        
class WriteSocket(YieldEvent):
    def __init__(self, sock, data):
        self.sock = sock
        self.data = data
    
    def handle_yield(self, sched, task):
        log.debug('handle_yield, WriteSocket\n')
        sched._write_wait(self.sock.fileno(), self, task)
    
    def handle_resume(self, sched, task):
        log.debug('handle_resume, WriteSocket\n')
        nsent = self.sock.send(self.data)
        sched.add_ready(task, nsent)
    
class AcceptSocket(YieldEvent):
    def __init__(self, sock):
        self.sock = sock
        
    def handle_yield(self, sched, task):
        log.debug('handle_yield, AcceptSocket\n')
        sched._read_wait(self.sock.fileno(), self, task)
    
    def handle_resume(self, sched, task):
        log.debug('handle_resume, AcceptSocket\n')
        r = self.sock.accept()
        sched.add_ready(task, r)

# Wrapper around a socket object for use with yield
class Socket(object):
    def __init__(self, sock):
        self._sock = sock
    def recv(self, maxbytes):
        return ReadSocket(self._sock, maxbytes)
    def send(self, data):
        return WriteSocket(self._sock, data)
    def accept(self):
        return AcceptSocket(self._sock)
    def __getattr__(self, name):
        return getattr(self._sock, name)
        
if __name__ == '__main__':
    from socket import socket, AF_INET, SOCK_STREAM
    import time
    
    # be called using line = yield from readline(sock)
    def readline(sock):
        chars = []
        while True:
            c = yield sock.recv(1)                          # ReadSocket
            log.debug('readline, yiled c={}'.format(c))
            if not c:
                break
            chars.append(c)
            if c == b'\n':
                break
        return b''.join(chars)

    # Echo server using generators
    class EchoServer:
        def __init__(self,addr,sched):
            self.sched = sched
            sched.new(self.server_loop(addr))
        
        def server_loop(self,addr):
            s = Socket(socket(AF_INET,SOCK_STREAM))
        
            s.bind(addr)
            s.listen(5)
            while True:
                c,a = yield s.accept()                      # AcceptSocket
                log.debug('c,a=s.accept, c={},a={}\n'.format(c,a))
                print('Got connection from ', a)
                self.sched.new(self.client_handler(Socket(c)))

        def client_handler(self,client):
            while True:
                line = yield from readline(client)
                print('get line {}\n'.format(line))
                if not line:
                    break
                line = b'GOT:' + line
                while line:
                    nsent = yield client.send(line)         # WriteSocket
                    log.debug('nsent='.format(nsent))
                    line = line[nsent:]
            client.close()
            print('Client closed')
            
    sched = Scheduler()
    EchoServer(('',16000),sched)
    sched.run()
