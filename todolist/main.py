import getpass
import bcrypt
from db.user_db import login, create_user
from menu.menu_principal import menu


# https://github.com/wagnerpalmeira/python-crypt-hiddenpass
# https://github.com/github/gitignore/blob/main/Python.gitignore


# Separar módulo
def criotpgrafar(password):
    bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(bytes, bcrypt.gensalt(14))
    return hashed


# Separar módulo
def checar_password(password, hashed):
    bytes = password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed)

is_authenticated = False



while(not is_authenticated):
     username = input("Digite seu usuário: ")
     password = getpass.getpass("Digite sua senha: ")
     # password = criotpgrafar(password)
     # create_user(username, password)


    # Not Good - Deveriamos enviar o password e descriptografar no login
     user = login(username)

     if user and checar_password(password, user[2]):
          menu(user)
     else:
          print("Usuário e senha inválidos!")