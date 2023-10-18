## ---------------------------------------
## Function Imports
import os
from register_fuction import *
from customer_login import *
from employee_login import *
from pre_defined_products import *
## ---------------------------------------

## ---------------------------------------
## Users - Dictionary
users = {}
## ---------------------------------------

## All Code
while True:
    try: 
        ## ---------------------------------------
        ## Initial Menu
        print(f"======[4Disease Pharmacy]======")
        print(f"1. Customer")
        print(f"2. Employee")
        print(f"3. Exit")
        print(f" ")
        role_choice = int(input("Role Number: "))
        print(f"===============================")
        ## ---------------------------------------

        ## ---------------------------------------
        ## Customer Decision Path
        if role_choice == 1:
            print(f"Role: Customer.")
            print(f"")
            while True:
                try:
                    print(f"===============================")
                    print(f"1. Login")
                    print(f"2. Register")
                    print(f"3. Exit")
                    print(f"")

                    customer_select = int(input("Select: "))
                    print(f"===============================")

                    match customer_select:
                        case 1:
                                input("Press Enter to Continue...")
                                os.system("cls")
                                login_c(users)
                        case 2:
                                register(users)
                                input("Press Enter to Continue...")
                                os.system("cls")
                        case 3:
                            input("Press Enter to Continue...")
                            os.system("cls")
                            break
                        case _:
                            print(f"Invalid Option, try again.")
                            input("Press Enter to Continue...")
                            os.system("cls")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    print(f"===============================")
                    input("Press Enter to Continue...")
                    os.system("cls")
        ## ---------------------------------------

        ## ---------------------------------------
        ## Employee Decision Path
        elif role_choice == 2:
            print(f"Role: Employee.")
            login_e()
            ## print(f"===============================")
        ## ---------------------------------------

        ## ---------------------------------------
        ## Exit Code
        elif role_choice == 3:
            input("Press Enter to Continue...")
            os.system("cls")
            break
        ## ---------------------------------------

        ## ---------------------------------------
        ## Error Message
        else:
            print(f"Invalid Role. Please type Again.")
            input("Press Enter to Continue...")
            os.system("cls")
        ## ---------------------------------------
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        print(f"===============================")
        input("Press Enter to Continue...")
        os.system("cls")