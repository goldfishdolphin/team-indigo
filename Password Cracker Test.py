import random

special = ["#","$","%","&","*","!","@","^","-","+","."]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
          "n","o","p","q","r","s","t","u","v","w","x","y","z"]
numerals = ["0","1","2","3","4","5","6","7","8","9"]
cracked_password = []

def set_character_limitations():
    # Let user input a password using input()
    # Find the length of the password using len() 
    print('Enter a password, only the alphabet, numbers, and some special characters are allowed:')
    user_input = input()
    length = len(user_input)
    inputlist = set(user_input)
    caps = [x.upper() for x in alphabet]
    setcheck = inputlist.difference(special,alphabet,numerals,caps)
    setlength = len(setcheck)
    # Check for character limit
    if length > 15:
        print("Your password exceeds character limit of 15!")
        set_character_limitations()
    # Check if the input matches the character lists, if not, prompt again.
    elif setlength > 0:
        print("The character(s)",setcheck, "aren't allowed!")
        set_character_limitations()
    elif not setcheck:
        password_cracker(user_input, length)   

def password_cracker(user_input,length):
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
                    print("Trying random letter ...", rand)
                    if rand == char:
                        cracked_password.append(rand)
                        i += 1
                        print("Guessed right! ... " ,(''.join(cracked_password))+('▇'*(length-i)))
            if char.isupper() == True:
                rand = ''
                while rand != char:
                    rand = random.choice(alphabet)
                    rand = rand.upper()
                    print("Trying random letter ...", rand)
                    if rand == char:
                        cracked_password.append(rand)
                        i += 1
                        print("Guessed right! ... " ,(''.join(cracked_password))+('▇'*(length-i)))
        if char.isnumeric() == True:
            rand = ''
            while rand != char:
                rand = random.choice(numerals)
                print("Trying random number ...", rand)
                if rand == char:
                    cracked_password.append(rand)
                    i += 1
                    print("Guessed right! ... " ,(''.join(cracked_password))+('▇'*(length-i)))
        elif char.isalpha() != True:
            rand = ''
            while rand != char:
                rand = random.choice(special)
                print("Trying random special character ...", rand)
                if rand == char:
                    cracked_password.append(rand)
                    i += 1
                    print("Guessed right! ..." ,(''.join(cracked_password))+('▇'*(length-i)))
    print("Your cracked password is:", ''.join(cracked_password))


set_character_limitations()