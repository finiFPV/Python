import os
from os.path import exists
from time import sleep


cwd = os.getcwd()
file_exists = exists(f'{cwd}\\save.txt')
clear = lambda: os.system('cls')

def aa():
    clear()
    nam = str(input("Name And Surname >>"))
    clear()
    tel = str(input("Telephone Number >>"))
    clear()
    desc = str(input("Description >>"))
    clear()
    f = open(f'save.txt', 'a+')
    f.write(f'Name: {nam}\n')
    f.write(f'Telephone: {tel}\n')
    f.write(f'Description: {desc}\n')
    f.write('----------------------------------------------------------------\n')
    f.close()
    print('Information Saved')
    sleep(2)
    clear()
    bb()

def bb():
    clear()
    print('1. Add An Entery To The Contacts')
    print('2. Display The Contact List')
    print('69. Exit')
    choice = int(input('>>'))
    if choice == 1:
        aa()
    elif choice == 2:
        view_contacts()
    elif choice == 69:
        quit()
    else:
        print('Please Enter A Valid Choise')
        sleep(2)
        clear()
        bb()

def view_contacts():
    clear()
    if os.path.isfile("save.txt"):
        f = open("save.txt")
        lines = f.readlines()
        for line in lines:
            print(line)
        def bbc():
            bc = str(input('Return To Main Menu? (y/n) >>'))
            if bc == 'y' or bc == 'Y':
                bb()
            elif bc == 'n' or bc == 'N':
                quit()
            else:
                print('Please Enter A Valid Choice!')
                sleep(2)
                clear()
                bbc()
        bbc()

    else:
        clear()
        print('No contacts found!')
        sleep(3)
        clear()
        bb()

bb()