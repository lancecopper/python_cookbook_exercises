import struct

class StructField:
    '''
    Descriptor representing a simple structure field
    '''
    def __init__(self, format, offset):
        self.format =  format
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r

class StructureMeta(type):
    '''
    Metaclass that automatically creates StructField descriptors
    '''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset=0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname, 
                        NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)

            
class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer=(bytedata)
    
    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))

class NestedStruct:
    '''
    Descriptor representing a nested structure
    '''
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset
        
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:self.offset+self.struct_type.struct_size]
            result = self.struct_type(data)
            #Save resulting structure back on instance to avoid 
            #further recomputation of this step
            setattr(instance, self.name, result)
            return result

class SizedRecord:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)
        
    @classmethod
    def from_file(cls, f, size_fmt, includes_size=True):
        sz_nbytes = struct.calcsize(size_fmt)
        sz_bytes = f.read(sz_nbytes)
        sz, = struct.unpack(size_fmt, sz_bytes)
        buf = f.read(sz - includes_size * sz_nbytes)
        return cls(buf)
        
    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for off in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, off)
        elif isinstance(code, StructureMeta):
            size = code.struct_size
            for off in range(0, len(self._buffer), size):
                data = self._buffer[off:off+size]
                yield code(data)
 
class Point(Structure):
    _fields_ = [
                ('<d', 'x'),
                ('d', 'y')
                ]
class PolyHeader(Structure):
    _fields_ = [
                ('<i', 'file_code'),
                (Point, 'min'),#nested struct
                (Point, 'max'),#nested struct
                ('i', 'num_polys')
                ]

 
f = open('polys.bin', 'rb')
phead = PolyHeader.from_file(f)
print(phead.num_polys)
polydata = [SizedRecord.from_file(f, '<i') for n in range(phead.num_polys)]
print(polydata)

for n,poly in enumerate(polydata):
    print('Polygon', n)
    for p in poly.iter_as('<dd'):
        print(p)
        
for n,poly in enumerate(polydata):
    print('Polygon', n)
    for p in poly.iter_as(Point):
        print(p.x, p.y)
