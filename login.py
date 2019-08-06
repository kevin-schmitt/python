# Simple authentification with strong crypt password python3
import getpass
import crypt

SALT = crypt.mksalt(crypt.METHOD_SHA512)
PWD = {'GLMF' : crypt.crypt('Python3', SALT) }

def login():
    username = input('Login: ')
    password = crypt.crypt(getpass.getpass(), SALT)

    if username in PWD and password == PWD[username] :
        return True
    else:
        return False

if login():
    print('Acces authorise')
else:
    print('Acces not authorize')
