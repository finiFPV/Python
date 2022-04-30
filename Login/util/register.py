from colorama import Fore
from time import sleep
import os
import re


password_valid = True
email_valid = True
clear = lambda: os.system('cls')
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


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

def email_invalid():
    print(f"{Fore.RED}The email is invalid! Please enter a valid email address.")
    sleep(2)
    clear()
    email_save()

def email_save():
    global email
    email = input(f'{Fore.CYAN}Enter your email address. >>')
    while email_valid == False:
        email_invalid(email)
    

def email_cheack(email):
    if(re.fullmatch(regex, email)):
        email_valid = True
        print(email)
    else:
        email_valid = False
        email_invalid()

def register():
    clear()
    user_name = str(input(f'{Fore.CYAN}Enter your username. >>'))
    user_save = str(f'Username: {user_name}.a#11end11#a.')
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
    email_save()

    clear()