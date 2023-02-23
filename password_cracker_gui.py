import pyautogui
import random
import string

alphabet = string.printable[:76]
cracked_password = []


def set_character_limitations():
    # Let user input a password using input()
    # Find the length of the password using len()

    user_input = pyautogui.password('Enter your password: ')
    length = len(user_input)
    inputlist = set(user_input)
    setcheck = inputlist.difference(alphabet)
    setlength = len(setcheck)
    # Check for character limit
    if length > 15:
        print("Your password exceeds character limit of 15!")
        set_character_limitations()
    # Check if the input matches the character lists, if not, prompt again.
    elif setlength > 0:
        print("The character(s)", setcheck, "aren't allowed!")
        set_character_limitations()
    elif not setcheck:
        password_cracker(user_input)


def password_cracker(user_input):
    # Checks if each character is a letter(capitalized or not), a number or a special character.
    # If condition is correct, loop until it matcheds with the randomized list of alphanumerics and special characters.
    # Prints output live to see the function in action as it loops through to find the password
    i = 0
    for char in user_input:
        if char.isalpha() == True:
            if char.islower() == True:
                rand = ''
                while rand != char:
                    rand = random.choice(alphabet)
                    if rand == char:
                        cracked_password.append(rand)
                        i += 1
            if char.isupper() == True:
                rand = ''
                while rand != char:
                    rand = random.choice(alphabet)
                    rand = rand.upper()

                    if rand == char:
                        cracked_password.append(rand)
                        i += 1

        if char.isnumeric() == True:
            rand = ''
            while rand != char:
                rand = random.choice(alphabet)
                if rand == char:
                    cracked_password.append(rand)
                    i += 1

        elif char.isalpha() != True:
            rand = ''
            while rand != char:
                rand = random.choice(alphabet)
                if rand == char:
                    cracked_password.append(rand)
                    i += 1

    answer = ''.join(cracked_password)
    print("Guessed right!")
    print("Your cracked password is:", answer)


set_character_limitations()
