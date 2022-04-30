from colorama import Fore
from time import sleep
import os


password_valid = True
clear = lambda: os.system('cls')


clear()

def passwords_notequal():
    print(f"{Fore.RED}The passwords dosen't match! Please enter them again.")
    sleep(2)
    clear()
    passwords_save()

def passwords_save():
    global password1
    password1 = str(input(f'{Fore.CYAN}Enter your password. >>'))
    clear()
    global password2
    password2 = str(input(f'{Fore.CYAN}Enter your password again. >>'))
    clear()
    global password_valid
    if password1 != password2:
        password_valid = False
    else:
        password_valid = True
        
def user_taken():
    clear()
    print(f'{Fore.RED}Username is already taken! Please use a different username.')
    sleep(2)
    clear()
    register()


def register():
    clear()
    user_name = str(input(f'{Fore.CYAN}Enter your username. >>'))
    user_save = str(f'Username: {user_name}')
    with open('util\\database.txt', 'r') as reg:
        for line in reg:
            if user_save in line:
                user_taken()
                return
    reg.close()
    clear()
    passwords_save()
    while password_valid == False:
        passwords_notequal()
    clear()