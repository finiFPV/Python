from colorama import Fore
from time import sleep
from util.email import *
import subprocess
import os
import random
import string

digits = list(string.digits)
password_valid = True
email_valid = False
clear = lambda: os.system("cls")
hardwareid = (
    subprocess.check_output("wmic csproduct get uuid").decode().split("\n")[1].strip()
)


clear()


def save():
    with open("util\\database.txt", "a+") as save:
        save.write(f"{user_save}\n")
        save.write(f"{password_save}\n")
        save.write(f"{email_save}\n")
        save.write(f"{bitcoin_save}\n")
        save.write(f"{hwid_save}\n")
        save.write(f"Membership: none.membership.{special_key}\n")
        save.write(f"Admin: false.admin.{special_key}\n")
        save.write(f"Owner: false.status.{special_key}\n")
        save.write("\n")
    save.close()


def email_verify(email):
    code = []
    global email_valid
    global verif1
    global result
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
    global password1
    password1 = str(input(f"{Fore.CYAN}Enter your password. >>"))
    clear()
    global password2
    password2 = str(input(f"{Fore.CYAN}Enter your password again. >>"))
    clear()
    global password_valid
    if password1 != password2:
        password_valid = False
    else:
        global password_save
        password_save = str(f"Password: {password1}.password.{special_key}")
        password_valid = True


def user_taken():
    clear()
    print(f"{Fore.RED}Username is already taken! Please use a different username.")
    sleep(2)
    clear()
    register()


def email_taken():
    print(f"{Fore.RED}Email is already taken! Please use a different email address.")


def email_unvalidate():
    global email_valid
    email_valid = False


def register():
    clear()
    global user_name
    user_name = str(input(f"{Fore.CYAN}Enter your username. >>"))
    global special_key
    special_key = str(f"{user_name}.xyzdt28@~")
    global user_save
    user_save = str(f"Username: {user_name}.username.xyzdt28@~")
    with open("util\\database.txt", "r") as reg:
        for line in reg:
            if user_save in line:
                user_taken()
                return
    reg.close()
    clear()
    passwords_save()
    while password_valid == False:
        passwords_notequal()
    email = input(f"{Fore.CYAN}Enter your email address. >>")
    global email_save
    email_save = str(f"Email: {email}.email.{special_key}")
    with open("util\\database.txt", "r") as reg:
        for line in reg:
            if email_save in line:
                user_taken()
                return
    clear()
    bitcoin_address = input(
        f"{Fore.CYAN}Enter your bitcoin address. Leave empty if you dont have one. >>"
    )
    clear()
    global bitcoin_save
    bitcoin_save = str(f"BTC Address: {bitcoin_address}.btc.{special_key}")
    global hwid_save
    hwid_save = str(f"HWID: {hardwareid}.hwid.{special_key}")
    clear()
    while email_valid == False:
        email_verify(email)
    save()
    print(f"{Fore.CYAN}Registered successfully! You can login now.")
    sleep(3)
    clear()
    email_unvalidate()
    return


# to find database enteries {something}.credential_type.{user_name}.xyzdt28@~