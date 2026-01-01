````md
# 🔹 Module 01: Basics of Python

Welcome to **Module 01** of the **Ultimate Python Bootcamp**.  
In this module, we will build a **strong foundation** in Python by learning how Python code is written, structured, and executed.

---

## 🧠 Topics Covered

- Comments & Code Structure  
- Variables & Data Types  
- Naming Conventions  
- Strings & Type Conversion  
- Input Statement in Python  

---

## 📝 1. Comments & Code Structure

### What are Comments?
Comments are **notes written inside the code** to explain what the code is doing.  
Python **ignores comments** while running the program.

### Types of Comments

#### 🔹 Single-line Comment
```python
# This is a single-line comment
print("Hello Python")
````

---

#### 🔹 Multi-line Comment

Python does not have official multi-line comments, but we use:

```python
"""
This is a multi-line comment
Used for documentation
"""
print("Learning Python")
```

---

### Basic Code Structure

A Python program:

* Is written **line by line**
* Does **not use semicolons**
* Uses **indentation** instead of brackets `{}`

```python
if True:
    print("Indentation is important")
```

---

## 🧮 2. Variables & Data Types

### What is a Variable?

A variable is used to **store data** in memory.

```python
age = 21
name = "Python"
```

---

### Common Data Types in Python

| Data Type | Example         |
| --------- | --------------- |
| int       | `10`, `-5`      |
| float     | `3.14`, `2.5`   |
| str       | `"Hello"`       |
| bool      | `True`, `False` |

---

### Example

```python
age = 20
price = 99.99
language = "Python"
is_easy = True
```

Python automatically detects the data type.

---

## 🏷️ 3. Naming Conventions

Naming conventions make code **clean and readable**.

### Rules for Variable Names

✅ Can contain letters, numbers, underscore
❌ Cannot start with a number
❌ Cannot use spaces
❌ Cannot use keywords

---

### Good vs Bad Names

✅ Good:

```python
user_name = "Sambhav"
total_marks = 450
```

❌ Bad:

```python
1name = "Error"
total marks = 500
```

---

### Python Style (Best Practice)

* Use **snake_case**
* Use **meaningful names**

---

## 🔤 4. Strings & Type Conversion

### What is a String?

A string is a **sequence of characters**.

```python
name = "Python"
message = 'Welcome'
```

---

### String Operations

```python
print(name.upper())
print(name.lower())
print(len(name))
```

---

### Type Conversion

Type conversion means **changing one data type into another**.

```python
age = "20"
new_age = int(age)
```

---

### Common Conversions

```python
int("10")      # string → int
float("3.5")  # string → float
str(100)      # int → string
```

---

## ⌨️ 5. Input Statement in Python

### What is Input?

The `input()` function is used to **take input from the user**.

```python
name = input("Enter your name: ")
print(name)
```

---

### Input Always Returns String

```python
age = input("Enter your age: ")
print(type(age))  # str
```

---

### Converting Input

```python
age = int(input("Enter your age: "))
print(age + 1)
```

---

## 🧪 Practice Example

```python
name = input("Enter your name: ")
year = int(input("Enter your birth year: "))

age = 2025 - year
print("Hello", name)
print("Your age is", age)
```

---

Keep practicing 🚀
Happy Coding 🐍💙