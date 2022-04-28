from decimal import Decimal
from time import sleep
percentage = Decimal('0')
step = Decimal('0.01')
while True:
   percentage += step
   print(percentage)
   sleep(0.1)
