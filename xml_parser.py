from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
print("Retrieving :",url)
xmldata = urlopen(url, context=ctx).read()
stuff = ET.fromstring(xmldata)
listoftrees = stuff.findall('.//count')
summation=0
for item in listoftrees:
    summation=summation+int(item.text)
print('Sum :',summation)