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