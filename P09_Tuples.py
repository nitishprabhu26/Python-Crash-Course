# Working with Tuples
# Tuples are immutable. its a container where we can store values.
# It is immutable- cant be changed/modified once created. for data thats never gonna change.
# But Lists can do it all

coordinates = (4,5)

# TypeError: 'tuple' object does not support item assignment
# coordinates[1]=6

print(coordinates[0])

# Lists of tuples
coordinate_list=[(1,2), (4,4), (80,55)]
print(coordinate_list)
