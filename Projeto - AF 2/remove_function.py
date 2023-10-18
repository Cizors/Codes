import os
from pre_defined_products import *

def remove_products():
    while True:
        try:
            remove_counter = 1

            print(f"=========[Products]=========")

            for p_name3 in product_name:
                print(f"{remove_counter}. {p_name3}")

                remove_counter += 1

            p_select3 = int(input(f"Select: "))
            print(f"============================")

            if p_select3 < 1 or p_select3 > len(product_name):
                print(f"Invalid Product. Type Again.")
                print(f"============================")
                input(f"Press Enter to Continue...")
                os.system("cls")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print(f"============================")
            input("Press Enter to Continue...")
            os.system("cls")

    product_name.pop(p_select3 - 1)
    product_stripe.pop(p_select3 - 1)
    product_price.pop(p_select3 - 1)
    product_quantity.pop(p_select3 - 1)

    print(f"Product Removed with Success!")
    input(f"Press Enter to Continue...")
    os.system("cls")