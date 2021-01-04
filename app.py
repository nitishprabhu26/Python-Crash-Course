# PYTHON Crash COurse
from math import *





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
