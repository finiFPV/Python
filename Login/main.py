from util.register import *
from colorama import Fore
from time import sleep
from os.path import exists
import os

clear = lambda: os.system('cls')
cwd = os.getcwd()

clear()
def start_menu():
    clear()
    print(f'{Fore.CYAN}1. Login')
    print(f'{Fore.CYAN}2. Register')
    print(f'{Fore.RED}0. Exit')
    start_choise = str(input(f'{Fore.CYAN}>>'))
    clear()
    if start_choise == '1':
        clear()
        #WORK ON THIS
    elif start_choise == '2':
        register()
        clear()
        start_menu()
    elif start_choise == '0':
        clear()
        quit()
    else:
        print(f'{Fore.RED}Please enter a valid choice! (1,2,0)')
        sleep(2)
        clear()
        start_menu()

def auto_run():
    if os.path.isfile(f'{cwd}\\util\\database.txt'):
        start_menu()
    elif not os.path.isfile(f'{cwd}\\util\\database.txt'):
        f = open('util\\database.txt', 'a+')
        os.system("attrib +h util\\database.txt")
        f.close()
        start_menu()
    else:
        print(f'{Fore.RED}Databse creatition error!')
        sleep(2)
        quit()
    
if __name__ == "__main__":
    auto_run()