import re

filename=input("Enter name of the file to be opened.")
fhand=open(filename)
finallist=[]
sum=0
for line in fhand:
    num_list=re.findall('[0-9]+',line)
    finallist=finallist+num_list
for num in finallist:
    sum=sum+int(num)
print(sum)