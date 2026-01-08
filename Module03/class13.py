# # VOTER ID CHECK

# # IF VOTER IS HAVING AGE GREATER THAN 18 
# # THEN HE/SHE CAN VOTE
# # ELSE THEY CANNOT VOTE

# # Control Flow
# # If else
# # Loops

# age = int(input("Enter a age: "))
   
# if age >= 18 :
#     print("You can vote")
# else :
#     print("You cannot vote")

# print("All students Name")

# # LOOPs with INPUT statement

# # IF ELSE Condition
# print("Samiksha")
# print("Shreya")
# print("Pranita")
# print("Prajakta")
# print("Om")
# print("Misba")
# print("Vaishnavi")


# take 2 inputs a and b
# check in if 

# a = int(input("Enter a number A : "))
# b = int(input("Enter a number B : "))

# if a > b : # condition true
#     print(f"A is Greater {a}")
    
# # condition false
# else :
#     print(f"B is Greater {b}")
    
    
# user has 100 rs
# if he purchase 40 rs atta (pith) then how much will remain?
# if user is left with more than 50 rs then buy 2 chocolates of 20 rs 
# and give the final answer how many rs left?

# money = int(input("Enter how much Rs do you have? : "))

# atta = 40 
# print("Atta is of 40 Rs. You have successfully purchased it!\n")

# money = money - atta 

# if money >= 50 : 
#     chocolate = 20
#     print(f"You have more than 50rs left! Now you can purchase 2 Chocolates 1 for 20rs\n")
#     money = money - chocolate * 2 

# print(f"You have {money} Rs left!")

contri = int(input("Kiti paise gola jhale? : "))

if contri <= 10 and contri >=5 :
    print("Chocolate chi goli gheu apan!")
    
elif contri > 10 and contri <= 50 :
    print("Cadbury gheu apan!")
    
elif contri > 50 and contri <= 100 : 
    print("Wafers and Cupcake gheu apan!")
    
elif contri > 100 :
    print("Hotel madhe j1 karu apan!")
    
else :
    print("Kami paise aslya mule apan kahich karu shakat nhi!")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")