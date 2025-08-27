# Chapter 7 — Files

---

This chapter introduced how to work with external files using Python. It covered reading files line by line, applying conditional logic to parse relevant data, handling errors using try and except, and performing calculations using extracted values.

---

### Exercise 7.2

**Task**  
Prompt for a file name, extract all lines starting with X-DSPAM-Confidence:, and compute the average of the extracted floating-point values.

**My code**

file = input("Enter File Name: ")  
try:  
    handle = open(file)  
except:  
    print("File not found", file)  
    quit()  
count = 0  
total = 0  
for line in handle:  
    if not line.startswith("X-DSPAM-Confidence:"):  
        continue  
    a = line.find(":")  
    b = line[a+1:].strip()  
    c = float(b)  
    count += 1  
    total += c  
    average = total / count  
print("Average spam confidence:", average)

**Sample Output**  
Enter File Name: mbox-short.txt  
Average spam confidence: 0.7507185185185187

**What it does**  
- Prompts for a file name and attempts to open it safely.  
- Reads the file line by line.  
- Filters lines that start with "X-DSPAM-Confidence:".  
- Extracts and converts the confidence value to float.  
- Keeps count and sum of these values.  
- Calculates and prints the average spam confidence.  
- Handles file-not-found errors gracefully with try/except.

---

## Reflections

This chapter helped me bring together multiple core skills — reading files, parsing strings, handling exceptions, and computing summary statistics. These are foundational tools I’ll build on in later chapters and real-world ML tasks.