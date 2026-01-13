# Data Strucuture
# 1. LIST = []

# 2. TUPLE = ()
# t = ( 10, 20, 30 )
# print(type(t))

# Characteristics
# Ordered
# Indexed
# Immutable (cannot be chaged)
# Heterogeneous!

# l = [10, True, "Sambhav"]
# t = (10, True, "Sambhav")

# print(l[0]) # 10
# l[0] = 100
# print(l[0]) # 10

# print(t[0]) # 10
# t[0] = 100
# print(t)

# Indexing in Tuple
# t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# print(t[1])
# s = "Rajgurunagar"

# print(s)
# print(s[::-1])


# Tuple Traversing
# t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# for i in t:
#     print(i)

# range function
# for i in range(len(t)):
#     print(t[i])

# Tuple Methods
# t = (10, 20, 30, 20, 20, 10, 30)
# t = (
#     88, 23, 5, 71, 42, 90, 14, 67, 31, 99, 
#     1, 55, 82, 36, 4, 78, 29, 60, 9, 45, 
#     11, 73, 80, 2, 51, 94, 38, 66, 17, 49, 
#     85, 22, 7, 92, 3, 58, 13, 61, 40, 96, 
#     25, 77, 10, 53, 89, 34, 6, 91, 19, 47
# )

# print(t.count(20))
# print(t.index(17))

# Tuple Constructor
# lst = [1, 2, 3] #mutable
# t = tuple(lst)
# print(t)

# Tuple Unpacking

# gift = ("Remote Car", "Aeroplane", "Chess")
# print(gift)

# gift01, gift02, gift03 =  ("Remote Car", "Aeroplane", "Chess")

# print(gift01)
# print(gift02)
# print(gift03)

# t = (1, 2, 3)
# t = (1,)

# print("I am checking type :",type(t))

# SETS

# What is SET?
# - store multiple unique values
# - duplicates are not allowed
# s = {1, 2, 3}
# # s = {}

# print(s)
# print(type(s))

# Characteristics
# 1. Unordered
# 2. No Index
# 3. Mutable
# 4. Based on Hashing

# name = "$@mb#@v"
# isChild = False
# age = 1234567
# print(hash(age))

# print(isChild)
# print(hash(isChild))

# print(name)
# print(hash(name))

# s = {1, 2 ,2, 3, 3, 3, 4, 4, 4, 4, 5}
# print(s)

# s = {1, 2, 3, 4, 5, 6, 7}

# for i in s:
#     print(i)

# Set Constructor

# lst = [2, 2, 2, 3, 3, 6, 6, 6, 4, 4, 4, 5]
# print(lst)
# s = set(lst)
# print(s)

# Set Methods
# 1. add
# s = {1, 2, 3}
# print(s)
# s.add(4)
# print(s)

# 2. remove
# s = {1, 2, 3, 4}
# print(s)
# s.remove(2)
# print(s)

# 3. union
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.union(y)

# print(z)

# 4. intersection
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)

# 5. difference
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.difference(y)

# print(z)

# x = {1, 2, 3, 4, 5, 6}
# y = {9, 3, 4, 5, 6}

# z = x.difference(y)
# z = y.union(x)
# z = z.difference(y)

# print(z)