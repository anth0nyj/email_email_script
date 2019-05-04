# Dependencies
import smtplib
import getpass
from pathlib import Path
import pdb


# Get Login Credentials

def createToken():
    from logintoken import LoginToken
    name = input("Enter your name: ")
    addr = input("Enter your email address: ")
    pw = getpass.getpass("Enter your password: ")
    token = LoginToken(addr, pw, name)
    return token

# Pull credentials from local file if possible. Otherwise, prompt cred entry.
def obtainToken():
    token = None
    # First, try to find and use cred file.
    try:
        if Path("./login_creds").exists:
            from login_creds import login_token
            # Give user option to use file or manually enter creds.
            use_file_res = None
            while (use_file_res != 'y' and use_file_res != 'n'):
                use_file_res = input("A login credential file for \"" + getattr(login_token, 'addr') + "\"  has been found. Would you like to use this to log in? [Y/n]: ").lower() or 'y'
                if use_file_res.lower() == 'y':
                    return login_token
                elif use_file_res.lower() == 'n':
                    token = createToken()
                    return token
                else:
                    print("Please submit a valid response.")
            return token
        return token

    # Cred file not found. Prompt cred entry.
    except:
        print("No login credential file found.")
        return createToken()

    if token:
        return token

token = obtainToken()

# Start/Configure SMTP Server
print("Initializing server...")
server = smtplib.SMTP('smtp.gmail.com', 587)
print("Connecting server...")
server.connect("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()

# Use credentials to login
server.login(getattr(token, 'addr'), getattr(token, 'pw'))

# Compose email
rec_addr = input("Enter recipient email: ")
msg_subj = input("Enter a subject line: ")
msg_body = input("Enter the body of your email: ")

# Format input to create email
msg = (f"""From: {getattr(token, 'name')} <{getattr(token, 'addr')}>
To: <{rec_addr}>
Subject: {msg_subj}

{msg_body}""")

# Send email
server.sendmail(getattr(token, 'addr'), rec_addr, msg)

# Close server
server.quit()
