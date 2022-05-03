from validate_email_address import validate_email
from colorama import Fore
from time import sleep
from util.email import *
from util.save import save
import subprocess
import os
import random
import string
import datetime

now = datetime.datetime.now()
digits = list(string.digits)
password_long = True
password_valid = True
email_valid = False
clear = lambda: os.system("cls")
email_exists = False
hardwareid = (
    subprocess.check_output("wmic csproduct get uuid").decode().split("\n")[1].strip()
)


clear()


def email_verify(email):
    code = []
    global email_valid
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
        email_valid = False
        print(f"{Fore.RED}Verfiction code is invalid. Sending the new code...")
        sleep(3)
        clear()
    else:
        email_valid = True


def passwords_notequal():
    print(f"{Fore.RED}The passwords dosen't match! Please enter them again.")
    sleep(2)
    clear()
    passwords_save()


def passwords_save():
    global password_long
    global password1
    password1 = str(input(f"{Fore.CYAN}Enter your password. >>"))
    clear()
    if len(password1) < 4:
        password_long = False
        print(f"{Fore.RED}The password must be at least 4 characters long.")
        sleep(3)
        clear()
    else:
        password_long = True
        password2 = str(input(f"{Fore.CYAN}Enter your password again. >>"))
        clear()
        global password_valid
        if password1 != password2:
            password_valid = False
        else:
            password_valid = True


def user_taken():
    clear()
    print(f"{Fore.RED}Username is already taken! Please use a different username.")
    sleep(2)
    clear()
    register()


def email_unvalidate():
    global email_valid
    global email_exists
    email_exists = False
    email_valid = False


def email_dosent_exist():
    clear()
    print(
        f"{Fore.RED}Email is doesn't exist! Please verify that you typed in the email correctly."
    )
    sleep(3)
    clear()


def input_email():
    global email
    global email_exists
    email = input(f"{Fore.CYAN}Enter your email address. >>")
    email_exists = validate_email(email)
    if email_exists == False:
        email_dosent_exist()
        email_exists = False
    else:
        email_exists = True
    clear()


def register():
    clear()
    user_name = str(input(f"{Fore.CYAN}Enter your username. >>"))
    special_key = str(f"fini.{user_name}.xyzdt28@~")
    with open("util\\database.txt", "r") as read:
        for lines in read:
            if special_key in lines:
                user_taken()
                return
    read.close()
    clear()
    passwords_save()
    while password_long == False:
        passwords_save()
    while password_valid == False:
        passwords_notequal()
    while email_exists == False:
        input_email()
    while email_valid == False:
        email_verify(email)
    membership = "none"
    admin = False
    owner = False
    level = 0
    time = str(now.strftime("%Y-%m-%d %H:%M:%S"))
    save(
        user_name,
        password1,
        email,
        hardwareid,
        membership,
        admin,
        owner,
        time,
        level,
        special_key,
    )
    print(f"{Fore.CYAN}Registered successfully! You can login now.")
    sleep(3)
    clear()
    email_unvalidate()
    return