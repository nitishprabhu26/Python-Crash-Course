# PYTHON Crash COurse
from math import *

print("Hello World!")

user_name = "Nitish Prabhu"
user_age = 25
is_student = True
print("Hi, I am " + user_name + ". I am " + str(user_age) + " years old.")

# Working with strings:
print("Welcome to \"Python Programming\". \nGood Morning!")
print(user_name.upper())
print(user_name.upper().isupper())
print(len(user_name))
print(user_name[0])
print(user_name.index("i"))
print(user_name.index("ish"))
print(user_name.replace("Nitish Prabhu", "Nitish Prabhu Kota"))

# Working with numbers:
print(-5.4)
print(2 * 5.9)
print(10 % 4)
print(abs(-4))
print(pow(3, 2))
print(max(3, 2))
print(round(3.49))
print(ceil(3.2))
print(sqrt(67))

# Getting Input From Users
name = input("Enter name: ")
print("Hello " + name + "!")

# Lists
friends1 = ["John", "Jane", "Jack"]
friends2 = ["John", 2, True]
print(friends1[0])
print(friends2[-1])
print(friends2[1:2])
friends2[1] = 3
print(friends2[1:2])

# combine list
friends1.extend(friends2)
print(friends1)
# add individual element to list
friends1.append("Jim")
print(friends1)
# add individual element to list in the middle
friends1.insert(1, "Jared")
print(friends1)
friends1.remove("Jim")
print(friends1)
print(friends2.pop())
print(friends2)
print(friends2.clear())
print(friends2)
print(friends1.count("John"))
print(friends1)
friends1.remove("John")
print(friends1)
print(friends1.index("Jack"))
numbers1 = [1,3,4,2]
numbers1.sort()
print(numbers1)
numbers1.reverse()
print(numbers1)
numbers2=numbers1.copy()
print(numbers2)

# Working with Tuples
