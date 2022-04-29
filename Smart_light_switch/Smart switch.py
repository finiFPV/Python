import datetime
import os
from os.path import exists
from time import sleep
from colorama import Fore


now = datetime.datetime.now()
cwd = os.getcwd()
file_exists = exists(f'{cwd}\\settings.txt')
clear = lambda: os.system('cls')

clear()
def ac():
    print(f"{Fore.CYAN}0. Cheack if the switch is on")
    print(f"{Fore.CYAN}1. Change settings")
    print(f"{Fore.RED}8. Exit")
    z = int(input(f"{Fore.CYAN}>>"))
    if z == 0:
        cc()
    elif z == 1:
        bc()
    elif z == 8:
        dc()
    else:
        print(f"{Fore.RED}Please enter a valid choise.")
        sleep(5)
        ac()
          
def bc():
    clear()
    x = str(input(f"{Fore.CYAN}When to turn on the switch >>"))
    clear()
    y = str(input(f"{Fore.CYAN}When to turn off the switch >>"))
    f = open("settings.txt", "w")
    a = str(x).zfill(2)
    b = str(y).zfill(2)
    f.write(a)
    f.write(' ')
    f.write(b)
    f.close()
    clear()
    ac()

def cc():
    with open('settings.txt', 'r') as f:
        k = f.readline()
        j = f.readline()
        f.close()
        h = now.strftime("%H")
        if k <= h:
            clear()
            print(f"{Fore.CYAN}The switch is on")
            sleep(3)
            clear()
            ac()
        elif j >= h:
            clear()
            print(f"{Fore.CYAN}The switch is on")
            sleep(3)
            clear()
            ac()
        elif k >= h:
            clear()
            print(f"{Fore.CYAN}The switch is off")
            sleep(3)
            clear()
            ac()
        elif j <= h:
            clear()
            print(f"{Fore.CYAN}The switch is off")
            sleep(3)
            clear()
            ac()
        else:
            clear()
            print(f"{Fore.RED}Error!")
            sleep(3)
            clear()
            ac()

def dc():
    quit()


if file_exists == True:
    ac()
else:
    bc()