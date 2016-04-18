import requests

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters(if any)

parms = {
         'name1':'value1',
         'name2':'value2'
}

#Extra headers
headers = {
           'User_agent':'none/ofyourbusiness',
           'Spam':'Eggs',
           'test':'hahahah'
}

resp = requests.post(url, data=parms, headers=headers)


# Decoded text returned by the request
text = resp.text
json= resp.json()
print(json)
         
         
