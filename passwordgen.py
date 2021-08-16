from random import randint

password_base = 0

password_base = input("Input up to five words, separated by spaces, to use to generate your password: ")
password_base = password_base.split(' ')

password_base[:] = [s.replace('o', '0') for s in password_base]
password_base[:] = [s.replace('l', '1') for s in password_base]
password_base[:] = [s.replace('z', '2') for s in password_base]
password_base[:] = [s.replace('s', '5') for s in password_base]

print(password_base)

def generate_password():
    return 0