from urllib import request, parse

#Base URL being accessed
url = 'http://httpbin.org/get'

#Dictionary of query parameters(if any)
parms = {
         'name1':'value1',
         'name2':'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)
print(querystring)

# Make a GET request and read the response
u = request.urlopen(url+'?'+querystring)
resp = u.read()
resp = resp.decode(encoding='utf-8')
print(resp)
print(type(resp))
         
         
