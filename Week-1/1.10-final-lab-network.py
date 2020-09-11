#!/usr/bin/env python3

import requests
import socket

def check_connectivity(url):
   request = requests.get(url)
   response = request.status_code
   if response == int(200):
      return True
   return False

def check_localhost(localhost):
   get_localhost = socket.gethostbyname(localhost)
   if get_localhost == "127.0.0.1":
      return True
   return False

print (check_connectivity("http://www.google.com"))
print (check_localhost('localhost'))


""" 
#!/usr/bin/env python3
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == '127.0.0.1':
        return True
    return False


def check_connectivity():
    request = requests.get('http://www.google.com')
    response = request.status_code
    if response == 200:
        return True
    return False 
"""







