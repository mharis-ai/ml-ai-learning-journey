# Chapter 13 — Python and Web Services

---

This chapter explores retrieving and processing data from web services, including XML parsing, JSON handling, and using web APIs with URL encoding and SSL.

---

### Exercise — Extract Data From XML

**Task**  
Prompt for a URL, retrieve XML data, parse it, extract all `<count>` elements, and compute their sum and count.

**My code**

import urllib.request  
import xml.etree.ElementTree as ET  

url = input("Enter - ")  
print("Retreiving", url)  
html = urllib.request.urlopen(url).read()  
print("Retrieving", len(html), "characters")  
tree = ET.fromstring(html)  
numbers = 0  
total_count = 0  
counts = tree.findall('.//count')  
for i in counts:  
    total_count += 1  
    numbers += int(i.text)  

print("Count:", total_count)  
print("Sum:", numbers)

**Sample Output**  
Enter -  http://py4e-data.dr-chuck.net/comments_2261434.xml 
Retreiving  http://py4e-data.dr-chuck.net/comments_2261434.xml 
Retrieving 4218 characters
Count: 50
Sum: 2801

**What it does**  
- Prompts for an XML URL.  
- Retrieves the raw XML content.  
- Parses XML using ElementTree.  
- Finds all `<count>` elements.  
- Counts the elements and sums their integer values.  
- Prints the total count and sum.

---

### Exercise — Extract Data From JSON

**Task**  
Prompt for a JSON URL, retrieve and parse JSON data, extract values from a nested list of dictionaries, and compute their sum and count.

**My code**

import urllib.request, json  

url = input("Enter - ")  
print("Retrieving", url)  
json_url = urllib.request.urlopen(url)  
json_data = json_url.read()  
print("Retrieved", len(json_data), "characters")  

info = json.loads(json_data)  
count = 0  
total = 0  
for item in info["comments"]:  
    count += 1  
    total += item["count"]  
print("Count:", count)  
print("Sum:", total)

**Sample Output**  
Enter -  http://py4e-data.dr-chuck.net/comments_2261435.json
Retrieving  http://py4e-data.dr-chuck.net/comments_2261435.json
Retrieved 2727 characters
Count: 50
Sum: 2542

**What it does**  
- Prompts for a JSON URL.  
- Retrieves JSON data as bytes.  
- Decodes and parses JSON.  
- Iterates over the `"comments"` list of dictionaries.  
- Sums the `"count"` values and counts the entries.  
- Prints the total count and sum.

---

### Exercise — Using the GeoJSON API

**Task**  
Prompt for a location string, encode it into a URL query parameter, send the request to a geolocation API over HTTPS with SSL context, parse the JSON response, and extract location details.

**My code**

import urllib.request, urllib.parse  
import json, ssl  

ctx = ssl.create_default_context()  
ctx.check_hostname = False  
ctx.verify_mode = ssl.CERT_NONE  

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'  

address = input("Enter location: ")  
url = serviceurl + urllib.parse.urlencode({'q': address})  
print("Retrieving", url)  

uh = urllib.request.urlopen(url, context=ctx)  
data = uh.read().decode()  
print("Retrieved", len(data), "characters")  
info = json.loads(data)  

lat = info['features'][0]['properties']['lat']  
lon = info['features'][0]['properties']['lon']  
location = info['features'][0]['properties']['formatted']  
plus_code = info['features'][0]['properties'].get('plus_code', 'Not found')  

print("Plus code:", plus_code)

**Sample Output**  
Enter location: American University in Cairo
Retrieving http://py4e-data.dr-chuck.net/opengeo?q=American+University+in+Cairo
Retrieved 1567 characters
Plus code: 8G2H26VP+4J

**What it does**  
- Sets up an SSL context that disables certificate verification.  
- Prompts for a location input string.  
- Encodes the location as a URL query parameter.  
- Sends an HTTPS request to a geolocation API.  
- Retrieves and parses the JSON response.  
- Extracts latitude, longitude, formatted address, and optionally plus code.  
- Prints the plus code.

---

## Reflections

This chapter deepened my understanding of working with web APIs, including handling XML and JSON data formats, URL encoding, SSL context management, and parsing nested data structures. These skills are essential for integrating external data sources in AI and ML applications.