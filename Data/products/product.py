from ..pull import *
from tabulate import tabulate
import copy
from ..banners import product_banner


product = {}

def load_product():
    global products 
    products = pull_data('Data/products/products.json')

def write_product():
    save_data(products, 'Data/products/products.json')


def product_menu():
    while True:
        try:
            print("\n\n0 - Main menu\n1 - All Product\n2 - New Product")
            print("3 - Update Product\n4 - Delete_Product")
            choice = int(input("Option: "))
            if choice not in range(0,5):
                error()
                continue
        except:
            error()
            continue
        if choice == 0:
            return
        elif choice == 1:
            print_product()
        elif choice == 2:
            create_product()
            print("Product has been created...")
        elif choice == 3:
            print_product()
            update_product()
            print("Product has been updated...")
        elif choice == 4:
            print_product()
            delete_product()
            print("Product has been deleted...")
            

def print_product():
    print(tabulate(products,showindex=True,headers='keys',tablefmt='fancy_grid'))

def create_product():
    while True:
        name = input("Product Name: ")
        if name.isalpha() == True:
            product["product_name"] = name.title()
            break
        else:
            error()
            continue
    price = input("Price: ")
    product["Price"] = price
    dict_copy = copy.deepcopy(product)
    products.append(dict_copy)

def update_product():
    while True:
        try:
            option = int(input("Option: "))
            product = products[option]
            break
        except:
            error()
            continue
    for key, value in product.items():
        print(f"Key: {key}, Value: {value}")
        new_value = input("Enter New Value: ")
        if new_value.strip() == '':
            continue
        else:
            product[key] = new_value

def delete_product():
    while True:
        try:
            option = int(input("Which product you want to delete: "))
            product = products[option]
            break
        except:
            error()
            continue
    products.remove(product)

    