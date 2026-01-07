# Create a number between 1 - 100
# ask user to guess the number
# user will guess the number
    # if correct show congrats
    # if lower show guess higher number
    # if higher show guess lower number
# also track score tries(chance)

# import random
# num = random.randint(1, 100)
# tries = 0

# while True :
#     userInput = int(input("Guess a number between 1 - 100 😁 \n"))
#     if userInput > 100 or userInput < 0 :
#         print("😭😭 Invalid Input!!! Please Try Again\n")
#         continue
#     tries = tries + 1
#     if userInput == num :
#         print(f"Congratulations!🎉 You guessed it correct in {tries} tries!\n")
#         break
#     elif userInput > num :
#         print("Ohh No! ☹️  Please Guess Lower!\n")
#     elif userInput < num :
#         print("Ohh No! ☹️  Please Guess Higher!\n")
    
# Stone Paper and Scissor

# select 
# 1. stone
# 2. paper
# 3. scissor
# computer will select 1 number
# user will select 1 number

# import random

# userScore = 0
# comScore = 0

# while True :
#     computerInp = random.randint(1, 3)
#     print(f"========================")
#     print(f"SCORE")
#     print(f"User : {userScore}       V/S         Computer : {comScore}")
#     print(f"========================")

#     userInp = int(input("Please Select any 1\nStone Paper Scissor 😁\n1. Stone 🪨\n2. Paper 📃\n3. Scissor ✂️\n========================\n : "))
#     if userInp > 3 or userInp < 0 :
#         print("😭😭 Invalid Input!!! Please Try Again\n")
#         continue
#     if userInp == 1 and computerInp == 3 :
#         userScore = userScore + 1
#         print("You won the round! 🎉 \n")
#     elif userInp == 2 and computerInp == 1 :
#         userScore = userScore + 1
#         print("You won the round! 🎉 \n")
#     elif userInp == 3 and computerInp == 2 :
#         userScore = userScore + 1
#         print("You won the round! 🎉 \n")
#     elif userInp == computerInp :
#         print("It was a draw! 🟰 \n")
#     else :
#         comScore = comScore + 1
#         print("Computer won the round! 🎉\n")
    
#     if userScore == 5 :
#         print("Congratulations! 🎉 You Won!!! 🎖️")
#         break
#     elif comScore == 5 :
#         print("Computer! Won this game! 😈👹")
#         break
    