# import requests

# url='http://mob4.mobilog.info/lt/core/login.cgi'

# request = requests.get(url)
# print(request.content)
# print (request.status_code)


import requests
import sys


InstanceUrl = sys.argv[1]


data = {

    
  }
    

headers = {'Content-Type': 'application/json'}

url = InstanceUrl
r = requests.get(url, json=data, headers=headers)
print( r.status_code)

