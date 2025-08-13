# Chapter 8 — Lists

---

This chapter introduced Python lists and how they can be used to store, sort, and manage collections of data. It also demonstrated how to parse and extract specific elements from text using the split() method, as well as how to build new lists dynamically through loops and conditions.

---

### Exercise 8.4

**Task**  
Prompt for a file name, extract all unique words from the file, sort them, and print them.

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

**Sample Output**  
Enter File: romeo.txt  
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

**What it does**  
- Opens a text file safely.  
- Reads the file line by line.  
- Splits each line into individual words.  
- Adds unique words to a list, ignoring duplicates.  
- Sorts the list of unique words alphabetically.  
- Prints the sorted list.

---

### Exercise 8.5

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

**Sample Output**  
Enter File: mbox-short.txt  
stephen.marquard@uct.ac.za  
louis@media.berkeley.edu  
zqian@umich.edu  
rjlowe@iupui.edu  
...  
There were 27 lines in the file with From as the first word

**What it does**  
- Opens a file safely.  
- Reads through each line, filtering lines starting with "From ".  
- Extracts and prints the second word (email address) from those lines.  
- Counts and prints the total number of such lines.

---

## Reflections

This chapter helped me get comfortable working with dynamic lists, identifying patterns in text, and filtering relevant data. These list and string techniques are essential for data parsing and will continue to appear in future tasks.