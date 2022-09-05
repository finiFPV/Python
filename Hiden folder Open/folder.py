import os, maskpass
while True:
    password = maskpass.askpass('>> ')
    if password == 'Your Password':
        os.system('start Z:\\Data')
        break