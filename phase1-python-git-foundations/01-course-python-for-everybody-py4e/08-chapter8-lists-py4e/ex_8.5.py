file = input("Enter File: ")
count = 0
try:
    fh = open(file)
except:
    print("File not found", file)
    quit()
for line in fh:
    if not line.startswith("From "):
        continue
    words=line.split()
    email = words[1]
    count+=1
    print(email)
print("There were",count,"lines in the file with From as the first word")