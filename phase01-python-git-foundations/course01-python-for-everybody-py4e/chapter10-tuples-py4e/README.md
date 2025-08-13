# Chapter 10  — Tuples

---

This chapter introduces tuples and how they can be used with dictionaries for sorting data. The following program counts how many messages were sent during each hour of the day.

---

### Exercise 10.2

**Task**  
Read a file, extract the hour from lines starting with From , count how many times each hour appears, and print the results sorted by hour.

**My code**

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
    haris[word] = haris.get(word, 0) + 1  

haris = sorted(haris.items())  

for hour, count in haris:  
    print(hour, count)

**Sample Output**  
Enter File: mbox-short.txt  
04 3  
06 1  
07 1  
09 2  
10 3  
11 6  
14 1  
15 2  
16 4  
17 2  
18 1  
19 1  

**What it does**  
- Prompts for a file name.  
- Opens and reads the file line by line.  
- Filters lines starting with `"From "`.  
- Extracts the hour part from the timestamp.  
- Counts how many messages occur in each hour using a dictionary.  
- Sorts the dictionary items by hour using tuples.  
- Prints each hour and the corresponding count.

---

## Reflections

This script shows how dictionaries and tuples work together to organize and sort data — a useful pattern for time-based analysis.