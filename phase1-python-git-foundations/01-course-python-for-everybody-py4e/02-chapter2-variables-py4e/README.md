# Chapter 2 — Variables

---

This chapter introduces how to store values using variables, accept user input, and perform basic arithmetic operations. These are essential foundations for building dynamic, interactive programs and will later support real-world data manipulation in machine learning workflows.

---

### Exercise 2.2 — Welcome Message

**Task**  
Write a program that uses `input` to prompt the user for their name and then welcomes them.

**My code**

name = input("Enter your name: ")  
print("Hello", name)

**Sample Output**

Enter your name: Haris  
Hello Haris

**What it does**  
This simple program demonstrates string input and output. It uses a variable to store the user's name and prints a custom greeting, showing how user data can be captured and reused inside a program.

---

### Exercise 2.3 — Compute Gross Pay from Input

**Task**  
Write a program to prompt the user for hours and rate per hour to compute gross pay.

**My code**

hours = input("Enter Hours: ")  
rate = input("Enter Rate Per Hour: ")  
hours = float(hours)  
rate = float(rate)  
pay = hours * rate  
print("Gross Pay:", pay)

**Sample Output**

Enter Hours: 35  
Enter Rate Per Hour: 2.75  
Gross Pay: 96.25

**What it does**  
This program accepts numeric input, converts it to float, calculates gross pay, and displays the result. It practices both arithmetic expressions and type conversion — skills that will be reused often in real data processing and AI pipelines.

---

## Reflections

This chapter helped solidify my understanding of variables, user input, and basic numeric operations — the building blocks of programming. These simple scripts taught me how data flows through a program, a pattern that mirrors how input data is passed through ML models. Each step, though basic now, is foundational for engineering intelligent systems in the future.
