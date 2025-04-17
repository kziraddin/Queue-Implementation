# Queue Data Structure Implementations in Python

This project demonstrates how to implement the **Queue** data structure using three different approaches in Python:

1. Dynamic Arrays (Python lists)
2. `deque` from `collections` module
3. Singly Linked List (custom implementation)

---

## 📌 Features

- Basic queue operations: `enqueue`, `dequeue`, `peek`, `isEmpty`, and `display`
- Interactive menu-driven CLI to test the linked list implementation
- Modular and object-oriented design

---

## 🧠 Implementations

### 1. `dynamicArrayQueue`  
Implements queue using Python's built-in list.

- Pros: Simple, built-in
- Cons: `dequeue` is O(n) due to shifting of elements

### 2. `doubleEndedQueue`  
Uses Python’s `collections.deque` for efficient O(1) operations.

- Pros: Fast and reliable
- Cons: Less customizable than a custom linked list

### 3. `linkedListQueue`  
Implements queue using a custom **singly linked list**.

- Pros: Good for learning and customizing
- Cons: Slightly more complex

---

## 📟 How to Use

Run the script directly from the terminal:

```bash
python3 queues.py
```

**You’ll see a menu like:**
- Press q to QUIT.

- Press 1 to ADD value to the queue.
- Press 2 to POP value from the queue.
- Press 3 to print PEEK value from queue.

## 📂 File Structure
```bash
queues.py   # Main script containing all 3 queue implementations and CLI
```

## ✅ Sample Output
```bash
Press 1 to ADD value to the queue.
>>> 1
Enter value to add. >> 13
QUEUE:  [13]

Press 2 to POP value from the queue.
>>> 2
QUEUE:  []

Press 3 to print PEEK value from queue.
>>> 3
QUEUE is Empty.
```
## 👨‍💻 Author
Developed by Ziraddin — passionate about learning data structures and building projects in Python.

## DEMO VIDEO

https://github.com/user-attachments/assets/55bdc47d-5685-4681-8408-06c5c909640f




