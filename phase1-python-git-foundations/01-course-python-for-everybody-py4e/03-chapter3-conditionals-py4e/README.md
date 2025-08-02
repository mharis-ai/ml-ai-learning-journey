# Chapter 3 — Conditionals

---

This chapter introduces how programs make decisions using conditions like `if`, `else`, and `elif`. It also touches on error handling with `try` and `except`, which helps make programs more robust when dealing with user input or unexpected values.

These control structures are foundational for logic in any intelligent system, especially in AI pipelines that rely on condition-based flows.

---

### Exercise 3.1 — Compute Gross Pay with Overtime

**Task**  
Write a program to prompt the user for hours and rate per hour. Pay the regular rate for the first 40 hours and 1.5 times the rate for hours worked above 40.

**My code**

hours = input("Enter Hours: ")  
rate = input("Enter Rate Per Hour: ")  
hours = float(hours)  
rate = float(rate)  
if hours > 40:  
    rp = 40 * rate  # regular pay  
    op = (hours - 40) * (rate * 1.5)  # overtime pay  
    pay = op + rp  
    print(pay)  
else:  
    pay = hours * rate  
    print(pay)

**Sample Output (with overtime)**

Enter Hours: 45  
Enter Rate Per Hour: 10.50  
498.75

**Sample Output (no overtime)**

Enter Hours: 38  
Enter Rate Per Hour: 15  
570.0

**What it does**  
This program checks whether the inputted hours exceed 40, then calculates pay accordingly — either using regular multiplication or adding overtime pay. This was my first program that uses real logic and branching.

---

### Exercise 3.3 — Score to Grade Converter with Error Handling

**Task**  
Write a program that prompts for a score between 0.0 and 1.0. If input is out of range or invalid, show an error. If valid, convert it to a grade using:

- ≥ 0.9 → A  
- ≥ 0.8 → B  
- ≥ 0.7 → C  
- ≥ 0.6 → D  
- < 0.6 → F

**My code**

score = input("Enter Your Score: ")  
try:  
    score = float(score)  
    if score < 0.0 or score > 1.0:  
        print("Error: Score is out of range. Please enter a value between 0.0 and 1.0.")  
    elif score >= 0.9:  
        print("Grade: A")  
    elif score >= 0.8:  
        print("Grade: B")  
    elif score >= 0.7:  
        print("Grade: C")  
    elif score >= 0.6:  
        print("Grade: D")  
    else:  
        print("Grade: F")  
except:  
    print("Error: Invalid input. Please enter a numeric value.")

**Sample Output (valid)**

Enter Your Score: 0.85  
Grade: B

**Sample Output (invalid range)**

Enter Your Score: 1.8  
Error: Score is out of range. Please enter a value between 0.0 and 1.0.

**Sample Output (non-numeric)**

Enter Your Score: hello  
Error: Invalid input. Please enter a numeric value.

**What it does**  
This program uses conditional logic to convert a score into a letter grade and also includes error handling using `try-except` to catch non-numeric values. It's an important practice in writing clean, user-safe programs.

---

## Reflections

This chapter was a major step in writing real logic-based code. I learned how to guide program flow using decisions, and how to protect input using error handling. These are core principles not only in software development, but in AI where branching logic is everywhere — from preprocessing to model selection.