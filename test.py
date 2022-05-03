import datetime
import subprocess

now = datetime.datetime.now()
save = []
hardwareid = (
    subprocess.check_output("wmic csproduct get uuid").decode().split("\n")[1].strip()
)

user_save = 'fini'
password_save = '12345678'
email_save = 'markusskalenda@gmail.com'
bitcoin_save = 'bc1qkycn37yy93flg5xw9dx0l2nfcq8jp5wk5jm2r0'
hwid_save = hardwareid
membership = 'none'
admin = 'false'
owner = 'false'
time = time = str(now.strftime("%Y-%m-%d %H:%M:%S"))

save = [user_save, password_save, email_save,bitcoin_save, hwid_save, membership, admin, owner, time]

with open("database.txt", "a+") as save_database:
        save_database.write(f'{user_save}.xyzabc123qwe{save}')
        save_database.write("\n")
save_database.close()
with open("database.txt", "r") as read:
    for read_lines in read:
        lines = read.readline()

    
read.close()
x = lines.replace(f'{user_save}.xyzabc123qwe', '')
z = x.replace('[', '')
y = z.replace(']', '')
q = y.replace("'", "")
v = q.split(",")
print(v[0])
