# Chapter 2 — Variables

---

This chapter introduces how to store values using variables, accept user input, and perform basic arithmetic operations. These are essential foundations for building dynamic, interactive programs and will later support real-world data manipulation in machine learning workflows.

---

### Exercise 2.2

**Task**  
Write a program that uses `input` to prompt the user for their name and then welcomes them.

**My code**

name = input("Enter your name: ")  
print("Hello", name)

**Sample Output**

Enter your name: Haris  
Hello Haris

**What it does**  
- Prompts the user for their name and stores it in a variable.  
- Prints a custom greeting including the entered name.

---

### Exercise 2.3

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
- Prompts the user to input hours and rate per hour.  
- Converts input strings to floats for calculation.  
- Calculates gross pay by multiplying hours by rate.  
- Prints the gross pay.

---

## Reflections

This chapter helped solidify my understanding of variables, user input, and basic numeric operations — the building blocks of programming. These simple scripts taught me how data flows through a program, a pattern that mirrors how input data is passed through ML models. Each step, though basic now, is foundational for engineering intelligent systems in the future.