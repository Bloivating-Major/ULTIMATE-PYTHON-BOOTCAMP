# # Print Each Digit (Reverse Order)
# # Break a number into individual digit
# # and print them starting form the last digit.
# # 345 = 5 4 3

# # num = int(input("Enter a number : "))

# # while num > 0:
# #     rem = num % 10
# #     print(rem)
# #     num = num // 10
    
# # Sum of Digits
# # Add all the digits of a number (e.g 123 => 1+2+3 = 6)
# # 123 = 1 + 2 + 3 = 6

# # num = int(input("Enter a number : "))
# # total = 0

# # while num > 0 : 
# #     rem = num % 10
# #     total = total + rem
# #     num = num // 10

# # print(f"Sum of digit is {total}")

# # Reverse a number
# # input a number and reverse its digits eg.
# # 123 => 321

# # num = int(input("Enter a number : "))
# # rev = 0

# # while num > 0 : 
# #     digit = num % 10
# #     rev = rev * 10 + digit
# #     num = num // 10

# # print(f"Reverse is {rev}")

# # Palindrome Number Check
# # check if a number is palindrome reads
# # same from forward and backwards eg. 121, 1331

# # num = int(input("Enter a number : "))
# # dup = num
# # rev = 0

# # while num > 0 : 
# #     digit = num % 10
# #     rev = rev * 10 + digit
# #     num = num // 10

# # if dup == rev :
# #     print(f"{dup} is Palindrome")
# # else : 
# #     print(f"{dup} is not Palindrome")

# # Automorphic Number
# # a number is automorphic if it's square ends
# # with the number itself
# # 5 ^ 2 = 25 
# # 76^2 = 5776

# num = int(input("Enter a number : "))
# square = num * num 

# temp = num
# rem = 1

# while temp > 0 :
#     rem = rem * 10 
#     temp = temp // 10 
             
# if square % rem == num :
#     print("Number is Automorphic")
# else :
#     print("Number is not Automorphic")
