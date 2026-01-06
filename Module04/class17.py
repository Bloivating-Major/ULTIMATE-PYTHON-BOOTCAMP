# While Loop
# Syntax
# while condition :
            # code to execute

# break 
# continue

#  break
#  break stops the loop immedieately

# a = 0
# while a < 10 :
#     print(a+1) # 1
#     if a == 5 :
#         break
#     a = a + 1
    
# print(f"This is value of {a}")
    
# a = 1

# while a <= 10 :
#     if a == 5 :
#         a = a + 1
#         continue
#     print(a)
#     a = a + 1


# Print Each Digit (Just in Reverse Order)
# Break a number into individual digits
# Print them starting from the last digit
# EG : 145
# 5
# 4
# 1

a = 145

while  a > 0: 
    rem = a % 10
    print(rem)
    a = a // 10




