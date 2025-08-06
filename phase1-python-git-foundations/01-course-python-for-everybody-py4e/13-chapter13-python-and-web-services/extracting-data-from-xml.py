import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter - ")
print("Retreiving",url)
html = urllib.request.urlopen(url).read()
print("Retrieving",len(html),"characters")
tree = ET.fromstring(html)
numbers = 0
total_count = 0
counts = tree.findall('.//count')
for i in counts:
    total_count+=1
    numbers += int(i.text)

print("Count:",total_count)
print("Sum:",numbers)


'''Enter -  http://py4e-data.dr-chuck.net/comments_2261434.xml 
Retreiving  http://py4e-data.dr-chuck.net/comments_2261434.xml 
Retrieving 4218 characters
Count: 50
Sum: 2801'''