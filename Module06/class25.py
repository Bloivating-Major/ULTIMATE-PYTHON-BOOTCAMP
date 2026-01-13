# Dictionary in Python

# stores data in key value pair
# kitchen = {
#     "snacks" : "Biscuits",
#     "rice" : "Basmati",
#     "sugar" : "Gava kadchi Sakhar",
#     "teaPowder" : "Vagh Bakri Chaha"
# }

# print(kitchen)

# characteristics
# 1. Mutable
# 2. Keys must be unique
# 3. Values can be duplicate
# 4. Ordered 

# Dictionary traversing

kitchen = {
    "snacks" : "Biscuits",
    "rice" : "Basmati",
    "sugar" : "Gava kadchi Sakhar",
    "teaPowder" : "Vagh Bakri Chaha",
}

# print(kitchen[21])

# method 1 to run a loop
# for i in kitchen:
#     print(kitchen[i])

# method 2 to run a loop
# for values in kitchen.values():
#     print(values)
    
# for keys in kitchen.keys():
#     print(keys)

# for keys, values in kitchen.items():
#     print(keys, values)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# # get
# brand = car.get("brand")
# print(brand)

# pop
# print(car)
# car.pop("year")
# print(car)

# update