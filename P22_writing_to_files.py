# append- adding text at the end of the file

employee_file = open("employees.txt", "a")
employee_file.write("\nNitish - Developer")

employee_file.close()

# writing/overwriting the file
employee_file = open("employees.txt", "w")
employee_file.write("Jim - Salesman")
employee_file.write("\nKim - Developer")
employee_file.write("\nPam - Tester")
employee_file.write("\nTim - Manager")
employee_file.write("\nNitish - Developer")

employee_file.close()


employee_file1 = open("employees1.txt", "w")
employee_file1.write("Nitish - Developer")

employee_file.close()


# NOTE: HTML can also be written into a file(.html file)