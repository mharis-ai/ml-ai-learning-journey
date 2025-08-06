import urllib.request
import ssl
from bs4 import BeautifulSoup

haris_ssl = ssl.create_default_context()
haris_ssl.check_hostname = False
haris_ssl.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = int(input("Enter count: "))  
position = int(input("Enter position: "))

for i in range(count):
    print("retreiving",url)
    html = urllib.request.urlopen(url,context=haris_ssl)
    soup = BeautifulSoup(html,'html.parser')
    links = soup.find_all('a')
    url = links[position - 1].get('href')

print("Final name:", links[position - 1].text)

'''Enter URL:  http://py4e-data.dr-chuck.net/known_by_Pyper.html
Enter count: 7
Enter position: 18
retreiving  http://py4e-data.dr-chuck.net/known_by_Pyper.html
retreiving http://py4e-data.dr-chuck.net/known_by_Leigham.html
retreiving http://py4e-data.dr-chuck.net/known_by_Daniyal.html
retreiving http://py4e-data.dr-chuck.net/known_by_Alekzander.html
retreiving http://py4e-data.dr-chuck.net/known_by_Miranne.html
retreiving http://py4e-data.dr-chuck.net/known_by_Loki.html
retreiving http://py4e-data.dr-chuck.net/known_by_Bisma.html
Final name: Richie'''