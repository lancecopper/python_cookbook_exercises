def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff!')
    
import dis
#print(dis.dis(countdown))
#print(countdown.__code__.co_code)
c = countdown.__code__.co_code
import opcode
print(opcode.opname[c[0]])
print(opcode.opname[c[3]])
opcode.opname[c[3]]

opcode.opname[c[0]]

