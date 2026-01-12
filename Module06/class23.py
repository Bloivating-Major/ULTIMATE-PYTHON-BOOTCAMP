# Sum and Average of List

# a = [10, 20, 30, 40, 50]
# # Sum = 150
# # Average = 30
# sum = 0
# for i in a:
#     sum = sum + i
# print(f"The sum is {sum} and average is {sum/len(a)}")

# Take a List and find the maximum element 
# and also index of that element
# a = [1, 45, 23, 89, 67, 98, 12, 36, 82]
# max = a[0] # assuming 1st element is max
# index = 0
# for i in range(len(a)) :
#     if a[i] > max :
#         max = a[i]
#         index = i

# print(f"Your max value is {max} and index is {index}")

#  Print 2nd maximum element
# a = [1, 4, 5, 15, 13]
# max1 = a[0]
# max2 = a[0]
# index1 = 0
# index2 = 0

# for i in range(len(a)):
#     if a[i] > max1 :
#         max2 = max1
#         max1 = a[i]
#         index2 = index1
#         index1 = i
#     elif a[i] > max2 :
#         max2 = a[i]
#         index2 = i
# print(f"Max is {max1} with index {index1} and Max 2 is {max2} with index {index2}")

# Check if the List is sorted in ascending order or not!
# a = [12, 13, 14, 15, 16, 17, 99, 24, 25, 36, 78, 90]

# for i in range(len(a)-1):
#     if a[i] < a[i+1] :
#         continue
#     else :
#         print("Your list is not sorted")
#         break
# else :
#     print("Your list is sorted")