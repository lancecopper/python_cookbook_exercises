import threading
import time

# Worker thread
def worker(n, sema):
    # Wait to be signaled
    sema.acquire()
    
    # Do some work
    print('Working', n)
    time.sleep(1)
    sema.release()

# Create some threads
sema = threading.Semaphore(1)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()

