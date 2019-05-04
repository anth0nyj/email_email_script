# This is a template for storing your login credentials. To use it, enter your information in the appropriate fields, and then change the filename from "login_creds_template.py" to "login_creds.py". Eventually, I may add features that generate this file for you, but until then, it's hardcoded in the first manner that came to mind.

# Note: this is not a necessary step. The script itself allows you to forgo using this file entirely and enter your credentials at runtime. I just found that really tedious, and figured this was a simple fix.

class LoginToken:
    def __init__(self, addr, pw, name):
        self.addr = addr
        self.pw = pw
        self.name = name
