# If Else
# Q1. Check whether a number is even or odd
# Pseudocode:
# 1 Start
# 2 Take number input
# 3 Check number % 2 == 0
# 4 If true print Even
# 5 Else print Odd
# 6 End

# num = int(input("Enter a number : "))

# if num % 2 == 0 :
#     print("Even")
# else :
#     print("Odd")

# Q2. Check voting eligibility based on age
# Pseudocode:
# 1 Start
# 2 Take age input
# 3 Check age >= 18
# 4 If yes print Eligible
# 5 Else print Not eligible
# 6 End

# age = int(input("Enter a age : "))

# if age >= 18 :
#     print("You can vote")
# else :
#     print("You cannot vote")

# Q3. Check if entered number is positive or negative
# Pseudocode:
# 1 Start
# 2 Take number input
# 3 Check number > 0
# 4 If yes print Positive
# 5 Else print Negative
# 6 End

# num = int(input("Enter a number : "))

# if num > 0 :
#     print("Positive")
# else :
#     print("Negative")

# Q4. Check if student passed the exam
# Pseudocode:
# 1 Start
# 2 Take marks input
# 3 Check marks >= 40
# 4 If yes print Passed
# 5 Else print Failed
# 6 End

# marks = int(input("Enter marks : "))

# if marks >= 35 :
#     print("Pass")
# else :
#     print("Fail")

# Q5. Check if temperature is hot or cold
# Pseudocode:
# 1 Start
# 2 Take temperature input
# 3 Check temp >= 30
# 4 If yes print Hot
# 5 Else print Cold
# 6 End

# temperature = int(input("Enter temperature : "))

# if temperature >= 30 :
#     print("Hot")
# else :
#     print("Cold")

# Q6. Check if a number is divisible by 7
# Pseudocode:
# 1 Start
# 2 Take number input
# 3 Check number % 7 == 0
# 4 If yes print Divisible
# 5 Else print Not divisible
# 6 End

# num = int(input("Enter a number : "))

# if num % 7 == 0 :
#     print("Divisible by 7")
# else :
#     print("Not divisible by 7")

# Q7. Check if username length is valid
# Pseudocode:
# 1 Start
# 2 Take username input
# 3 Check length >= 5
# 4 If yes print Valid
# 5 Else print Invalid
# 6 End

# Q8. Check if user entered correct OTP
# Pseudocode:
# 1 Start
# 2 Store correct OTP
# 3 Take user OTP
# 4 Compare both
# 5 If match print Success
# 6 Else print Failed
# 7 End

# Q9. Check if character is vowel or consonant
# Pseudocode:
# 1 Start
# 2 Take character input
# 3 Check if in vowels
# 4 If yes print Vowel
# 5 Else print Consonant
# 6 End

# Q10. Check if a number is zero or non-zero
# Pseudocode:
# 1 Start
# 2 Take number input
# 3 Check number == 0
# 4 If yes print Zero
# 5 Else print Non-zero
# 6 End

# If Else Ladder


# Q11. Assign grade based on marks
# Pseudocode:
# 1 Start
# 2 Take marks input
# 3 If marks >= 90 grade A
# 4 Else if >=75 grade B
# 5 Else if >=60 grade C
# 6 Else print Fail
# 7 End

# Q12. Categorize age group
# Pseudocode:
# 1 Start
# 2 Take age input
# 3 If age < 13 child
# 4 Else if < 20 teenager
# 5 Else if < 60 adult
# 6 Else senior
# 7 End

# Q13. Check traffic signal action
# Pseudocode:
# 1 Start
# 2 Take signal color
# 3 If red stop
# 4 Else if yellow slow down
# 5 Else if green go
# 6 End

# Q14. Electricity bill category
# Pseudocode:
# 1 Start
# 2 Take units input
# 3 If units <=100 low usage
# 4 Else if <=300 medium usage
# 5 Else high usage
# 6 End

# Q15. Determine exam result category
# Pseudocode:
# 1 Start
# 2 Take marks
# 3 If >=85 distinction
# 4 Else if >=60 first class
# 5 Else if >=40 pass
# 6 Else fail
# 7 End

# Q16. Weather condition message
# Pseudocode:
# 1 Start
# 2 Take temperature
# 3 If <10 very cold
# 4 Else if <25 pleasant
# 5 Else hot
# 6 End

# Q17. Check salary tax slab
# Pseudocode:
# 1 Start
# 2 Take salary
# 3 If <=250000 no tax
# 4 Else if <=500000 low tax
# 5 Else high tax
# 6 End

# Q18. Movie ticket pricing
# Pseudocode:
# 1 Start
# 2 Take age
# 3 If <12 child price
# 4 Else if <60 adult price
# 5 Else senior discount
# 6 End

# Q19. Determine BMI category
# Pseudocode:
# 1 Start
# 2 Take BMI
# 3 If <18 underweight
# 4 Else if <25 normal
# 5 Else overweight
# 6 End

# Q20. Student attendance status
# Pseudocode:
# 1 Start
# 2 Take attendance %
# 3 If >=90 excellent
# 4 Else if >=75 good
# 5 Else poor
# 6 End


# For Loop


# Q21. Print numbers from 1 to N
# Pseudocode:
# 1 Start
# 2 Take N
# 3 Run loop from 1 to N
# 4 Print each number
# 5 End

# n = 7
# n = int(input("Enter a number : "))
# for i in range(1, n+1, 1):
#     print(i)
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)

# Q22. Print multiplication table of a number
# Pseudocode:
# 1 Start
# 2 Take number
# 3 Loop from 1 to 10
# 4 Multiply and print
# 5 End

# n = int(input("Enter a number : "))

# for i in range(1, 11, 1):
#     print(f"{n} x {i} = {n*i}")
    
# print(f"{n} x 1 = {n*1}")
# print(f"{n} x 2 = {n*2}")
# print(f"{n} x 3 = {n*3}")
# print(f"{n} x 4 = {n*4}")
# print(f"{n} x 5 = {n*5}")
# print(f"{n} x 6 = {n*6}")
# print(f"{n} x 7 = {n*7}")
# print(f"{n} x 8 = {n*8}")
# print(f"{n} x 9 = {n*9}")
# print(f"{n} x 10 = {n*10}")

# Q23. Calculate sum of first N Natural numbers
# Pseudocode:
# 1 Start
# 2 Take N
# 3 Initialize sum = 0
# 4 Loop from 1 to N
# 5 Add to sum
# 6 Print sum
# 7 End

# 1 + 2 + 3 + 4 + 5

# n = int(input("Enter a number : "))
# answer = 0
# for i in range(1, n+1, 1) :
#     answer = answer + i
# answer = answer + 1
# answer = answer + 2
# answer = answer + 3
# answer = answer + 4
# answer = answer + 5
# print(answer)

# Q24. Print all even numbers between 1 and 50
# Pseudocode:
# 1 Start
# 2 Loop from 1 to 50
# 3 Check even
# 4 Print if even
# 5 End

# for i in range(1, 51, 1):
#     if i % 2 == 0:
#         print(i)

# Q25. Count digits in a number
# Pseudocode:
# 1 Start
# 2 Take number as string
# 3 Loop through characters
# 4 Count digits
# 5 Print count
# 6 End

# num = input("Enter a number : ")
# count = 0

# for i in num :
#     count = count + 1

# print(count)

# print(num[0:3:1])

# for i in range(len(num)) :
#     print(num[i])


# Q26. Print characters of a string
# Pseudocode:
# 1 Start
# 2 Take string
# 3 Loop through string
# 4 Print each character
# 5 End

# name = input("Enter your name : ")

# for i in name :
#     print(i)
    
 

# Q27. Calculate factorial using for loop
# Pseudocode:
# 1 Start
# 2 Take number
# 3 Initialize result = 1
# 4 Loop from 1 to number
# 5 Multiply
# 6 Print result
# 7 End

# fact = fact * 1
# fact = fact * 2
# fact = fact * 3
# fact = fact * 4
# fact = fact * 5

# n =  int(input("Enter your number : "))
# fact = 1

# for i in range(1, n+1, 1):
#     fact = fact * i

# print(fact)

# Q28. Print squares of numbers 1 to 10
# Pseudocode:
# 1 Start
# 2 Loop from 1 to 10
# 3 Calculate square
# 4 Print square
# 5 End

# for i in range(1, 11, 1):
#     print(f"{i} x {i} = {i*i}")

# print("1 x 1 = 1")
# print("2 x 2 = 4")
# print("3 x 3 = 9")
# print("4 x 4 = 16")
# print("5 x 5 = 25")
# print("6 x 6 = 36")
# print("7 x 7 = 49")
# print("8 x 8 = 64")
# print("9 x 9 = 91")
# print("10 x 10 = 100")

# Q29. Print numbers in reverse from N to 1
# Pseudocode:
# 1 Start
# 2 Take N
# 3 Loop from N to 1
# 4 Print number
# 5 End

# n = 10

# for i in range(n, 0, -1):
#     print(i)

# Q30. Count multiples of 3 between 1 and 100
# Pseudocode:
# 1 Start
# 2 Initialize count
# 3 Loop 1 to 100
# 4 Check %3
# 5 Increase count
# 6 Print count
# 7 End

# count = 0

# for i in range(1, 101, 1):
#     if i % 3 == 0:
#         count  = count + 1
        
# print(count)

# While Loop

# Q31. Print numbers from 1 to N
# Pseudocode:
# 1 Start
# 2 Take N
# 3 Set i=1
# 4 While i<=N
# 5 Print i
# 6 Increment i
# 7 End

# n = int(input("Enter a number : "))
# i = 1
# while i <= n:
#     print(i)
#     i = i + 1

# Q32. Sum digits of a number
# Pseudocode:
# 1 Start
# 2 Take number
# 3 Initialize sum=0
# 4 While number>0
# 5 Extract digit
# 6 Add to sum
# 7 Reduce number
# 8 Print sum
# 9 End

# Q33. Reverse a number
# Pseudocode:
# 1 Start
# 2 Take number
# 3 Initialize reverse=0
# 4 While number>0
# 5 Extract digit
# 6 Build reverse
# 7 Reduce number
# 8 Print reverse
# 9 End

# Q34. Check palindrome number
# Pseudocode:
# 1 Start
# 2 Take number
# 3 Store original
# 4 Reverse using loop
# 5 Compare original and reverse
# 6 Print result
# 7 End

# Q35. Find factorial using while loop
# Pseudocode:
# 1 Start
# 2 Take number
# 3 Set result=1
# 4 While number>0
# 5 Multiply
# 6 Decrease number
# 7 Print result
# 8 End

# Q36. Print even numbers up to N
# Pseudocode:
# 1 Start
# 2 Take N
# 3 Set i=2
# 4 While i<=N
# 5 Print i
# 6 i+=2
# 7 End

# Q37. Count digits using while loop
# Pseudocode:
# 1 Start
# 2 Take number
# 3 Set count=0
# 4 While number>0
# 5 Increase count
# 6 Reduce number
# 7 Print count
# 8 End

# Q38. Find sum until user enters 0
# Pseudocode:
# 1 Start
# 2 Set sum=0
# 3 Take input
# 4 While input !=0
# 5 Add to sum
# 6 Take input
# 7 Print sum
# 8 End

# Q39. Print table using while loop
# Pseudocode:
# 1 Start
# 2 Take number
# 3 Set i=1
# 4 While i<=10
# 5 Multiply and print
# 6 Increment i
# 7 End

# Q40. Check password until correct
# Pseudocode:
# 1 Start
# 2 Set correct password
# 3 Take input
# 4 While input != correct
# 5 Ask again
# 6 Print success
# 7 End

# Break and Continue


# Q41. Stop printing numbers when number is 7
# Pseudocode:
# 1 Start
# 2 Loop from 1 to 10
# 3 If number ==7 break
# 4 Print number
# 5 End

# Q42. Skip number 5 while printing
# Pseudocode:
# 1 Start
# 2 Loop 1 to 10
# 3 If number ==5 continue
# 4 Print number
# 5 End

# Q43. Stop loop when user enters negative number
# Pseudocode:
# 1 Start
# 2 Loop forever
# 3 Take input
# 4 If input <0 break
# 5 Print input
# 6 End

# Q44. Skip vowels in a string
# Pseudocode:
# 1 Start
# 2 Take string
# 3 Loop characters
# 4 If vowel continue
# 5 Print character
# 6 End

# Q45. Exit loop when sum exceeds 100
# Pseudocode:
# 1 Start
# 2 Set sum=0
# 3 Loop inputs
# 4 Add to sum
# 5 If sum>100 break
# 6 End

# Q46. Skip multiples of 3
# Pseudocode:
# 1 Start
# 2 Loop 1 to 30
# 3 If multiple of 3 continue
# 4 Print number
# 5 End

# Q47. Stop searching when item found
# Pseudocode:
# 1 Start
# 2 Loop list
# 3 If item found break
# 4 End

# Q48. Skip even numbers
# Pseudocode:
# 1 Start
# 2 Loop 1 to 20
# 3 If even continue
# 4 Print odd
# 5 End

# Q49. Stop loop after 5 attempts
# Pseudocode:
# 1 Start
# 2 Set attempts=0
# 3 Loop
# 4 Increase attempts
# 5 If attempts==5 break
# 6 End

# Q50. Ignore invalid inputs
# Pseudocode:
# 1 Start
# 2 Loop inputs
# 3 If invalid continue
# 4 Process input
# 5 End

# Indentation
# Q51. Fix indentation in nested if statement
# Pseudocode:
# 1 Start
# 2 Observe wrong indentation
# 3 Correct if blocks
# 4 Ensure proper nesting
# 5 End
# Q52. Fix indentation in for loop
# Pseudocode:
# 1 Start
# 2 Check loop body alignment
# 3 Indent statements correctly
# 4 End
# Q53. Fix indentation in while loop
# Pseudocode:
# 1 Start
# 2 Check while condition
# 3 Indent loop body
# 4 End
# Q54. Fix indentation in if-else inside loop
# Pseudocode:
# 1 Start
# 2 Identify block structure
# 3 Correct indentation
# 4 End
# Q55. Fix indentation in break statement
# Pseudocode:
# 1 Start
# 2 Place break inside loop
# 3 Indent correctly
# 4 End
# Q56. Fix indentation in continue statement
# Pseudocode:
# 1 Start
# 2 Ensure continue inside loop
# 3 Indent correctly
# 4 End
# Q57. Fix indentation in grade program
# Pseudocode:
# 1 Start
# 2 Align else-if ladder
# 3 Fix indentation levels
# 4 End
# Q58. Fix indentation in input validation
# Pseudocode:
# 1 Start
# 2 Align if checks
# 3 Indent print statements
# 4 End
# Q59. Fix indentation in nested loops
# Pseudocode:
# 1 Start
# 2 Check inner loop indentation
# 3 Fix alignment
# 4 End
# Q60. Fix indentation in menu-driven program
# Pseudocode:
# 1 Start
# 2 Indent menu options correctly
# 3 Ensure logic works
# 4 End