from struct import Struct
from collections import namedtuple

def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return(record_struct.unpack(chunk) for chunk in chunks)
    
    
def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))
        
#if __name__ == '__main__':
#    with open('data.b', 'rb') as f:
#        print(read_records('<idd',f))
#        for rec in read_records('<idd',f):
#            print(rec)

#if __name__ == '__main__':
#    with open('data.b', 'rb') as f:
#        data = f.read()
#    print(unpack_records('<idd', data))
#    for rec in unpack_records('<idd', data):
#        print(rec)

Record=namedtuple('Record', ['kind','x','y'])

with open('data.b', 'rb') as f:
    records=(Record(*r) for r in read_records('<idd',f))
    for r in records:
        print(r.kind, r.x, r.y)