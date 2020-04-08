from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urlopen(url, context=ctx).read()
js=json.loads(data)
summation=0
for item in js['comments']:
    summation=summation+int(item['count'])
print(summation)
