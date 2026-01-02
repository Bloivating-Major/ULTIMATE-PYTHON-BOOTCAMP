# Question 01 Compare two numbers
# Take two user inputs and determine
# which number is greater or if they're
# equal.

# a = int(input("Please enter first number : "))
# b = int(input("Please enter second number : "))

# if a == b :
#     print(f"{a} is equal to {b}")
# elif a > b :
#     print(f"{a} is greater than {b}")
# else : 
#     print(f"{b} is greater than {a}")


# Question No 2 Greet By Gender
# Accept a gender input
# (m or f) and print a greeting
# "hello sir Happy new year" or 
# "hello mam Happy new year"

# gender = input("Please enter your gender : ")
# if gender == "m" :
#     print("Hello Sir, Happy New Year!")
# elif gender == "f" :
#     print("Hello Mam, Happy New Year!")
# else :
#     print("Invalid Input")

# Questoin No 3
# Make the gender check case insensitive
# ("m", "M", "f", "F") 
# if input is invalid then print invalid input

# gender = input("Please enter your gender : ")

# if gender == "m" or gender == "M" :
#     print("Hello Sir, Happy New Year!")
# elif gender == "f" or gender == "F" : 
#     print("Hello Mam, Happy New Year!")
# else :
#     print("Invalid Input")

# Question 04 
# Even or Odd checker

# num = int(input("Please enter a number : "))

# if num % 2 == 0 :
#     print(f"{num} is Even Number")
# else :
#     print(f"{num} is Odd Number")

# Question 05
# Voting Eligiblity
# Take input and ask user to enter 
# name and age and if age >= 18
# print "eligible to vote" if not
# print "Name you will become eligible to vote in X years!"

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))

# if age >= 18 :
#     print("You are eligible to vote!")
# else :
#     rem = 18 - age
#     print(f"{name} you will become eligible to vote in {rem} years!")

# Question 06
# Day Number to day name
# Input a integer from user
# Which day will be there on that given integer

# day = int(input("Enter a number between 1 to 7 : "))

# if day == 1 :
#     print("Today is Monday")
# elif day == 2:
#     print("Today is Tuesday")
# elif day == 3 : 
#     print("Today is Wednesday")
# elif day == 4 :
#     print("Today is Thursday")
# elif day == 5 :
#     print("Today is Friday")
# elif day == 6 :
#     print("Today is Saturday")
# elif day == 7 :
#     print("Today is Sunday")
# else :
#     print("Invalid Day")

# Question No 7
# Take 3 numbers int as input from user
# and find the greatest among them
# all input are equal => all input are equal
# any two input are equal => 2 input are equal
# if no input is equal => print the greater number

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number : "))

# # 2 = 5 = 2 = a
# # 2 = 2 = 5 = b
# # 5 = 2 = 2 = c

# if a == b and b == c :
#     print("All are equal")
# elif a == b or b == c  or c == a :
#     print("Any two number are equal")
# elif a > b and a > c :
#     print(f"{a} is greatest")
# elif b > a and b > c :
#     print(f"{b} is greatest")
# else :
#     print(f"{c} is greatest")

# Question No 8

# year = int(input("Enter a year : "))

# if year % 100 == 0 and year % 400 == 0 :
#     print("It's a leap year")
# elif year % 100 != 0 and year % 4 == 0 :
#     print("it's a leap year")
# else :
#     print("it's not a leap year!")

# HOME WORK

# Question No 9
# Ask for purchase amount, Apply discount on threshold
# eg : above Rs 1000 => 10% 1200 => 10%
# eg : above Rs 5000 => 20% 5500 => 20% 
# Print the final bill
# SHOP Discount Calculator

# bill = int(input("Please tell your total amount : "))

# if bill >= 1000 and bill < 5000 :
#     print(f"You got discount of 10% your final amuont is {(bill * 90)/100}")
# elif bill >= 5000 :
#     print(f"You got discount of 20% your final amount is {(bill * 80)/100}")
# else :
#     print("Sorry no discount for you!")

# Question No 10
# Vowel and Consonant
# Accept a sigle character from user and check
# if it is vowel (a, e, i , o, u) or consonent 
# invalid char check and case sensitive char check!

char = input("Please tell your Alphabet : ")

if char in "aeiouAEIOU" :
    print("It is a vowel")
elif char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" :
    print("It is a consonent")
else :
    print("Invalid Input")