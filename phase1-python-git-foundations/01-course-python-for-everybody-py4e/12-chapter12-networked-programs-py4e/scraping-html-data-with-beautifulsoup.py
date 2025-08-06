import urllib.request
import ssl
from bs4 import BeautifulSoup

haris_ssl = ssl.create_default_context()
haris_ssl.check_hostname = False
haris_ssl.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
haris_html = urllib.request.urlopen(url,context=haris_ssl).read()
haris_soup = BeautifulSoup(haris_html,'html.parser')

count = 0
total = 0

haris_tags = haris_soup.find_all('span')

for tag in haris_tags:
    number = int(tag.get_text())
    total += number
    count += 1

print("Count",count)
print("Sum", total)

'''Enter -  http://py4e-data.dr-chuck.net/comments_2261432.html
Count 50
Sum 2459'''