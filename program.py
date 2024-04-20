import random
import string

def password_generator(min_length, alphabets, numbers, special_characters):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = ""
    if alphabets:
        characters += letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_letters = False
    has_numbers = False
    has_special = False


    while (not meets_criteria) or len(pwd)< min_length:
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in letters:
            has_letters = True
        elif new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if alphabets:
            meets_criteria = has_letters and meets_criteria
        if special_characters:
            meets_criteria = has_special and meets_criteria

    return pwd

min_length1= int(input("Enter the min length of the password : "))
alphabets1 = input("Weather you want to include alphabet (y/n) : ")
numbers1 = input("weather you want to include numbers (y/n) : ")
special_characters1 = input ("Weather you want to include special_characters (y/n) : ")
password = password_generator(min_length1, alphabets1, numbers1, special_characters1)
print("your password is : ", password)

