import os
from list_function import *
from buy_fuction import *
from edit_function import *
from remove_function import *
from add_function import *

def customer_options():
    while True:
        try:
            print(f"=====[Options]=====")
            print(f"1. Buy Products")
            print(f"2. Product List")
            print(f"3. Exit")

            customer_choice = int(input("Option: "))
            print(f"===================")

            match customer_choice:
                case 1:
                    input("Press Enter to Continue...")
                    os.system("cls")
                    buy_products()
                case 2:
                    input("Press Enter to Continue...")
                    os.system("cls")
                    product_list()
                case 3:
                    input("Press Enter to Continue...")
                    os.system("cls")
                    break
                case _:
                    print(f"Invalid Option.")
                    input("Press Enter to Continue...")
                    os.system("cls")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print(f"===================")
            input("Press Enter to Continue...")
            os.system("cls")

def employee_options():
    while True:
        try:
            print(f"=====[Options]=====")
            print(f"1. Add Product")
            print(f"2. Edit Product")
            print(f"3. Remove Product")
            print(f"4. Product List")
            print(f"5. Exit")

            employee_choice = int(input("Option: "))
            print(f"===================")

            match employee_choice:
                case 1:
                    input("Press Enter to Continue...")
                    os.system("cls")
                    add_products()
                case 2:
                    input("Press Enter to Continue...")
                    os.system("cls")
                    edit_products()
                case 3:
                    input("Press Enter to Continue...")
                    os.system("cls")
                    remove_products()
                case 4: 
                    input("Press Enter to Continue...")
                    os.system("cls")
                    product_list()
                case 5:
                    input("Press Enter to Continue...")
                    os.system("cls")
                    break
                case _:
                    print(f"Invalid Option.")
                    input("Press Enter to Continue...")
                    os.system("cls")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print(f"===================")
            input("Press Enter to Continue...")
            os.system("cls")