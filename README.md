# Bruteforce
Bruteforce Attacker - Stole your Password


usage: bruteforce.py [-h] [-v]
                     url name_email name_pass xpath_login title filePath
                     fireFox_path

Bruteforce Attacker - Stole your password

positional arguments:
  url            Url of the Website
  name_email     Move your cursor to email column and click on inspect Element
                 and copy name of email element
  name_pass      Move your cursor to password column and click on inspect
                 Element and copy name of password element
  xpath_login    Move your cursor to login/Signin button and click on inspect
                 Element and copy xpath of button element
  title          Title of page that open after successful in login
  filePath       file name containing Usernames and Password in xlsx format
  fireFox_path   Your firefox browser path

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
