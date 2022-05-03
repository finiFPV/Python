import smtplib
from email.message import EmailMessage
from colorama import Fore
from time import sleep
import json
import os

clear = lambda: os.system("cls")


def settings():
    with open("util\\settings.json", "r") as settings_file:
        global subject
        global content
        global content2
        global email_from
        global email_password
        settings = json.loads(settings_file.read())
        subject = settings["subject"]
        content = settings["content"]
        content2 = settings["content2"]
        email_from = settings["email"]
        email_password = settings["password"]
    settings_file.close()


def send_message(email, result):
    settings()
    msg = EmailMessage()
    msg.set_content(f"{content}{result}{content2}")
    msg["Subject"] = subject
    msg["From"] = email_from
    msg["To"] = email

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com")
        server.login(email_from, email_password)
        server.send_message(msg)
        server.quit()

    except:
        print(
            f"{Fore.RED}Error with sending the verification code! This may be because of an invalid email address or a problem with the email server. Please try again."
        )
        sleep(6)
        clear()
        exit()