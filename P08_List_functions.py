friends1 = ["John", "Jane", "Jack"]
friends2 = ["John", 2, True]

print("\nList Functions:")
# combine list
print("\nCombining lists:")
friends1.extend(friends2)
print(friends1)

# add individual element to list
print("\nadd individual element to list")
friends1.append("Jim")
print(friends1)
# add individual element to list in the middle
print("add individual element to list in the middle")
friends1.insert(1, "Jared")
print(friends1)

print("remove element")
# Remove first occurrence of value.
friends1.remove("Jim")
print(friends1)

print("pops last element")
print(friends2.pop())
print(friends2)
print("clear the elements of the list")
print(friends2.clear())
print(friends2)
print("Return number of occurrences of value")
print(friends1.count("John"))
print(friends1)
friends1.remove("John")
print(friends1)

print("Return first index of value")
print(friends1.index("Jack"))

print("\nSorting List")
numbers1 = [1,3,4,2]
numbers1.sort()
print(numbers1)
numbers1.reverse()
print(numbers1)
numbers2=numbers1.copy()
print(numbers2)