# Advance Stuff in Python

# Lambda Function ✅

# map(), filter(), zip()

# comprehensions (list, dict, set)

# generators (yeild & generator expressions)
# decorators (concept + creation)

# What is Lambda?
# expression Y
# it is a small anonymous function
# written in 1 line

# Normal Function
# def square(x):
#     return x * x
# print(square(2))

# def addTwoNums(a,b):
#     return a + b

# addTwoNums = lambda a, b : a + b

# print(addTwoNums(5, 5))

# square = lambda x : x * x

# print(square(2))

# def keyword is not used in lambda
# there is not function name in lambda functions
# automically return's the value
# it is used when function logic is very small / single line

# Map filter and zip
# What does map do?

# nums = [1, 2, 3, 4]

# print(nums)

# res = map(lambda n : n * n, nums)

# print(list(res))
# print(nums)

# for i in range(len(nums)):
#     nums[i] = nums[i] * nums[i]

# print(nums)
# [1, 4, 9, 16]

# filter

# nums = [1, 2, 3, 4, 5, 6]

# evenNumber = filter(lambda n : n % 2 == 0, nums)

# print(list(evenNumber))

# words = ["hey", "hi", "hello", "bye", "python"]

# filtered = filter(lambda samiksha : len(samiksha) > 3, words)

# print(list(filtered))

# words = ["hey", "hi", "hello", "bye", "python"]

# word2=[]
# for i in words:
#     if len(i) >= 3:
#         word2.append(i)
# print(word2)

# print(list(filter(lambda w : len(w) >= 3, words)))

# myList = [1, 2, 3, 4, 5]
# print(myList)

# for i in range(len(myList)):
#     myList[i] = myList[i] * 2

# print(myList) 

# [2, 4, 6, 8, 10]