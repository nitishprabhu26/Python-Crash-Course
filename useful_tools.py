import random

feet_in_mile = 5280
meters_in_kilometers = 1000
number_array = [1,2,3,4,5,6,7,8,9,0]


def get_file_ext(filename):
    return filename[filename.index(".")+1:]


def roll_dice(num):
    return random.randint(1,num)