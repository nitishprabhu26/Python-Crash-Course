# Loop - Loop through and execute a block of code multiple times

print("While loop: ")
i = 1
while i <= 10:
    print(i)
    i += 1

print("While loop completed\n")

print("For loop: ")
for letter in "Nitish":
    print(letter)

friends = ["Jack", "John", "Jane"]
for friend in friends:
    print(friend)

# Range: last value wont be included
for index in range(0,10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

print("For loop completed\n")