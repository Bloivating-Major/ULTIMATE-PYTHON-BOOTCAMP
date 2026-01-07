# 🎮 Python Mini Projects – Game Day Session

Today’s session was all about **applying Python fundamentals** to build **real, interactive games**.  
Students learned how basic concepts like **loops, conditions, input handling, and randomness** come together to create fun programs.

In this session, we built **two complete terminal-based games** 👇

---

## 🧠 Concepts Used in Today’s Session

Before jumping into games, let’s understand what concepts we applied:

- `while` loop (infinite loops with control)
- `if`, `elif`, `else` (decision making)
- `break` and `continue`
- User input handling
- Score tracking using variables
- `random` module
- Logic building & flow control

---

# 🎯 Game 01: Guess the Number Game

### 📌 Game Idea
- Computer randomly selects a number between **1 and 100**
- User keeps guessing the number
- Program gives hints:
  - Guess higher ⬆️
  - Guess lower ⬇️
- Game ends when the user guesses correctly
- Number of attempts (tries) is tracked

---

## 🔹 Rules of the Game

1. User must enter a number between **1 and 100**
2. Invalid inputs are rejected
3. Every valid guess increases the **try count**
4. Game stops only when the correct number is guessed

---

## 🧩 Logic Flow (How the Game Works)

1. Generate a random number
2. Start an infinite loop
3. Take user input
4. Validate input range
5. Compare guess with actual number
6. Give hints
7. Stop when guessed correctly

---

## 🧪 Code: Guess the Number Game

```python
import random

num = random.randint(1, 100)
tries = 0

while True:
    userInput = int(input("Guess a number between 1 - 100 😁\n"))

    if userInput > 100 or userInput < 1:
        print("😭 Invalid Input! Please try again.\n")
        continue

    tries += 1

    if userInput == num:
        print(f"Congratulations! 🎉 You guessed it in {tries} tries!\n")
        break
    elif userInput > num:
        print("Ohh No! ☹️ Guess a LOWER number!\n")
    else:
        print("Ohh No! ☹️ Guess a HIGHER number!\n")
````

---

## 🧠 What Students Learned from This Game

✔ Using `random.randint()`
✔ Infinite loops using `while True`
✔ Input validation
✔ Counting attempts
✔ Real-time feedback logic

---

# ✊✋✌️ Game 02: Stone Paper Scissors

### 📌 Game Idea

* User plays **Stone–Paper–Scissors** against the computer
* First to score **5 points** wins the game
* Scores are displayed after every round

---

## 🔹 Game Rules

| Choice     | Number |
| ---------- | ------ |
| Stone 🪨   | 1      |
| Paper 📃   | 2      |
| Scissor ✂️ | 3      |

* Stone beats Scissor
* Paper beats Stone
* Scissor beats Paper

---

## 🧩 Logic Flow

1. Initialize user & computer scores
2. Computer picks a random choice
3. User enters a choice
4. Validate user input
5. Decide winner of the round
6. Update scores
7. Stop game when any score reaches 5

---

## 🧪 Code: Stone Paper Scissors Game

```python
import random

userScore = 0
comScore = 0

while True:
    computerInp = random.randint(1, 3)

    print("========================")
    print("SCORE")
    print(f"User : {userScore}   V/S   Computer : {comScore}")
    print("========================")

    userInp = int(input(
        "Choose one:\n"
        "1. Stone 🪨\n"
        "2. Paper 📃\n"
        "3. Scissor ✂️\n"
        ": "
    ))

    if userInp < 1 or userInp > 3:
        print("😭 Invalid Input! Try again.\n")
        continue

    if userInp == 1 and computerInp == 3:
        userScore += 1
        print("You won the round! 🎉\n")
    elif userInp == 2 and computerInp == 1:
        userScore += 1
        print("You won the round! 🎉\n")
    elif userInp == 3 and computerInp == 2:
        userScore += 1
        print("You won the round! 🎉\n")
    elif userInp == computerInp:
        print("It's a draw! 🟰\n")
    else:
        comScore += 1
        print("Computer won the round! 😈\n")

    if userScore == 5:
        print("Congratulations! 🎖️ You WON the game!")
        break
    elif comScore == 5:
        print("Computer won the game! 👹")
        break
```

---

## 🧠 What Students Learned from This Game

✔ Score tracking
✔ Using loops for repeated rounds
✔ Game-ending conditions
✔ Combining multiple conditions
✔ Writing real-world logic

---

## 🎓 Key Takeaways from Today’s Session

* Programming is about **thinking**, not memorizing
* Small concepts combine to create big programs
* Games are the best way to learn logic
* Confidence grows by building things 🚀

---

## 🚀 What’s Next?

In upcoming sessions, we will:

* Improve these games
* Add difficulty levels
* Introduce functions
* Build more mini projects

---

**Keep practicing. Keep building. Keep winning. 🐍💙**
Happy Coding!