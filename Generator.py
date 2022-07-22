import random

print('Welcome To Your Password Generator !!!')
print(' _                 _             _          ______        _  _            ')
print('| |               | |           | |         | ___ \      (_)| |           ')
print('| |__   _   _     | |     _   _ | |_   ___  | |_/ /  ___  _ | |__    ___  ')
print('|  _ \ | | | |    | |    | | | || __| / _ \ | ___ \ / _ \| ||  _ \  / _ \ ')
print('| |_) || |_| |    | |____| |_| || |_ | (_) || |_/ /|  __/| || |_) ||  __/ ')
print('|_.__/  \__, |    \_____/ \__,_| \__| \___/ \____/  \___||_||_.__/  \___| ')
print('         __/ |                                                            ')
print('        |___/                                                             ')                                                   

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@€$%^&*().,?0123456789'

number = input('\nAmount of passwords to generate: ')
number = int(number)

length = input('Input Your Password Length: ')
length = int(length)

print('here are your passwords: \n ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
