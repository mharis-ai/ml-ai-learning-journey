file = input("Enter File: ")
haris = list()
try:
    fh= open(file)
except:
    print("File not found", file)
    quit()
for line in fh:
    list_words = line.strip()
    words=list_words.split()
    for i in words:
        if not i in haris:
            haris.append(i)
haris.sort()
print(haris)