# print("Welcome to the Python restaurant")

# print("Menu card:")
# menu_card={
#     "Pasta":70,
#     "Burger":68,
#     "Pizza":50,
#     "Maggie":90,
# }

# for key,values in menu_card .items():
#     print(f"{key}:{values}")

# bill=0
# bill=bill+menu_card["Maggie"]
# print(f"your bill is {bill} RS")

# print("Thank you visit again!")

# Hashing Concept in Data Structure

# numbers = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3 , 4, 4, 4, 4, 4, 4,4, 4, 4, 4,4, 4, 4, 5, 5, 5, 5,5]

# # 1, 2, 3, 4, 5

# occurences = {}

# for i in numbers:
#     if i in occurences:
#         occurences[i] = occurences[i] + 1
#     else :
#         occurences[i] = 1


# for keys in occurences.keys():
#     print(keys)

# Step 1 Create Empty Dictionary
# Step 2 Run a Loop on List
# Step 3 Ask a question does that element exist in your dictionary
# Step 4 If Yes => Increase It's value by 1
# Step 5 If No => Add it to the dictionary and give it value as 1


# occurences = { 
#               1 : numbers.count(1), 
#               2 : numbers.count(2), 
#               3: numbers.count(3), 
#               4 : numbers.count(4), 
#               5 : numbers.count(5) 
# }

# print(occurences)

# print(numbers.count(1))
# print(numbers.count(2))
# print(numbers.count(3))
# print(numbers.count(4))
# print(numbers.count(5))