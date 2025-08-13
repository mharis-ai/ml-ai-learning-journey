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