import string

password = 'oK1d'

print('You forgot your password and you want to recover it. Answering below questions will help us recover your password faster.')

pass_len = int(input('How many characters does the password have? '))

alphabet = ''
c = ''

# checking which character types we need to include
num = input('Does your password contain numbers? (y/n) ')
if num == "y":
    alphabet = alphabet + string.digits
    c = c + ' numbers'

s_let = input('Does your password contain lowercase letters? (y/n) ')
if s_let == "y":
    alphabet = alphabet + string.ascii_lowercase
    c = c + ' lowercase letters'

b_let = input('Does your password contain uppercase letters? (y/n) ')
if b_let == "y":
    alphabet = alphabet + string.ascii_uppercase
    c = c + ' uppercase letters'

spec = input('Does your password special characters? (y/n) ')
if spec == "y":
    alphabet = alphabet + string.punctuation
    c = c + ' special characters'


print('Ok, looking for password of {} characters consisting of{}'.format(pass_len, c))

def pass_recover(pass_len, alphabet):
    if pass_len == 1:
        for ch in alphabet:
            yield ch
    else:
        for sub_str in pass_recover(pass_len-1, alphabet):
            for ch in alphabet:
                yield sub_str + ch


for i in range(pass_len, 5):
    for i in pass_recover(i, alphabet):
        if i == password:
            print("Found your password: " + i)
            break

