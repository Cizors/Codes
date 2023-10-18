import os
from pre_defined_products import *

## product_name, product_stripe, product_price, product_quantity = stock()

def buy_products():
    while True:
        try:
            counter = 1

            print(f"=======[Buy Products]=======")

            for p_name in product_name:
                print(f"{counter}. {p_name}")

                counter = counter + 1

            p_select = int(input(f"Select: "))

            if p_select < 1 or p_select > len(product_name):
                print(f"Invalid Product. Type Again.")
                print(f"============================")
                input(f"Press Enter to Continue...")
                os.system("cls")
            else:
                input(f"Press Enter to Continue...")
                os.system("cls")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print(f"==============================")
            input("Press Enter to Continue...")
            os.system("cls")            

    while True:
        try:
            print(f"=====[Informations]=====")
            print(f"Name: {product_name[p_select - 1]}")
            print(f"Stripe: {product_stripe[p_select - 1]}")
            print(f"Price: R${product_price[p_select - 1]:.2f}")
            print(f"Quantity: {product_quantity[p_select - 1]}")
            print(f"")

            quantity = int(input("How Many?: "))
            total = product_quantity[p_select - 1] * quantity

            if quantity <= 0:
                print(f"Invalid Quantity. Type Again.")
                print(f"==============================")
                input(f"Press Enter to Continue...")
                os.system("cls")
            elif quantity > product_quantity[p_select - 1]:
                print(f"Insufficent Stock. Type Again.")
                print(f"==============================")
                input(f"Press Enter to Continue...")
                os.system("cls")
            else:
                product_quantity[p_select - 1] = product_quantity[p_select - 1] - quantity
                print(f"Total Price: R${total:.2f}")
                print(f"Purchase Sucessful!")
                print(f"==============================")
                input(f"Press Enter to Continue...")
                os.system("cls")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print(f"==============================")
            input("Press Enter to Continue...")
            os.system("cls")
