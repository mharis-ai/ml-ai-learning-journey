import urllib.request,json

url = input("Enter - ")
print("Retrieving", url)
json_url = urllib.request.urlopen(url)
json_data = json_url.read()
print("Retrieved",len(json_data),"characters")

info = json.loads(json_data)
count = 0
total = 0
for item in info["comments"]:
    count += 1
    total += item["count"]
print("Count:",count)
print("Sum:", total)