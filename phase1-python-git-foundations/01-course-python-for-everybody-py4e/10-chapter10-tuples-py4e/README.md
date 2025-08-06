# Chapter 10  — Tuples

---

This chapter introduces tuples and how they can be used with dictionaries for sorting data. The following program counts how many messages were sent during each hour of the day.

---

### Exercise 10.2 — Count Emails by Hour

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

**What it does**  
- Prompts for a file name 
- Opens and reads the file  
- Filters lines starting with `From`  
- Extracts the hour from the time field
- Uses a dictionary to count how many messages appear in each hour
- Sorts the dictionary by hour using tuples
- Prints the hour and its corresponding count

---

## Reflections

This script shows how dictionaries and tuples work together to organize and sort data — a useful pattern for time-based analysis.