import os
from unicodedata import decimal
from colorama import Fore
from time import sleep
import keyboard
import datetime
from decimal import Decimal

clear = lambda: os.system('cls')

clear()
def start(): 
    print(f"{Fore.CYAN}0. Timer")
    print("1. Chronometer")
    print("2. Clock")
    print(f"{Fore.RED}5. Exit")
    x = int(input(f"{Fore.CYAN}>>"))
    if x == 0:
        clear()
        y = int(input("Timer lenght >>"))
        while y >= 0:
            clear()
            print(y)
            y -= 1
            sleep(1)
        clear()
        start()
    elif x == 1:
        print("Press 1 to stop")
        z = Decimal('0')
        a = Decimal('0.1')
        sleep(1)
        while True:
            clear()
            print(z)
            z += a
            if keyboard.is_pressed("1"):
                clear()
                start()
            sleep(0.01)
    elif x == 2:
        now = datetime.datetime.now()
        clear()
        print ("Current date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        sleep(5)
        clear()
        start()
    elif x == 5:
        quit()
    else:
        clear()
        print(f"{Fore.RED}Please enter a valid option!")
        sleep(1)
        clear()
        start()

start()