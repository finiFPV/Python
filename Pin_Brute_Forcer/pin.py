import os
import pyautogui
import threading
from time import sleep
from colorama import Fore

clear = lambda: os.system('cls')
clear()
y = int(input(f"{Fore.GREEN}Pin length >> "))
clear()

a = 5
x = 0

for i in range(5):
   print(a)
   a -= 1
   sleep(1)
   clear()

def Proc1():
   while True:
      global x
      x += 1
      z = str(x).zfill(y)
      pyautogui.write(z+"\n")
      print(z)
      sleep(0.13)

def Proc2():
   while True:
      global x
      x += 1
      z = str(x).zfill(y)
      pyautogui.write(z+"\n")
      print(z)
      sleep(0.13)

def Proc3():
   while True:
      global x
      x += 1
      z = str(x).zfill(y)
      pyautogui.write(z+"\n")
      print(z)
      sleep(0.13)

def Proc4():
   while True:
      global x
      x += 1
      z = str(x).zfill(y)
      pyautogui.write(z+"\n")
      print(z)
      sleep(0.13)

thread1 = threading.Thread(target=Proc1)
thread1.start()
sleep(0.13)

thread2 = threading.Thread(target=Proc2)
thread2.start()
sleep(0.13)

thread3 = threading.Thread(target=Proc3)
thread3.start()
sleep(0.13)

thread4 = threading.Thread(target=Proc4)
thread4.start()