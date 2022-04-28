import random
import keyboard
from time import sleep

b = True
print("Press r to roll the dice!")

while b == True:
    if keyboard.is_pressed("r"):
        print(random.randint(1,6))
        sleep(0.2)
        