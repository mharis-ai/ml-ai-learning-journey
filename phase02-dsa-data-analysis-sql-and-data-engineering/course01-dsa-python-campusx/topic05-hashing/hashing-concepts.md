# Hashing Concepts in Python – Haris

> This document provides a clear and concise overview of hashing techniques in Python, covering **all main concepts** including open addressing and chaining.  
> All concepts are explained thoroughly to ensure clarity and deep understanding.

---

## Credits
This document, including all explanations, tables, and concepts, has been **created and refined with assistance from GPT**. The content is structured for clarity, precision, and educational purposes.

---

## 1️⃣ Open Addressing (Closed Hashing)
All keys are stored directly in the array. Collisions are resolved using **probing**.

### Linear Probing
- **Formula:** `index = (h(key) + i) % size`
- **Behavior:** On collision, check the next sequential slot
- **Pros:** Simple, cache-friendly
- **Cons:** Primary clustering occurs
- **Average Time:** O(1)
- **Worst-case Time:** O(n)
- **Use case:** Small tables, low load factor (<0.7)

### Quadratic Probing
- **Formula:** `index = (h(key) + i^2) % size`
- **Behavior:** On collision, jump in squares (1, 4, 9…) to find the next slot
- **Pros:** Reduces primary clustering
- **Cons:** Secondary clustering possible; table size should be prime
- **Average Time:** O(1)
- **Worst-case Time:** O(n)
- **Use case:** Medium load factor

### Double Hashing
- **Formula:** `index = (h1(key) + i * h2(key)) % size`
- **Behavior:** Uses a second hash function to determine the step size
- **Pros:** Minimal clustering, uniform distribution
- **Cons:** Slightly more complex; requires a good second hash function
- **Average Time:** O(1)
- **Worst-case Time:** O(n)
- **Use case:** High performance under medium/high load factor

> **Note:** In open addressing, only the formula for `index` changes; rest of the code logic remains similar.

---

## 2️⃣ Chaining (Open Hashing)
Each slot stores a collection (linked list, tree, or dynamic array) of keys that hash to the same index.

### Linked List Chaining
- **Behavior:** Collided elements stored in a linked list at that slot
- **Pros:** Simple, load factor can exceed 1
- **Cons:** Extra memory for pointers, cache-unfriendly
- **Average Time:** O(1 + α)
- **Worst-case Time:** O(n)

### BST / Tree Chaining
- **Behavior:** Collisions stored in a balanced binary search tree
- **Pros:** Worst-case O(log n) search
- **Cons:** More complex, memory overhead
- **Average Time:** O(log α)
- **Worst-case Time:** O(log n)

### Dynamic Array / Vector Chaining
- **Behavior:** Collisions stored in a dynamic array
- **Pros:** Better cache locality, faster traversal
- **Cons:** Insert/remove slower than linked list
- **Average Time:** O(1 + α)
- **Worst-case Time:** O(n)

> **Note:** Chaining allows load factor >1, making it suitable for hash tables with high collisions or unpredictable sizes.

---

## 3️⃣ Comparison Table

| Hashing Type        | Subtype         | Pros                          | Cons                          | Avg       | Worst  |
|--------------------|----------------|-------------------------------|-------------------------------|-----------|--------|
| Open Addressing     | Linear         | Simple, cache-friendly        | Primary clustering            | O(1)      | O(n)   |
|                    | Quadratic      | Reduces clustering            | Secondary clustering possible | O(1)      | O(n)   |
|                    | Double Hashing | Minimal clustering            | Requires 2 hash functions    | O(1)      | O(n)   |
| Chaining            | Linked List    | Simple, load >1 allowed       | Extra memory, cache-unfriendly| O(1 + α) | O(n)   |
|                    | BST / Tree     | Worst-case O(log n)           | Complex, memory overhead      | O(log α) | O(log n)|
|                    | Dynamic Array  | Better cache locality          | Insert/remove slower          | O(1 + α) | O(n)   |

---

**This document is a complete reference for hashing concepts in Python, structured for clarity and deep conceptual understanding. Created with the guidance and refinement of GPT.**