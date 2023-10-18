import os

def register(users):

    print(f"======[Register]======")
    username = input("Username: ")
    password = input("Password: ")

    users[username] = password
    print(f"Registered with Sucess!")
    print(f"======================")