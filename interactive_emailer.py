# Dependencies
import smtplib
import getpass

# Get Login Credentials
from pathlib import Path
try:
    login_creds = Path("./login_creds")
    if login_creds:
        from login_creds import LoginCreds
        login = LoginCreds()
        email_addr = login.email_addr
        pw = login.pw
        name = login.name
except:
    print("No login file found.")

# Start/Configure SMTP Server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()

# Use login credentials if they exist
if 'email_addr' in locals():
    send_addr = email_addr
    send_pw = pw
    send_name = name
# If no creds exist, enter them
else:
    send_name = input("Enter your name: ")
    send_addr = input("Enter your email: ")
    send_pw = getpass.getpass("Enter your password: ")

# Use credentials to login
server.login(send_addr, send_pw)

# Compose email
rec_addr = input("Enter recipient email: ")
msg_subj = input("Enter a subject line: ")
msg_body = input("Enter the body of your email: ")

# Format input to create email
msg = (f"""From: {send_name} <{send_addr}>
To: <{rec_addr}>
Subject: {msg_subj}

{msg_body}""")

# Send email
server.sendmail(send_addr, rec_addr, msg)

# Close server
server.quit()
