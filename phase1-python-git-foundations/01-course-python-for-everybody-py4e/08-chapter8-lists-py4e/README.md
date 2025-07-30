# Chapter 8 — Lists

---

This chapter introduced Python lists and how they can be used to store, sort, and manage collections of data. It also demonstrated how to parse and extract specific elements from text using the split() method, as well as how to build new lists dynamically through loops and conditions.

---

### Exercise 8.4 — Building a Sorted List of Unique Words

**Task**  
Prompt for a file name, extract all lines starting with X-DSPAM-Confidence:, and compute the average of the extracted floating-point values.

**My code**

file = input("Enter File: ")
haris = list()
try:
    fh = open(file)
except:
    print("File not found", file)
    quit()
for line in fh:
    list_words = line.strip()
    words = list_words.split()
    for i in words:
        if not i in haris:
            haris.append(i)
haris.sort()
print(haris)

**What it does**  
Reads a text file, splits each line into words, appends only new words to a list, sorts the list alphabetically, and prints it.


### Exercise 8.5 — Extracting Email Senders from "From" Lines

**Task**  
Scan a file for lines that start with "From " and print the second word (the email address) from each of those lines. Count and display the total number of such lines.

**My code**

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
    words = line.split()
    email = words[1]
    count += 1
    print(email)
print("There were", count, "lines in the file with From as the first word")


**What it does**  
Opens a file, identifies lines that begin with "From ", extracts and prints the email address (second word), and keeps a running count of such lines.

---

## Reflections

This chapter helped me get comfortable working with dynamic lists, identifying patterns in text, and filtering relevant data. These list and string techniques are essential for data parsing and will continue to appear in future tasks.