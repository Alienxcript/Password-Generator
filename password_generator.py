# password generator

import random

char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*_-+=|,./?><;:"

char_list = list(char)
randomized_char_list = char_list.copy()
random.shuffle(randomized_char_list)
random.shuffle(randomized_char_list)

user_no_of_char = 0

def intro():
    print("Hello, welcome to the Password Generator")


def no_of_char():
    global user_no_of_char
    try:
        user_no_of_char = int(input("What is the number of characters you would like Your password to have(number should be greater than 7):   "))
    except ValueError:
        print("Your input is not a number")
        no_of_char()
    else:
        confirm_no_char()

def confirm_no_char():
    if user_no_of_char < 7:
        print("Your value is less than seven(7)")
        no_of_char()
    else:
        password_generate()


pas_wrd = list()


def password_generate():
    global pas_wrd
    global user_no_of_char
    while user_no_of_char > 0:
        choosed_char = random.choice(randomized_char_list)
        pas_wrd.append(choosed_char)
        user_no_of_char -= 1 

intro()
no_of_char()
pas_wrd = "".join(pas_wrd)
print(pas_wrd)


input("Press Enter to Exit:.....    ")



