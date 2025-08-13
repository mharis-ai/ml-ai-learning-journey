# Chapter 5 — Iterations

---

This chapter focused on writing loops that repeatedly execute a block of code. I practiced using `while` loops, handling input inside loops, and applying conditional logic to track values like maximum and minimum.

The main exercise demonstrated how to collect an unknown number of inputs and dynamically compute the largest and smallest values entered, using logic and flow control.

---

### Exercise 5.2

**Task**  
Write a program that repeatedly prompts the user for integers until the user types "done".  
Handle any bad input using `try`/`except`, and compute the largest and smallest numbers entered.

**My code**

largest = None  
smallest = None  
while True:  
    integers = input("Enter Integers: ")  
    if integers == "done":  
        break  
    try:  
        integers = int(integers)  
    except:  
        print("Invalid input")  
        continue  
    if largest is None or integers > largest:  
        largest = integers  
    if smallest is None or integers < smallest:  
        smallest = integers  
print("Maximum is", largest)  
print("Minimum is", smallest)

**Sample Output**

Enter Integers: 8  
Enter Integers: 15  
Enter Integers: abc  
Invalid input  
Enter Integers: 3  
Enter Integers: done  
Maximum is 15  
Minimum is 3

**What it does**  
- Initializes `largest` and `smallest` as `None`.  
- Continuously prompts the user for input until `"done"` is entered.  
- Converts valid inputs to integers, ignoring invalid inputs with a message.  
- Updates the largest and smallest values dynamically.  
- Prints the maximum and minimum after termination.

---

## Reflections

This chapter gave me hands-on practice with input validation, loop control, and dynamic value tracking — all crucial skills for tasks like parsing datasets, processing logs, and filtering inputs in real-world ML pipelines.