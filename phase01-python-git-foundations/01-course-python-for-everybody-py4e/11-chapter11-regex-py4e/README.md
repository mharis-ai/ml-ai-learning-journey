# Chapter 11 — Regex

---

This chapter introduces the use of regular expressions (regex) in Python to find patterns within text data. It demonstrates how regex can extract numbers from text lines for further processing.

---

### Exercise — Regular Expressions

**Task**  
Read a file, extract all numbers from each line using regex, convert them to integers, sum them all, and print the total.

**My code**

import re

file = input("Enter File: ")  
try:  
    hfile = open(file)  
except:  
    print("File not found with name:", file)  
    quit()  

total = 0  

for line in hfile:  
    numbers = re.findall('[0-9]+', line)  
    for num in numbers:  
        total += int(num)  

print("Sum:", total)

**Sample Output**  
Enter File: regex.txt  
Sum: 385667

**What it does**  
- Prompts for a file name.  
- Opens and reads the file line by line.  
- Uses regex to find all sequences of digits in each line.  
- Converts extracted digit strings to integers.  
- Keeps a running total sum of all found numbers.  
- Prints the final sum.

---

## Reflections

This chapter helped me learn how powerful regex can be for pattern matching and extracting data from unstructured text. This is a crucial skill for parsing complex datasets and cleaning data in real-world machine learning projects.