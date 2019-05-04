# This is a template for storing your login credentials. To use it, enter your information in the appropriate fields, and then change the filename from "login_creds_template.py" to "login_creds.py" (don't worry; that filename is included in the .gitgnore). Eventually, I may add features that generate this file for you, but until then, it's hardcoded.

# NOTE: this is not a necessary step, rather merely a convenience. The script itself allows you to forgo using this file entirely and enter your login credentials at run time.

from logintoken import LoginToken

login_token = LoginToken(addr='you@you.com', pw='yourpassword', name='yourname')

