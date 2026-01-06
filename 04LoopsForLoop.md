# 🔁 FOR Loop in Python – Complete Beginner Guide (Logic Building)

A **for loop** is used when we want to **repeat a block of code a fixed number of times** or iterate over a sequence like numbers, strings, etc.

This chapter will help you understand:
- What a for loop is
- How `range()` works
- How to use for loop with strings
- Logic-building problems using for loop

---

## 🧠 Why Do We Need Loops?

Imagine printing your name 10 times.

❌ Without loop:
```python
print("Sambhav")
print("Sambhav")
print("Sambhav")
# ... repeated again and again
````

✅ With for loop:

```python
for i in range(10):
    print("Sambhav")
```

👉 Loops make code:

* Short
* Clean
* Reusable
* Easy to manage

---

## 🔹 What is a FOR Loop?

A `for` loop repeats a block of code **for each value in a sequence**.

---

## 🔹 Syntax of FOR Loop

```python
for variable in sequence:
    code to execute
```

Example:

```python
for i in range(5):
    print(i)
```

---

## 🔢 The `range()` Function (VERY IMPORTANT)

`range()` is commonly used with `for` loop to generate numbers.

### Syntax

```python
range(start, stop, step)
```

| Parameter | Meaning                     | Default  |
| --------- | --------------------------- | -------- |
| start     | Starting value              | 0        |
| stop      | Ending value (not included) | Required |
| step      | Increment / Decrement       | 1        |

---

### Examples of `range()`

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(1, 11, 2) # 1, 3, 5, 7, 9
```

---

## 🧪 Example 1: Print Numbers from 1 to 10

```python
for i in range(1, 11):
    print(i)
```

---

## 🧪 Example 2: Print Name with Numbers

```python
for i in range(1, 11):
    print(f"{i}. Sambhav")
```

---

## 🔤 FOR Loop with Strings

Strings are sequences of characters, so we can loop over them.

---

### Method 1: Using Index

```python
name = input("Enter your name: ")

for index in range(len(name)):
    print(name[index])
```

### 🧠 Explanation

* `len(name)` gives length of string
* `index` accesses each character

---

### Method 2: Direct Character Access (Recommended)

```python
name = input("Enter your name: ")

for ch in name:
    print(ch)
```

👉 Cleaner and easier to understand.

---

## 🧠 Logic Building Questions Using FOR Loop

---

## ✅ Q1: Print "Hello" N Times

```python
n = int(input("Enter a number: "))

for i in range(n):
    print(i + 1, "Hello")
```

---

## ✅ Q2: Print Numbers from 1 to N

```python
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)
```

---

## ✅ Q3: Print Numbers from N to 1

```python
n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    print(i)
```

---

## ✅ Q4: Sum of Natural Numbers (1 to N)

Example:

```
N = 5 → 1 + 2 + 3 + 4 + 5 = 15
```

```python
n = int(input("Enter a number: "))
totalSum = 0

for i in range(1, n + 1):
    totalSum = totalSum + i

print(f"Total sum from 1 to {n} is {totalSum}")
```

---

## ✅ Q5: Factorial of a Number

Example:

```
5! = 1 × 2 × 3 × 4 × 5 = 120
```

```python
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"Factorial of {n} is {fact}")
```

---

## ✅ Q6: Sum of Even and Odd Numbers (1 to N)

```python
n = int(input("Enter a number: "))

evenSum = 0
oddSum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        evenSum = evenSum + i
    else:
        oddSum = oddSum + i

print(f"Even Sum is {evenSum} and Odd Sum is {oddSum}")
```

---

## ✅ Q7: Sum of All Factors of a Number

Example:

```
6 → Factors: 1, 2, 3, 6 → Sum = 12
```

```python
n = int(input("Enter a number: "))
factSum = 0

for i in range(1, n + 1):
    if n % i == 0:
        factSum = factSum + i

print(f"Sum of all factors: {factSum}")
```

---

## ✅ Q8: Power Calculation (a^b without **)

Example:

```
2^3 = 2 × 2 × 2 = 8
```

```python
base = int(input("Enter base: "))
expo = int(input("Enter exponent: "))

power = 1

for i in range(1, expo + 1):
    power = power * base

print(power)
```

---

## ✅ Q9: Prime Number Check

A **prime number** has exactly **2 factors**:

* 1
* The number itself

Examples: `2, 3, 5, 7, 11`

```python
n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    isPrime = True
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break

    if isPrime:
        print("Prime Number")
    else:
        print("Not Prime Number")
```

---

## ❌ Common Mistakes Students Make

❌ Wrong `range()` values
❌ Forgetting `+1` in range
❌ Confusing start and stop
❌ Infinite loops (in while)

---

## ✅ Summary

✔ `for` loop is used for fixed iterations
✔ `range()` generates numbers
✔ Strings can be looped character by character
✔ For loop is powerful for math & logic problems
✔ Helps build strong problem-solving skills

---

