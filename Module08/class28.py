# Exception and Error Handling in Python

# a = int(input("enter a number: "))

# try:
#     print(10/a)
# except ZeroDivisionError:
#     print("Sorry you cannot divide by 0")

# print("So i have done the division")

a = int(input("enter a number: "))

try:
    print(10/a)
except Exception as err:
    print(f"Sorry there is an error as {err}")

print("Ok so i have done the division")