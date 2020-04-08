import urllib.request, urllib.parse,urllib.error
import json

serviceurl = "http://py4e-data.dr-chuck.net/json?"
line=input('Address:')
address = line.strip()

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

parms = dict()
parms["address"] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print(url)