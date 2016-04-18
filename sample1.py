# sample.py

import pdb

def func(n):
    if n>10:
        n = n + 10
        return n + 10    
    else:
        n *= 3
        return func(n)

func(1)
