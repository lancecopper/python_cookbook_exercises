from contextlib import contextmanager
import time

@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))

with timeblock('counting'):
    n = 100000
    while n > 0 :
        n -= 1
        




