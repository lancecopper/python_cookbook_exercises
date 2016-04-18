from xml.etree.ElementTree import iterparse
from collections import Counter 


def parse_and_remove(filename,path):
    path_parts=path.split('/')
    doc = iterparse(filename,('start', 'end'))
    #skip the root element
    next(doc)
    
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
            print("start.\n")
            print("tag_stack:",tag_stack,"\n")
            print("elem_stack",elem_stack,"\n")
        elif event == 'end':
            if tag_stack == path_parts:
                print("end.\n")
                print("elem:",elem)
                yield elem
                print("elem_stack[-2]",elem_stack[-2])
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass
    
patholes_by_zip = Counter
data = parse_and_remove('rows.xml','row/row')
i=0
for pothole in data:
    i+=1
    print(i,"\n")