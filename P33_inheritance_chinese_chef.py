from P31_inheritance_Chef import Chef

# inheritance - use all functions of chef class inside chinese chef class
class ChineseChef(Chef):

    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")