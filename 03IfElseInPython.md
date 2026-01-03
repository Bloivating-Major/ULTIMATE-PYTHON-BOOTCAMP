````md
# 🔀 Control Flow in Python – If, Else & Logic Building

In real life, we make decisions every day.

👉 *If it is raining → take an umbrella*  
👉 *If marks are above passing → result is pass*  

Python also works in the **same decision-making way** using **if–else**.

This chapter will help you understand:
- How decisions are made in Python
- How conditions are checked
- How to build logic step by step

---

## 🧠 What is Control Flow?

**Control Flow** means:
> The order in which code is executed based on conditions.

By default, Python executes code **top to bottom**.  
But using `if–else`, we can **control** which code runs.

---

## 🔹 Why Do We Need If–Else?

Without if–else, programs cannot:
- Take decisions
- Respond to user input
- Behave differently in different situations

---

## 🔹 Syntax of If–Else

```python
if condition:
    code if condition is True
else:
    code if condition is False
````

⚠️ **Indentation is mandatory in Python**

---

## 🧪 Example 1: Voter ID Check (Basic Logic)

### Problem Statement

* If age ≥ 18 → can vote
* Else → cannot vote

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```

### 🧠 Logic Explained

* Python checks the condition `age >= 18`
* If `True` → runs `if` block
* If `False` → runs `else` block
* Only **one block executes**

---

## 🔹 If–Else with Real-Life Meaning

```python
money = int(input("Enter how much money you have: "))

atta = 40
money = money - atta

if money >= 50:
    chocolate = 20
    money = money - (chocolate * 2)

print("Money left:", money)
```

### 🧠 Thinking Process

1. Take user input
2. Perform calculation
3. Check condition
4. Update value
5. Print result

👉 This is **real logic building**

---

## 🔹 If–Elif–Else (Multiple Conditions)

When there are **more than 2 choices**, we use `elif`.

```python
if condition1:
    code
elif condition2:
    code
elif condition3:
    code
else:
    code
```

---

## 🧪 Example: Contribution Decision (Multiple Conditions)

```python
contri = int(input("Kiti paise gola jhale?: "))

if contri >= 5 and contri <= 10:
    print("Chocolate chi goli gheu")
elif contri > 10 and contri <= 50:
    print("Cadbury gheu")
elif contri > 50 and contri <= 100:
    print("Wafers ani Cupcake gheu")
elif contri > 100:
    print("Hotel madhe jevan")
else:
    print("Kahi nahi ho shakat")
```

### 🧠 How Python Evaluates This

* Conditions checked **top to bottom**
* First `True` condition executes
* Remaining conditions are skipped

---

## 🔹 Comparison + Logical Operators in If–Else

```python
a = int(input("Enter number A: "))
b = int(input("Enter number B: "))

if a > b:
    print("A is greater")
else:
    print("B is greater")
```

### Operators Used

* `>` → comparison
* `if–else` → decision

---

## 🔹 Case Sensitivity Problem (Important Concept)

### ❌ Problem

```python
gender = input("Enter gender: ")

if gender == "m":
    print("Hello Sir")
```

Input: `M` → ❌ fails

---

### ✅ Solution (Using OR)

```python
if gender == "m" or gender == "M":
    print("Hello Sir")
elif gender == "f" or gender == "F":
    print("Hello Mam")
else:
    print("Invalid Input")
```

---

### ✅ Better Solution (Best Practice)

```python
gender = input("Enter gender: ").lower()

if gender == "m":
    print("Hello Sir")
elif gender == "f":
    print("Hello Mam")
else:
    print("Invalid Input")
```

---

## 🔹 Even or Odd Logic (Classic Interview Question)

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

### 🧠 Logic

* `%` gives remainder
* Even → remainder = 0

---

## 🔹 Voting Eligibility with Future Calculation

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    years = 18 - age
    print(f"{name}, you will be eligible in {years} years")
```

👉 Shows **decision + calculation**

---

## 🔹 Day Number to Day Name (Mapping Logic)

```python
day = int(input("Enter day number (1–7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")
```

---

## 🔹 Finding Greatest Among Three Numbers

```python
a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print("All are equal")
elif a == b or b == c or c == a:
    print("Any two are equal")
elif a > b and a > c:
    print("A is greatest")
elif b > a and b > c:
    print("B is greatest")
else:
    print("C is greatest")
```

👉 Combines:

* Comparison
* Logical operators
* Multiple decisions

---

## 🔹 Leap Year Logic (Very Important)

```python
year = int(input("Enter year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Leap Year")
elif year % 100 != 0 and year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

---

## 🔹 Vowel or Consonant (Membership Operator)

```python
char = input("Enter a character: ")

if char in "aeiouAEIOU":
    print("Vowel")
elif char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
    print("Consonant")
else:
    print("Invalid Input")
```

---

## 🧠 How to Think While Writing If–Else (VERY IMPORTANT)

Ask these questions:

1. What is the **input**?
2. What is the **condition**?
3. What happens if **True**?
4. What happens if **False**?
5. Do I need multiple conditions?

---

## ❌ Common Student Mistakes

❌ Using `=` instead of `==`
❌ Forgetting indentation
❌ Wrong logical conditions
❌ Not handling invalid input

---

## ✅ Summary

✔ `if` checks condition
✔ `else` handles false case
✔ `elif` handles multiple cases
✔ Conditions use comparison & logical operators
✔ Decision making is the heart of programming

---
Keep practicing 🐍💙
Happy Coding!