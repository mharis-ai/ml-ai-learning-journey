file = input("Enter File Name: ")

try:
    hfile = open(file)
except:
    print('No file found with name',file)
    quit()

haris = dict()
for line in hfile:
    if not line.startswith("From "):
        continue
    words = line.strip().split()
    word = words[1]
    haris[word] = haris.get(word,0)+1

bigword = None
bigcount= None
for sender,count in haris.items():
    if bigcount is None or count>bigcount:
        bigword = sender
        bigcount = count
print(bigword,bigcount)