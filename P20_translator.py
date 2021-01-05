# Translator - convert vowels to '*'

def translate(phrase):
    translation = ""
    for letter in phrase:
        # if letter.lower() in "aeiou:"
        if letter in "AEIOUaeiou":
            translation = translation +"*"
        else:
            translation = translation +letter
    return translation

print(translate(input("Enter a phrase: ")))


# Comments
'''multi
line
comment'''