import os
from pre_defined_products import *

def product_list():

    print(f"=====[Product List]=====")
    print(f"")

    for l_counter in range(len(product_quantity)):
        print(f"Name: {product_name[l_counter]}")
        print(f"Stripe: {product_stripe[l_counter]}")
        print(f"Price: R${product_price[l_counter]:.2f}")
        print(f"Quantity: {product_quantity[l_counter]}")
        print(f"")

        print(f"========================")

    input(f"Press Enter to Continue...")
    os.system("cls")