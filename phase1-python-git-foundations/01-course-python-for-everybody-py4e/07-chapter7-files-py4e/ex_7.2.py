file = input("Enter File Name: ")
try:
    handle = open(file)
except:
    print("File not found", file)
    quit()
count=0
total=0
for line in handle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    a = line.find(":")
    b = line[a+1:].strip()
    c = float(b)
    count += 1
    total += c
    average = total/count
print("Average spam confidence:", average)