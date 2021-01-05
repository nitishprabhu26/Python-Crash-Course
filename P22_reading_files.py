# modes - read, write, append, read/write

employee_file = open("employees.txt", "r")
# open("employees.txt", "w")
# open("employees.txt", "a")
# open("employees.txt", "r+")

# check if file is readable
print(employee_file.readable())


# read individual line - places cursor in the next line
# print(employee_file.readline())

# reads line and puts in a list
# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)

# read content of employee_file
print(employee_file.read())

# close file
employee_file.close()