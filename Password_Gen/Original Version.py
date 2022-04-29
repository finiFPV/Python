import string
import random
import os
import subprocess
from colorama import Fore
from time import sleep


hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
clear = lambda: os.system('cls')
m = string.digits
l = "!@#$%^&*()"


clear()

def aa():
    print(f"{Fore.CYAN}0. Generate A Password")
    print(f"{Fore.RED}6. Exit")
    u = int(input(f"{Fore.CYAN}>>"))
    if u == 0:
        clear()
        bb()
    elif u == 6:
        quit()
    else:
        clear()
        print(f"{Fore.RED}Please enter a valid choise!")
        sleep(2)
        clear()
        aa()

def bb():
    print(f"{Fore.CYAN}Enter the passwords lengtht:")
    length = int(input(f"{Fore.CYAN}>>"))
    clear()
    print(f"{Fore.CYAN}Generation options:")
    print(f"{Fore.CYAN}0. Only Letters")
    print(f"{Fore.CYAN}1. Only Digits")
    print(f"{Fore.CYAN}2. Only Punctuation")
    print(f"{Fore.CYAN}3. Letters And Digits")
    print(f"{Fore.CYAN}4. Letters And Punctuation")
    print(f"{Fore.CYAN}5. Digits And Punctuation")
    print(f"{Fore.CYAN}6. Letters, Digits And Punctuation")
    d = int(input(f"{Fore.CYAN}>>"))
    clear()
    if d == 0 or d == 1 or d == 2 or d == 4:
        print(f"{Fore.CYAN}Do You want the letters to be:")
        print(f"{Fore.CYAN}0. Lovercase")
        print(f"{Fore.CYAN}1. Uppercase")
        print(f"{Fore.CYAN}2. Both")
        g = int(input(f"{Fore.CYAN}>>"))
        if g == 0:
            t = string.ascii_lowercase
        elif g == 1:
            t = string.ascii_uppercase
        elif g == 2:
            t = string.ascii_letters
        else:
            print(f"{Fore.RED}Please enter a valid choise!")
    clear()
    if d == 0:
        x = list(t)
    elif d == 1:
        x = list(t + m)
    elif d == 2:
        x = list(t + l)
    elif d == 3:
        x = list(m + l)
    elif d == 4:
        x = list(t + m + l)
    else:
        print(f"{Fore.RED}Please enter a valid choise!")
    random.shuffle(x)
    y = []
    for i in range(length):
        y.append(random.choice(x))
    random.shuffle(y)
    print("".join(y)) #The outputed password
    sleep(5)
    clear()
    cc()

def cc():
    print(f"{Fore.CYAN}Do you want to save it to an encrypted file? (y/n") 
    k = str(input(">>"))
    clear()
    if k == 'y':
        clear()
        #WORK ON THIS SHIT
    elif k == 'n':
        aa()
    else:
        print(f"{Fore.RED}Please enter a valid choise!")
        sleep(2)
        clear()
        cc()
aa()