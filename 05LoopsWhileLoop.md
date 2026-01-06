# 🔁 Loops in Python – While Loop, Break & Continue (Logic Building)

Loops are used when we want to **repeat a block of code** until a condition is satisfied.

In this chapter, we will focus on:
- `while` loop
- `break` statement
- `continue` statement
- Important **logic-building problems** using loops

---

## 🧠 What is a While Loop?

A `while` loop runs **as long as a condition is True**.

👉 When the condition becomes False, the loop stops automatically.

---

## 🔹 Syntax of While Loop

```python
while condition:
    code to execute
````

⚠️ **Important**

* The condition must eventually become False
* Otherwise, the loop will run forever (infinite loop)

---

## 🧪 Example 1: Print Numbers from 1 to 10

```python
a = 1

while a <= 10:
    print(a)
    a = a + 1
```

### 🔍 How it works

* `a` starts from 1
* Loop runs while `a <= 10`
* `a` increases by 1 each time
* Loop stops when `a` becomes 11

---

## 🛑 Break Statement

`break` is used to **stop the loop immediately**, even if the condition is still True.

---

### 🧪 Example: Stop Loop When Value Becomes 5

```python
a = 0

while a < 10:
    print(a + 1)
    if a == 5:
        break
    a = a + 1

print(f"This is value of {a}")
```

### 🧠 Explanation

* Loop starts normally
* When `a == 5`, `break` executes
* Loop exits instantly

---

## ⏭️ Continue Statement

`continue` is used to **skip the current iteration** and move to the next one.

---

### 🧪 Example: Skip Number 5

```python
a = 1

while a <= 10:
    if a == 5:
        a = a + 1
        continue
    print(a)
    a = a + 1
```

### 🧠 Explanation

* When `a == 5`, print is skipped
* Loop continues with next value

---

## 🔢 Logic Building with While Loop

Now let’s use `while` loop for **real logic-based problems**.

---

## 🔹 1. Print Each Digit (Reverse Order)

### Problem

Break a number into digits and print them **from last to first**.

Example:

```
145
Output:
5
4
1
```

### Code

```python
a = 145

while a > 0:
    rem = a % 10
    print(rem)
    a = a // 10
```

### 🧠 Logic

* `% 10` → gives last digit
* `// 10` → removes last digit
* Loop runs until number becomes 0

---

## 🔹 2. Sum of Digits

### Problem

Add all digits of a number
Example:

```
123 → 1 + 2 + 3 = 6
```

### Code

```python
num = int(input("Enter a number: "))
total = 0

while num > 0:
    rem = num % 10
    total = total + rem
    num = num // 10

print(f"Sum of digits is {total}")
```

---

## 🔹 3. Reverse a Number

### Problem

Reverse the digits of a number
Example:

```
123 → 321
```

### Code

```python
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(f"Reverse is {rev}")
```

---

## 🔹 4. Palindrome Number Check

### Problem

A number is palindrome if it reads the same forward and backward
Examples:

```
121 → Palindrome
1331 → Palindrome
```

### Code

```python
num = int(input("Enter a number: "))
dup = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if dup == rev:
    print(f"{dup} is Palindrome")
else:
    print(f"{dup} is not Palindrome")
```

---

## 🔹 5. Automorphic Number

### What is an Automorphic Number?

A number is **automorphic** if its **square ends with the number itself**.

Examples:

```
5² = 25
76² = 5776
```

---

### Code

```python
num = int(input("Enter a number: "))
square = num * num

temp = num
rem = 1

while temp > 0:
    rem = rem * 10
    temp = temp // 10

if square % rem == num:
    print("Number is Automorphic")
else:
    print("Number is not Automorphic")
```

---

## 🧠 How to Think While Solving Loop Problems

Ask yourself:

1. What is the **condition**?
2. What should change inside the loop?
3. When should the loop stop?
4. Do I need `break` or `continue`?

---

## ❌ Common Mistakes by Students

❌ Forgetting to update loop variable
❌ Infinite loops
❌ Wrong condition
❌ Misusing `%` and `//`

---

## ✅ Summary

✔ `while` loop runs until condition becomes False
✔ `break` stops loop immediately
✔ `continue` skips current iteration
✔ Loops are powerful for number logic problems
✔ Logic building improves problem-solving skills

---

Happy Coding 🐍💙
Keep practicing every day!

