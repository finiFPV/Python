x = int(input("Number one:"))
y = int(input("Number two:"))
opp = input("Opperator:")

if opp == '+':
   print(x + y)
elif opp == '-':
   print(x-y)
elif opp == '*':
  print(x*y)
elif opp == '/':
    print(x/y)
else:
    print("Please enter a valid opperator")