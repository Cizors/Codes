import os
from pre_defined_products import *

def edit_products():
    while True:
        edit_counter = 1

        print(f"=======[Edit Products]=======")

        for p_name2 in product_name:
            print(f"{edit_counter}. {p_name2}")

            edit_counter += 1

        p_select2 = int(input(f"Select: "))
        print(f"=============================")

        if p_select2 < 1 or p_select2 > len(product_name):
            print(f"Invalid Product. Type Again.")
            print(f"============================")
            input(f"Press Enter to Continue...")
            os.system("cls")
        else:
            input(f"Press Enter to Continue...")
            os.system("cls")
            break

    print(f"=======[Informations]=======")
    print(f"Name: {product_name[p_select2 - 1]}")
    print(f"Stripe: {product_stripe[p_select2 - 1]}")
    print(f"Price: R${product_price[p_select2 - 1]:.2f}")
    print(f"Quantity: {product_quantity[p_select2 - 1]}")
    print(f"")

    edit_name = str(input("New Name: "))
    edit_stripe = str(input("New Stripe: "))
    edit_price = float(input("New Price: R$"))
    edit_quantity = int(input("New Quantity: "))

    product_name[p_select2 - 1] = edit_name
    product_stripe[p_select2 - 1] = edit_stripe
    product_price[p_select2 - 1] = edit_price
    product_quantity[p_select2 - 1] = edit_quantity

    print(f"")
    print(f"Product Edited with Success!")
    print(f"============================")
    input(f"Press Enter to Continue...")
    os.system("cls")