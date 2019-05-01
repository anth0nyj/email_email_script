# Dependencies
import smtplib
import getpass
from pathlib import Path

# Get Login Credentials

def createToken(**kwargs):
    if kwargs:
        return kwargs['file_creds']
    else:
        token = dict({'name': None, 'email_addr': None, 'pw': None})
        token.update({
            'name': input("Enter your name: "),
            'email_addr': input("Enter your email address: "),
            'pw': getpass.getpass("Enter your password: ")
        })
        return token
    return token


def obtainCreds():
    try:
        login_creds = Path("./login_creds")
        if login_creds:
            from login_creds import LoginCreds
            file_creds = LoginCreds()
            use_file_response = None
            while (use_file_response != 'y' and use_file_response != 'n'):
                use_file_response = input("A login credential file for \"" + file_creds.email_addr + "\"  has been found. Would you like to use this to log in? [y/n]: ")
                if use_file_response == 'y':
                    token = createToken(file_creds=file_creds)
                    return token
                elif use_file_response == 'n':
                    token = createToken()
                    return token
                else:
                    print("Please submit a valid response.")
            return token
        return token
    except:
        print("No login credential file found.")
    if token:
        return token

creds = obtainCreds()

# Start/Configure SMTP Server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()

# Use credentials to login
server.login(getattr(creds, 'email_addr'), getattr(creds, 'pw'))

# Compose email
rec_addr = input("Enter recipient email: ")
msg_subj = input("Enter a subject line: ")
msg_body = input("Enter the body of your email: ")

# Format input to create email
msg = (f"""From: {getattr(creds, 'name')} <{getattr(creds, 'email_addr')}>
To: <{rec_addr}>
Subject: {msg_subj}

{msg_body}""")

# Send email
server.sendmail(getattr(creds, 'email_addr'), rec_addr, msg)

# Close server
server.quit()
