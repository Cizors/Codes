import os
from menu_options import employee_options

def login_e():
    print(f"=====================[Login]=====================")
    username_login = input("Username: ")
    password_login = input("Password: ")

    if username_login == "4Disease" and password_login == "admin":
        print(f"Logged with Sucess!")
        print(f"==================================================")
        input("Press Enter to Continue...")
        os.system("cls")
        employee_options()
    else:
        print(f"Incorrect username or password, please type again.")
        print(f"==================================================")
        input("Press Enter to Continue...")
        os.system("cls")