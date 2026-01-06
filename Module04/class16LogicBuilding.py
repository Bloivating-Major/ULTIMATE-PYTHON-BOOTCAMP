# Q1 print "hello"  n times
# n is given by user.

# n = int(input("Enter a number : "))

# for i in range(n) : 
#     print(i+1, " Hello")

# Q2 print number from 1 to n
# take n from user

# n = int(input("Enter a number : "))

# for i in range(1, n+1) : 
#     print(i)

# Q3 print numbers from n to 1 n should not be negative

# n = int(input("Enter a number : "))

# for i in range(n, 0, -1) : 
#     print(i)

# Q4 sum of natural numbers (1 to n)
# take input from user and print sum of natural numbers till N
#N =  5 =  1 + 2 + 3 + 4 + 5 = 15

# a = 0

# a = a + 1 # 1
# a = a + 2 # 3
# a = a + 3 # 6
# a = a + 4  # 10
# a = a + 5 # 15

# print(a)

# n = int(input("Enter a number : "))
# a = 0

# for i in range(1, n+1) : 
#     totalSum = totalSum + i

# print(f"Total sum from 1 to {n} is {totalSum}")

# Q5
# factorial of a number
# user will give a number
# calculate it's factorial

# 5 factorial of 5
# 1 x 2 x 3 x 4 x 5 = 120

# n = int(input("Enter a number : "))
# fact = 1

# for i in range(1, n+1) :
#     fact = fact * i
    
# print(f"Factorial of {n} is {fact}")

# Q6 Print Sum of Even and Odd number in a range of N
# n = 10 2, 4, 6, 8, 10 odd = 1, 3, 5, 7, 9 

# BRUTE FORCE

# n = int(input("Enter a number : "))

# evenSum = 0
# oddSum = 0

# for i in range(1, n+1) : 
#     if i % 2 == 0 :
#         evenSum = evenSum + i
#     else : 
#         oddSum = oddSum + i

# print(f"Even Sum is {evenSum} and Odd Sum is {oddSum}")

#Q7 Print all factors sum take input from user
# # user will input
# calculate the factors
# sum them up

# 6 => 1, 2, 3, 6 sum = 12

# factor => number that divides given number completely

# n = int(input("Enter a number : "))

# factSum = 0

# for i in range(1, n+1) :
#     if n % i == 0 :
#         factSum = factSum + i

# print(f"Sum of all factors : {factSum}")
# print(n % 1)
# print(n % 2)
# print(n % 3)
# print(n % 4)
# print(n % 5)
# print(n % 6)

#Q9 Power Calculation ( a ^ b)
# take input from user as a  = base number b = exponent
# calculate the result using a for loop without using ( ** )

# 2 ^ 3 = 2 x 2 x 2 = 8 
# 5 ^ 4 = 5 x 5 x 5 x 5 = 125

# base = 2 
# expo = 3
# power = 1

# for i in range(1, expo+1, 1) : 
#     power = power * base

# print(power)

# Q10 Prime Number Check
# Accept a number from a user and ceck if it is 
# divisible by 1 and itself! 
# Mhnjech to number prime ahe ki nhi he check kra!

# 1 is 1 prime or not?

# prime number has exact 2 factors
# => 1 and number itself 

# ex : 2, 3, 5, 7, 11, 13

# 2 => No, 3 => No , 4 => No, 5 => No, 6 => No => 7
# 2 => Yes , 3 => No, 4 => Yes, 5 => No, 6 => No , 7 => No

# n = int(input("Enter a number : "))

# if n <= 1 : 
#     print("Not Prime")
# else :
#     isPrime = True
#     for i in range(2, n) : 
#         if  n % i == 0 : 
#             isPrime = False
#             break
#     if isPrime == True :
#         print("Prime Number")
#     else : 
#         print("Not Prime Number")