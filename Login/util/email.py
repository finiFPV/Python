import smtplib
from email.message import EmailMessage

def send_message(email, result):
    msg = EmailMessage()
    msg.set_content(result)
    msg['Subject'] = 'Verification Code'
    msg['From'] = "fini.noreply@gmail.com"
    msg['To'] = email
   
    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("fini.noreply@gmail.com", "AGMA#PU28@~")
    server.send_message(msg)
    server.quit()