# Chapter 9  — Dictionaries

---

This chapter covers dictionary-based counting and identifying maximum values from text data.

---

### Exercise 9.4

**Task**  
Read a file, extract email senders from `From` lines, and print the one with the highest count.

**My code**

file = input("Enter File Name: ")  

try:  
    hfile = open(file)  
except:  
    print('No file found with name', file)  
    quit()  

haris = dict()  
for line in hfile:  
    if not line.startswith("From "):  
        continue  
    words = line.strip().split()  
    word = words[1]  
    haris[word] = haris.get(word, 0) + 1  

bigword = None  
bigcount = None  
for sender, count in haris.items():  
    if bigcount is None or count > bigcount:  
        bigword = sender  
        bigcount = count  

print(bigword, bigcount)

**Sample Output**  
Enter File Name: mbox-short.txt  
cwen@iupui.edu 5

**What it does**  
- Prompts for a file name.  
- Opens and reads the file line by line.  
- Filters lines that start with `"From "`.  
- Extracts sender email addresses.  
- Uses a dictionary to count occurrences of each sender.  
- Finds and prints the email address with the highest count.

---

## Reflections

Simple use of dictionaries for counting and finding a max value — useful pattern for real data analysis.