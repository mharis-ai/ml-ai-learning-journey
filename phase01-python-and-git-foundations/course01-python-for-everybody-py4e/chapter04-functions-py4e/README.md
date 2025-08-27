# Chapter 4 — Functions

---

This chapter focused on how to define and call functions to write modular and reusable code. I learned how to group logic into callable blocks, return values from functions, and apply real logic inside user-defined methods.  
Functions make code cleaner and more scalable, which becomes important as programs grow — especially in ML pipelines where repeated steps are common.

---

### Exercise 4.6

**Task**  
Rewrite the pay computation program using a function.  
Pay the regular rate for the first 40 hours, and 1.5 times the rate for hours worked above 40.  
Use a function to calculate and return the pay based on inputs.

**My code**

hours=input("Enter Hours: ")  
rate=input("Rate Per Hour: " )  
hours=float(hours)  
rate=float(rate)  
def computepay():  
    if hours>40:  
        rp = 40*rate  
        op=(hours-40)*(rate*1.5)  
        pay=op+rp  
    else:  
        pay = hours*rate  
    return pay  
print("Pay",computepay())

**Sample Output (with overtime)**

Enter Hours: 45  
Rate Per Hour: 10.50  
Pay 498.75

**Sample Output (no overtime)**

Enter Hours: 38  
Rate Per Hour: 15  
Pay 570.0

**What it does**  
- Defines a function `computepay()` to encapsulate the pay calculation logic.  
- Checks if hours worked exceed 40 to calculate overtime pay accordingly.  
- Returns the total computed pay.  
- Prints the returned pay outside the function.

---

## Reflections

This chapter helped me shift toward reusable, structured code. Learning to wrap logic in functions lays the foundation for better design, testability, and clean separation of steps — all of which are critical in ML workflows, especially in preprocessing and evaluation stages.