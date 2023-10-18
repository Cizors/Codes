import os
from pre_defined_products import *

def add_products():
    while True:
        try:
            print(f"===========[New Product]===========")
            new_p_name = str(input(f"Name: "))
            new_p_stripe = str(input(f"Stripe: "))
            new_p_price = float(input(f"R$"))
            new_p_quantity = int(input(f"Quantity: "))

            product_name.append(new_p_name)
            product_stripe.append(new_p_stripe)
            product_price.append(new_p_price)
            product_quantity.append(new_p_quantity)

            print(f"New Product Registered with Success!")
            print(f"====================================")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print(f"====================================")
            input("Press Enter to Continue...")
            os.system("cls")

        while True:
            answer = input("Do you want to add another product [Y/N]? ")
            print(f"")
            if answer.lower() == 'n':
                input("Press Enter to Exit...")
                os.system("cls")
                return
            elif answer.lower() == 'y':
                input("Press Enter to Continue...")
                os.system("cls")
                break  # Continue adding new products
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
                input("Press Enter to Continue...")
                os.system("cls")
            