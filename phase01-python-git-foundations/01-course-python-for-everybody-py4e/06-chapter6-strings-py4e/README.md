# Chapter 6 — Strings

---

This chapter covered how to manipulate strings using indexing, slicing, looping, and built-in string methods. It also introduced techniques for parsing and extracting values from structured strings.

---

### Exercise 6.5

**Task**  
Extracting a Number from Text

**My code**

text = "X-DSPAM-Confidence:    0.8475"  
a = text.find(':')  
b = text[a+1:].strip()  
c = float(b)  
print(c)

**Sample Output**  
0.8475

**What it does**  
- Finds the position of the colon in the string.  
- Extracts the substring after the colon and removes leading/trailing spaces.  
- Converts the extracted substring to a float.  
- Prints the floating-point number.

---

## Reflections

This exercise helped me practice string slicing and method chaining. It’s a small example of how structured data can be parsed using just a few built-in string tools — something I’ll apply often later when reading files and processing real-world data.