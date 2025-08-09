# Chapter 12 — Networked Programs

---

This chapter covers working with networked data in Python. It introduces using sockets to retrieve web pages, using `urllib` and `BeautifulSoup` for web scraping, and parsing HTML content dynamically through multiple retrievals.

---

### Exercise — Request Response Cycle

**Task**  
Use Python's `socket` module to connect to a web server, send a simple HTTP GET request, and print the response.

**My code**

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
mysock.connect(('data.pr4e.org', 80))  
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  
mysock.send(cmd)  

while True:  
    data = mysock.recv(512)  
    if len(data) < 1:  
        break  
    print(data.decode(), end='')  

mysock.close()

**Sample Output**  
HTTP/1.1 200 OK
Date: Wed, 06 Aug 2025 15:09:30 GMT
Server: Apache/2.4.52 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

**What it does**  
- Creates a TCP socket connection to a web server.  
- Sends a raw HTTP GET request.  
- Receives the response in chunks of 512 bytes.  
- Decodes and prints the HTTP response content.  
- Closes the socket when done.

---

### Exercise — Scraping HTML Data with BeautifulSoup

**Task**  
Prompt for a URL, retrieve the page using `urllib` with SSL context, parse it with BeautifulSoup, extract all numbers inside `<span>` tags, and print the count and sum.

**My code**

import urllib.request  
import ssl  
from bs4 import BeautifulSoup  

haris_ssl = ssl.create_default_context()  
haris_ssl.check_hostname = False  
haris_ssl.verify_mode = ssl.CERT_NONE  

url = input("Enter - ")  
haris_html = urllib.request.urlopen(url, context=haris_ssl).read()  
haris_soup = BeautifulSoup(haris_html, 'html.parser')  

count = 0  
total = 0  

haris_tags = haris_soup.find_all('span')  

for tag in haris_tags:  
    number = int(tag.get_text())  
    total += number  
    count += 1  

print("Count", count)  
print("Sum", total)

**Sample Output**  
Enter -  http://py4e-data.dr-chuck.net/comments_2261432.html
Count 50
Sum 2459

**What it does**  
- Creates an SSL context that ignores certificate verification.  
- Prompts the user for a URL and retrieves the page content.  
- Parses the HTML using BeautifulSoup.  
- Finds all `<span>` tags on the page.  
- Extracts integer values inside each `<span>`.  
- Counts and sums these numbers.  
- Prints the total count and sum.

---

### Exercise — Following Links with BeautifulSoup

**Task**  
Prompt for a URL, a count, and a position. Follow the link at the given position in the page's anchor tags repeatedly for the specified count, and print the final name found.

**My code**

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
    print("retreiving", url)  
    html = urllib.request.urlopen(url, context=haris_ssl)  
    soup = BeautifulSoup(html, 'html.parser')  
    links = soup.find_all('a')  
    url = links[position - 1].get('href')  

print("Final name:", links[position - 1].text)

**Sample Output**  
Enter URL:  http://py4e-data.dr-chuck.net/known_by_Pyper.html
Enter count: 7
Enter position: 18
retreiving  http://py4e-data.dr-chuck.net/known_by_Pyper.html
retreiving http://py4e-data.dr-chuck.net/known_by_Leigham.html
retreiving http://py4e-data.dr-chuck.net/known_by_Daniyal.html
retreiving http://py4e-data.dr-chuck.net/known_by_Alekzander.html
retreiving http://py4e-data.dr-chuck.net/known_by_Miranne.html
retreiving http://py4e-data.dr-chuck.net/known_by_Loki.html
retreiving http://py4e-data.dr-chuck.net/known_by_Bisma.html
Final name: Richie

**What it does**  
- Sets up SSL context to ignore certificate verification.  
- Prompts for a starting URL, count of repetitions, and link position.  
- Repeatedly retrieves the page, finds all anchor tags.  
- Extracts the URL at the given position and uses it for the next retrieval.  
- After following the chain the specified number of times, prints the final link’s text.

---

## Reflections

This chapter taught me foundational skills for network programming, including raw socket communication, HTTP requests, SSL handling, and web scraping with BeautifulSoup. These techniques are essential for collecting and navigating web data in real AI and ML workflows.