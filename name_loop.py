from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count=int(input('Enter Count: '))
position=int(input('Enter Position: '))
while True:
    if count==0:
        break
    print("Retrieving :",url)
    html = urlopen(url, context=ctx).read()
    urllist=re.findall('href="(.+)"',html.decode())
    url=urllist[position-1]
    count=count-1
print("Retrieving :",url)
urlrecord=url.split('_')
urlrecord1=urlrecord[2].split('.')
print(urlrecord1[0])
#again i could not install beautiful soup so i used re