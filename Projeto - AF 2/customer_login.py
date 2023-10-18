import os
from menu_options import customer_options

def login_c(users):
    print(f"=====================[Login]=====================")
    username_login = input("Username: ")
    password_login = input("Password: ")

    if username_login in users and users[username_login] == password_login:
        print(f"Logged with Success!")
        print(f"==================================================")
        input("Press Enter to Continue...")
        os.system("cls")
        customer_options()
    else:
        print(f"Incorrect username or password, please type again.")
        print(f"==================================================")
        input("Press Enter to Continue...")
        os.system("cls")