from sample2 import *
with open('./test.txt', 'rb') as f:
    for line in f:
        print(type(line))
        print_chars(line)





