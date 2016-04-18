from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters(if any)
parms = {
         'name1':'value1',
         'name2':'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Extra headers
headers = {
           'User_agent':'none/ofyourbusiness',
           'Spam':'Eggs',
           'test':'hahahah'
}

req = request.Request(url, querystring.encode('ascii'), headers=headers)

# Make a request and read the response
u = request.urlopen(req)
resp = u.read()
resp = resp.decode(encoding='utf-8')
print(resp)
print('TYPE: ',type(resp))
