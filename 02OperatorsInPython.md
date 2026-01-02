````md
# 🧮 Python Operators – Complete Guide (Arithmetic, Assignment, Comparison & Logical)

Operators are **special symbols** used to perform operations on values and variables.

In Python, operators help us:
- Do calculations
- Assign values
- Compare values
- Make decisions using logic

---

## 📚 Types of Operators Covered

1. Arithmetic Operators  
2. Assignment Operators  
3. Comparison Operators  
4. Logical Operators  

---

# ➗ 1. Arithmetic Operators

Arithmetic operators are used to perform **mathematical operations**.

---

## 🔹 List of Arithmetic Operators

| Operator | Name | Example |
|--------|------|--------|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `%` | Modulus (Remainder) | `10 % 3` |
| `//` | Floor Division | `10 // 3` |
| `**` | Power (Exponent) | `2 ** 3` |

---

## 🔹 Examples

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
````

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

## 📝 Important Notes

* `/` always gives **float**
* `//` removes decimal part
* `%` gives remainder
* `**` is used for power

---

# 📝 2. Assignment Operators

Assignment operators are used to **assign or update values** in variables.

---

## 🔹 Basic Assignment

```python
x = 10
```

---

## 🔹 List of Assignment Operators

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

## 🔹 Examples

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

### Output

```text
15
12
24
6.0
```

---

# ⚖️ 3. Comparison Operators

Comparison operators are used to **compare two values**.
They always return **True or False**.

---

## 🔹 List of Comparison Operators

| Operator | Meaning               | Example  |
| -------- | --------------------- | -------- |
| `==`     | Equal to              | `5 == 5` |
| `!=`     | Not equal             | `5 != 3` |
| `>`      | Greater than          | `10 > 5` |
| `<`      | Less than             | `3 < 7`  |
| `>=`     | Greater than or equal | `5 >= 5` |
| `<=`     | Less than or equal    | `4 <= 6` |

---

## 🔹 Examples

```python
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

### Output

```text
False
True
True
False
True
False
```

---

## 🧠 Real-Life Example

```python
age = 18

print(age >= 18)
```

Output:

```text
True
```

👉 Used in **conditions and decision making**

---

# 🧠 4. Logical Operators

Logical operators are used to **combine conditions**.

They mostly work with **True / False** values.

---

## 🔹 List of Logical Operators

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be True        |
| `or`     | At least one condition must be True |
| `not`    | Reverses the result                 |

---

## 🔹 Logical `and`

```python
age = 20
has_id = True

print(age >= 18 and has_id)
```

Output:

```text
True
```

---

## 🔹 Logical `or`

```python
marks = 35
sports_quota = True

print(marks >= 40 or sports_quota)
```

Output:

```text
True
```

---

## 🔹 Logical `not`

```python
is_logged_in = False

print(not is_logged_in)
```

Output:

```text
True
```

---

## 🔁 Truth Table (Easy Understanding)

### AND

| A     | B     | Result |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | False  |
| False | True  | False  |
| False | False | False  |

### OR

| A     | B     | Result |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

# 🧪 Practice Questions

1. What is the output?

```python
print(5 > 3 and 10 < 5)
```

2. Predict the output:

```python
x = 10
y = 20
print(x == 10 or y == 5)
```

3. Find output:

```python
print(not (5 == 5))
```

---

# ✅ Final Summary

✔ Arithmetic → calculations
✔ Assignment → store & update values
✔ Comparison → compare values
✔ Logical → decision making

👉 These operators are **used everywhere** in Python.

---

## 🚀 What’s Next?

Next topic:

* Conditional Statements (`if`, `elif`, `else`)
* Flow control
* Real decision-based programs

Keep practicing 🐍💙
Happy Coding!
