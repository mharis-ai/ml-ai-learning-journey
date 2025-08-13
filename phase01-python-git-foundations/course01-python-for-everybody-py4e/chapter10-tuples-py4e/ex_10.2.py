file = input("Enter File: ")
haris = dict()
try:
    hfile = open(file)
except:
    print("No file found with name:", file)
    quit()

for line in hfile:
    if not line.startswith('From '):
        continue
    words = line.strip().split()
    word = words[5].split(':')[0]
    haris[word] = haris.get(word,0)+1

haris = sorted(haris.items())

for hour,count in haris:
    print(hour,count)