from util.email import *
from colorama import Fore
from time import sleep
import json
import os
import random
import string

clear = lambda: os.system("cls")
digits = list(string.digits)
password_match = False
pass_reset_scessfull = False
password_long = True
password_valid = True


clear()


def user_not_found(user_name):
    print(f'{Fore.RED}User: {user_name} Not Found!')
    sleep(3)


def passwords_notequal():
    print(f"{Fore.RED}The passwords dosen't match! Please enter them again.")
    sleep(2)
    clear()
    passwords_save()


def passwords_save():
    global password_long
    global password_new
    password_new = str(input(f"{Fore.CYAN}Enter your new password. >>"))
    clear()
    if len(password_new) < 4:
        password_long = False
        print(f"{Fore.RED}The password must be at least 4 characters long.")
        sleep(3)
        clear()
    else:
        password_long = True
        password2 = str(input(f"{Fore.CYAN}Enter your new password again. >>"))
        clear()
        global password_valid
        if password_new != password2:
            password_valid = False
        else:
            password_valid = True


def set_new_password(credentials, special_key):
    passwords_save()
    while password_long == False:
        passwords_save()
    while password_valid == False:
        passwords_notequal()
    credentials["password"] = password_new
    with open("util\\database.txt", "r") as current:
        data = current.readlines()
    write = str(f"{special_key}{credentials}")
    data[line_num] = write
    os.remove("util\\database.txt")
    with open("util\\database.txt", "a+") as file:
        file.writelines(data)
        


def pass_reset_func(credentials, special_key):
    global pass_reset_scessfull
    print(f"{Fore.CYAN}1. Reset your password.")
    print(f"{Fore.CYAN}2. Try again.")
    print(f"{Fore.CYAN}0. Exit.")
    pass_reset = str(input(f"{Fore.CYAN}>>"))
    clear()
    if pass_reset == '1':
        clear()
        email = credentials['email']
        code = []
        for i in range(6):
            code.append(random.choice(digits))
        random.shuffle(code)
        result = str("".join(code))
        send_message(email, result)
        verif1 = str(
        input(f"{Fore.CYAN}Enter the verification code sent to your email. >>")
        )
        clear()
        if result != verif1:
            pass_reset_scessfull = False
            print(f"{Fore.RED}Verfiction code is invalid. Sending the new code...")
            sleep(3)
            clear()
        else:
            set_new_password(credentials, special_key)
            pass_reset_scessfull = True
            return
    elif pass_reset == '2':
        pass_reset_scessfull = True
        return
    elif pass_reset == '0':
        quit()
    else:
        print(f'Please enter a valid option! (1/2/0)')
        sleep(3)
        clear()
        pass_reset_func(credentials, special_key)


def input_password(credentials, special_key):
    global password_match
    password = str(input(f"{Fore.CYAN}Enter your password. >>"))
    clear()
    if password != credentials['password']:
        print(f'{Fore.RED}Password incorrect!')
        sleep(3)
        clear()
        while pass_reset_scessfull == False:
            pass_reset_func(credentials, special_key)
        password_match = False
    else:
        password_match = True
        

def default_valeues():
    global password_match
    global pass_reset_scessfull
    global password_long
    global password_valid
    global user_faund
    password_match = False
    pass_reset_scessfull = False
    password_long = True
    password_valid = True
    user_faund = False
        
def login():
    global line_num
    global user_faund
    line_num = 0
    user_name = str(input(f"{Fore.CYAN}Enter your username. >>"))
    clear()
    special_key = str(f"fini.{user_name}.xyzdt28@~")
    with open("util\\database.txt", "r") as read:
        for lines in read:
            if special_key in lines:
                user_faund = True
                strip1 = lines.replace(f"{special_key}", "")
                strip2 = strip1.replace("'", '"')
                credentials = json.loads(strip2)
                break
            else:
                user_faund = False
            line_num += 1
    read.close()
    while user_faund == False:
        user_not_found(user_name)
        return
    while password_match == False:
        input_password(credentials, special_key)
    credentials_valid = credentials['user'] == user_name and password_match == True
    if credentials_valid == True:
        print(f'{Fore.CYAN}Login successfull!')
        sleep(2)
    default_valeues()