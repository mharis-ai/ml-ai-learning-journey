import re

file = input("Enter File: ")
try:
    hfile = open(file)
except:
    print("File not found with name:",file)
    quit()

total = 0

for line in hfile:
    numbers = re.findall('[0-9]+', line) 
    for num in numbers:
        total += int(num)

print("Sum:", total)