from xml.etree.ElementTree import parse, Element
doc = parse('rows.xml')
root = doc.getroot()
print(root)