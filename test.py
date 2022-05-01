import random
import string

code = []
digits = list(string.digits)

verif1 = str(input('Enter the verification code sent to your email.'))
print(verif1)
for i in range(6):
    code.append(random.choice(digits))
random.shuffle(code)
result = str("".join(code))
print(result)