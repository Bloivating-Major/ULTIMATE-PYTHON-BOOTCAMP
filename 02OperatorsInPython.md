````md
# ➗ Arithmetic & Assignment Operators in Python

Operators are symbols that are used to **perform operations** on values and variables.

In this lesson, we will learn:
- Arithmetic Operators
- Assignment Operators
- Simple examples for easy understanding

---

## 🧮 Arithmetic Operators

Arithmetic operators are used to perform **mathematical calculations**.

### List of Arithmetic Operators

| Operator | Name | Example |
|--------|------|--------|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `%` | Modulus | `10 % 3` |
| `//` | Floor Division | `10 // 3` |
| `**` | Exponent (Power) | `2 ** 3` |

---

### Examples

```python
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulus
print(a // b)  # Floor Division
print(a ** b)  # Power
````

---

### Output

```text
13
7
30
3.3333333333333335
1
3
1000
```

---

### Important Notes

* `/` always returns a **float**
* `//` removes decimal part
* `%` gives the **remainder**
* `**` is used for power

---

## 📝 Assignment Operators

Assignment operators are used to **assign values to variables**.

---

### Basic Assignment

```python
x = 10
```

---

### List of Assignment Operators

| Operator | Example   | Meaning      |
| -------- | --------- | ------------ |
| `=`      | `x = 5`   | Assign value |
| `+=`     | `x += 2`  | `x = x + 2`  |
| `-=`     | `x -= 2`  | `x = x - 2`  |
| `*=`     | `x *= 2`  | `x = x * 2`  |
| `/=`     | `x /= 2`  | `x = x / 2`  |
| `%=`     | `x %= 2`  | `x = x % 2`  |
| `//=`    | `x //= 2` | `x = x // 2` |
| `**=`    | `x **= 2` | `x = x ** 2` |

---

### Examples

```python
x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)
```

---

### Output

```text
15
12
24
6.0
```

---

## 🧠 Real-Life Example

```python
balance = 1000

balance += 500   # deposit
balance -= 200   # withdraw

print("Final Balance:", balance)
```

---

## 🧪 Practice Questions

1. What is the output of:

```python
print(10 // 4)
```

2. Find the remainder when `25` is divided by `4`.

3. Predict the output:

```python
x = 5
x **= 3
print(x)
```

---

## ✅ Summary

✔ Arithmetic operators perform calculations
✔ Assignment operators update variable values
✔ Python code becomes shorter and cleaner
✔ Used in almost every program

Keep practicing 🐍💙
Happy Coding!