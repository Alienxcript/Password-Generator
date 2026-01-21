# password generator

import random
from datetime import datetime

char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*_-+=|,./?><;:"

char_list = list(char)
randomized_char_list = char_list.copy()
random.shuffle(randomized_char_list)
random.shuffle(randomized_char_list)

user_no_of_char = 0

def intro():
    print("Hello, welcome to the Password Generator")

# this function checks the user input if it a number(integer)

def no_of_char():
    global user_no_of_char
    try:
        user_no_of_char = int(input("What is the number of characters you would like Your password to have(number should be greater than 7):   "))
    except ValueError:
        print("Your input is not a number")
        no_of_char()
    else:
        confirm_no_char()

# this function checks if the imputed integer is less than seven

def confirm_no_char():
    if user_no_of_char < 7:
        print("Your value is less than seven(7)")
        no_of_char()
    else:
        password_generate()


pas_wrd = list()

# this function generates the password using the user stated passowrd number length with a while loop 
# and appends it to the above password variable that is a list

def password_generate():
    global pas_wrd
    global user_no_of_char
    while user_no_of_char > 0:
        choosed_char = random.choice(randomized_char_list)
        pas_wrd.append(choosed_char)
        user_no_of_char -= 1 

# the functions executed 

#function to save the passwords

def save_password(password):
    with open("generated_passwords.txt", "a") as file:
        file.write("Password:  " + password + "\n")
        file.write("Time Generated:  " + str(datetime.now()) + "\n\n")


intro()
no_of_char()
pas_wrd = "".join(pas_wrd)
print(pas_wrd)
save_password(pas_wrd)



#seems this was necessary at the time when the script is launched through the terminal
# after the output the terminal closes this code is to keep it open
input("Press Enter to Exit:.....    ")


