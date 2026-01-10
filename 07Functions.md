# 🧩 Functions in Python – Complete Beginner to Intermediate Guide

In programming, **functions** help us write **clean, reusable, and organized code**.

Instead of writing the same code again and again, we write it **once inside a function** and reuse it whenever needed.

---

## 🧠 Why Do We Need Functions?

### ❌ Without Functions (Code Repetition)

```python
a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))
print(a + b)

c = int(input("Enter a number 1: "))
d = int(input("Enter a number 2: "))
print(c + d)
```

Problems:

* Repeated code
* Hard to maintain
* Not scalable

---

### ✅ With Functions (Reusable Code)

```python
def sumOfTwoNum(a, b):
    print(a + b)

sumOfTwoNum(10, 20)
sumOfTwoNum(5, 7)
```

👉 Write once, use many times.

---

## 🔹 What is a Function?

A **function** is a block of code that:

* Has a **name**
* Performs a **specific task**
* Can be **called multiple times**

---

## 🔹 Syntax of a Function

```python
def function_name(parameters):
    code block
```

* `def` → keyword to define function
* `function_name` → name of function
* `parameters` → inputs to function
* indentation → mandatory

---

## 🧪 Simple Function Example

```python
def greet():
    print("Hello, Welcome to Python!")
```

### Calling the Function

```python
greet()
greet()
```

---

## 🔹 Function with Parameters

Parameters allow functions to accept input.

```python
def sumOfTwoNum(a, b):
    print(a + b)

sumOfTwoNum(4, 6)
sumOfTwoNum(10, 20)
```

### 🧠 Explanation

* `a` and `b` are parameters
* Values passed during function call are arguments

---

## 🔹 Positional Arguments

Order matters in positional arguments.

```python
def show(a, b):
    print(a, b)

show(10, 20)   # a = 10, b = 20
```

---

## 🔹 Keyword Arguments (kwargs-style calling)

Order does **not** matter.

```python
def show(a, b):
    print(a, b)

show(b=4, a=6)
```

👉 Much safer and readable.

---

## 🔹 Default Parameters

Default values are used if no argument is passed.

```python
def greet(name="Student"):
    print(f"Hello {name}")

greet()
greet("Sambhav")
```

---

## 🔹 Return Statement

`return` sends a value back from the function.

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
```

### Difference Between `print` and `return`

| print            | return            |
| ---------------- | ----------------- |
| Displays output  | Sends value       |
| Cannot be reused | Can be reused     |
| Ends there       | Continues program |

---

## 🔹 Function Returning Multiple Values

```python
def calculate(a, b):
    return a + b, a - b, a * b

sum1, diff, prod = calculate(10, 5)
print(sum1, diff, prod)
```

---

## 🔹 Variable Scope (VERY IMPORTANT)

### Local Variable

Defined inside function → usable only inside

```python
def demo():
    x = 10
    print(x)
```

---

### Global Variable

Defined outside function → accessible everywhere

```python
x = 20

def demo():
    print(x)
```

---

## 🔹 `*args` (Multiple Positional Arguments)

Used when number of arguments is unknown.

```python
def totalSum(*args):
    total = 0
    for i in args:
        total += i
    return total

print(totalSum(1, 2, 3))
print(totalSum(10, 20, 30, 40))
```

👉 `args` is a tuple.

---

## 🔹 `**kwargs` (Multiple Keyword Arguments)

Used for key-value pairs.

```python
def studentInfo(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

studentInfo(name="Sambhav", age=21, course="Python")
```

👉 `kwargs` is a dictionary.

---

## 🔹 Combining args and kwargs

```python
def demo(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

demo(1, 2, 3, 4, name="Python", level="Beginner")
```

---

## 🔹 Function Calling Another Function

```python
def square(x):
    return x * x

def cube(y):
    return square(y) * y

print(cube(3))
```

---

## 🔹 Real-Life Example: Calculator Function

```python
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid Operator"

print(calculator(10, 5, "+"))
```

---

## ❌ Common Mistakes Students Make

❌ Forgetting indentation
❌ Using print instead of return
❌ Not calling the function
❌ Confusing parameters and arguments
❌ Scope confusion

---

## 🧠 How to Think While Writing Functions

Ask yourself:

1. What task is repeating?
2. What input does it need?
3. What output should it give?
4. Should it return a value?

---

## ✅ Summary

✔ Functions reduce repetition
✔ Improve readability
✔ Make code reusable
✔ Support arguments & returns
✔ `args` and `kwargs` handle flexibility

---

Keep practicing 🐍💙
Happy Coding!
