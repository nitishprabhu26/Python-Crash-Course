# Working with strings:

user_name = "Nitish Prabhu"
# adding quotation mark in string: using escape charecter "\"
print("Welcome to \"Python Programming\". \nGood Morning!")

# Functions
print(user_name.upper())
print(user_name.isupper())
# combining functions
print(user_name.upper().isupper())

print("Length is "+str(len(user_name)))

# using index
print(user_name[0])
print(user_name.index("i"))
print(user_name.index("ish"))
print(user_name.replace("Nitish Prabhu", "Nitish Prabhu Kota"))