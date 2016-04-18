try:
    cilent_obj.get_url(url)
except(URLError, ValueError, SocketTimeout):
    client_obj.remove_url(url)





