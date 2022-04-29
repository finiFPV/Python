import random
print("Starting number:")
x = int(input())
print("Ending number:")
y = int(input())
print("Guess the number between", x, "and", y, ":")
z = int(input())
n = random.randint(x,y)
if n == z:
  print("you guessed correctly!")
else:
   print("Wron, the number was:", n)