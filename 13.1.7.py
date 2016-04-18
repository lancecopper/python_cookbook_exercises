import urllib.request

auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password('pypi','http://pypi.python.org','username','password')
opener = urllib.request.build_openner(auth)
r = urlib.request.Request('http//pypi.python.org?:action=login')
u = opener.open(r)
resp = u.read()


