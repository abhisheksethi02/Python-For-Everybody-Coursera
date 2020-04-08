from urllib.request import urlopen 
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
spanlist=re.findall('([0-9]+)</span>',html.decode())
summation=0
count=0
for element in spanlist:
    summation=summation+int(element)
    count=count+1
print("Count",count)
print("Sum",summation)
