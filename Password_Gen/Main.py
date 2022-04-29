import string
import random
import os
import subprocess
from colorama import Fore
from time import sleep
from os.path import exists
from cryptography.fernet import Fernet

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
clear = lambda: os.system('cls')
cwd = os.getcwd()
enc_exists = exists(f'{cwd}\\enc.txt')
key_exists = exists(f'{cwd}\\key.key')
clear()


def aa():
   print(f"{Fore.CYAN}0. Generate A Password")
  # print(f"{Fore.CYAN}1. Encrypt/Decrypt The saved Passwords")
   print(f"{Fore.RED}6. Exit")
   choise = int(input(f"{Fore.CYAN}>>"))
   if choise == 0:
       clear()
       generate_random_password()
 #  elif choise == 1:
 #     clear()
 #     dd()
   elif choise == 6:
       quit()
   else:
       clear()
       print(f"{Fore.RED}Please enter a valid choise!")
       sleep(2)
       clear()
       aa()
def generate_random_password():
   print(f"{Fore.CYAN}Passwords Length")
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
   generation_options = int(input(f"{Fore.CYAN}>>"))
   clear()
   if generation_options != 0 and generation_options != 1 and generation_options != 2 and generation_options != 3 and generation_options != 4 and generation_options != 5 and generation_options != 6:
      print(f"{Fore.RED}Please Enter A Valid Option!")
      length = 0
      generation_options = 0
      sleep(2)
      clear()
      generate_random_password()
   if generation_options == 0 or generation_options == 3 or generation_options == 4 or generation_options == 6:
        print(f"{Fore.CYAN}Do You want the letters to be:")
        print(f"{Fore.CYAN}0. Lovercase")
        print(f"{Fore.CYAN}1. Uppercase")
        print(f"{Fore.CYAN}2. Both")
        letters = int(input(f"{Fore.CYAN}>>"))
        if letters == 0:
            case = string.ascii_lowercase
        elif letters == 1:
            case = string.ascii_uppercase
        elif letters == 2:
            case = string.ascii_letters
        else:
            print(f"{Fore.RED}Please enter a valid choise!")
   clear()

   if generation_options == 0 or generation_options == 3 or generation_options == 4 or generation_options == 6:
      alphabets = list(case)
      characters = list(case + string.digits + "!@#$%^&*()")
   digits = list(string.digits)
   special_characters = list("!@#$%^&*()")

   password = []

   def a0():
      for i in range(alphabets_count):
         password.append(random.choice(alphabets))
      if characters_count < length:
         random.shuffle(alphabets)
         for i in range(length - characters_count):
            password.append(random.choice(alphabets))
      
   def a1():
      for i in range(digits_count):
         password.append(random.choice(digits))
      if characters_count < length:
         random.shuffle(digits)
         for i in range(length - characters_count):
            password.append(random.choice(digits))

   def a2():
      for i in range(special_characters_count):
         password.append(random.choice(special_characters))
      if characters_count < length:
         random.shuffle(special_characters)
         for i in range(length - characters_count):
            password.append(random.choice(special_characters))
   
   def a3():
      alphadig = list(case + string.digits)
      for i in range(alphabets_count):
         password.append(random.choice(alphabets))
      for i in range(digits_count):
         password.append(random.choice(digits))
      if characters_count < length:
         random.shuffle(alphadig)
         for i in range(length - characters_count):
            password.append(random.choice(alphadig))
   
   def a4():
      alphapunc = list(case + "!@#$%^&*()")
      for i in range(alphabets_count):
         password.append(random.choice(alphabets))
      for i in range(special_characters_count):
         password.append(random.choice(special_characters))
      if characters_count < length:
         random.shuffle(alphapunc)
         for i in range(length - characters_count):
            password.append(random.choice(alphapunc))
   
   def a5():
      digipunc = list(string.digits + "!@#$%^&*()")
      for i in range(digits_count):
         password.append(random.choice(digits))
      for i in range(special_characters_count):
         password.append(random.choice(special_characters))
      if characters_count < length:
         random.shuffle(digipunc)
         for i in range(length - characters_count):
            password.append(random.choice(digipunc))

   def a6():
      for i in range(alphabets_count):
         password.append(random.choice(alphabets))
      for i in range(digits_count):
         password.append(random.choice(digits))
      for i in range(special_characters_count):
         password.append(random.choice(special_characters))
      if characters_count < length:
         random.shuffle(characters)
         for i in range(length - characters_count):
            password.append(random.choice(characters))
   
         
   if generation_options == 0:
      alphabets_count = length
      clear()
      characters_count = alphabets_count
      a0()
   elif generation_options == 1:
      digits_count = length
      clear()
      characters_count = digits_count
      a1()
   elif generation_options == 2:
      special_characters_count = length
      clear()
      characters_count = special_characters_count
      a2()
   elif generation_options == 3:
      print(f"{Fore.CYAN}Letter Count")
      alphabets_count = int(input(f"{Fore.CYAN}>>"))
      clear()
      print(f"{Fore.CYAN}Digit Count")
      digits_count = int(input(f"{Fore.CYAN}>>"))
      clear()
      characters_count = alphabets_count + digits_count
      a3()
   elif generation_options == 4:
      print(f"{Fore.CYAN}Letter Count")
      alphabets_count = int(input(f"{Fore.CYAN}>>"))
      clear()
      print(f"{Fore.CYAN}Punctuation Count")
      special_characters_count = int(input(f"{Fore.CYAN}>>"))
      clear()
      characters_count = alphabets_count + special_characters_count
      a4()
   elif generation_options == 5:
      print(f"{Fore.CYAN}Digit Count")
      digits_count = int(input(f"{Fore.CYAN}>>"))
      clear()
      print(f"{Fore.CYAN}Punctuation Count")
      special_characters_count = int(input(f"{Fore.CYAN}>>"))
      clear()
      characters_count = digits_count + special_characters_count
      a5()
   elif generation_options == 6:
      print(f"{Fore.CYAN}Letter Count")
      alphabets_count = int(input(f"{Fore.CYAN}>>"))
      clear()
      print(f"{Fore.CYAN}Digit Count")
      digits_count = int(input(f"{Fore.CYAN}>>"))
      clear()
      print(f"{Fore.CYAN}Punctuation Count")
      special_characters_count = int(input(f"{Fore.CYAN}>>"))
      clear()
      characters_count = alphabets_count + digits_count + special_characters_count
      a6()

   if characters_count > length:
      print(f"{Fore.RED}Characters total count is greater than the password length!")
      characters_count = 0
      length = 0
      alphabets_count = 0 
      digits_count = 0
      special_characters_count = 0
      sleep(2)
      clear()
      generate_random_password()

   random.shuffle(password)
   print(f"{Fore.MAGENTA}")
   global result
   result = str("".join(password))
   print(result)
   sleep(5)
   clear()
   cc()


def cc():
   print(f"{Fore.CYAN}Do you want to save it to an encrypted file? (y/n)") 
   k = str(input(">>"))
   clear()
   if k == 'y':
      clear()
      f = open(f"{cwd}\\passwords.txt", "a+")
      f.write(f'{result}\n')
      f.close()
      aa()
   elif k == 'n':
       aa()
   else:
       print(f"{Fore.RED}Please enter a valid choise!")
       sleep(2)
       clear()
       cc()

""" def dd():
   if enc_exists == False:
      f = open(f"{cwd}\\enc.txt", "a+")
      f.write('False')
      os.system("attrib +h enc.txt")
      f.close
   f = open(f"{cwd}\\enc.txt", "a+")
   line = f.readline()
   f.close
   if line == 'False':
      print(f"{Fore.RED}Passwords Aren't Encrypted! Do You Want To Encrypt Them? (y/n)")
      choise = str(input(f"{Fore.CYAN}>>"))
      if choise == 'y' or choise == 'Y':
         #os.system("attrib +h passwords.txt")
         print(f"{Fore.CYAN}File Successfully Encrypted")
         f = open(f"{cwd}\\enc.txt", "w+")
         f.write('True')
         f.close
         sleep(4)
         clear()
         aa()
      elif choise == 'n' or choise == 'N':
         clear()
         aa()
      else:
         print(f"{Fore.RED}Please Enter A Valid Choise!")
         sleep(2)
         clear()
         dd()
   elif line == 'True':
      print(f"{Fore.RED}Passwords Are Encrypted! Do You Want To Unencrypt Them? (y/n)")
      choise = str(input(f"{Fore.CYAN}>>"))
      if choise == 'y' or choise == 'Y':
         os.system("attrib -h passwords.txt")
         print(f"{Fore.CYAN}File Successfully Unencrypted")
         f = open(f"{cwd}\\enc.txt", "w+")
         f.write(False)
         f.close
         sleep(4)
         clear()
         aa()
      elif choise == 'n' or choise == 'N':
         clear()
         aa()
      else:
         print(f"{Fore.RED}Please Enter A Valid Choise!")
         sleep(2)
         clear()
         dd()
   else:
      print(line)
      print(f"{Fore.RED}File Read Error!")
      aa()
      """
aa()