from ..pull import *
from ..banners import product_banner

products = []

file_location = 'Data/products/products.txt'
def write_product():
    with open (file_location, 'w') as file:
        for product in products:
            file.write(product)
            file.write("\n")

def load_products():
    file = open(file_location, 'r')
    for line in file.readlines():
        products.append(line.rstrip("\n"))

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
        elif choice == 3:
            print_product()
            update_product()
            print("Product has been updated...")
        elif choice == 4:
            print_product()
            delete_product()
            print("Product has been deleted...")
            

def print_product():
    print("+=======================+")
    print("|   ALL   PRODUCTS      |")
    print("+=======================+")
    for x in range(len(products)):
        print(f"[{x}] - ", products[x])
    print("+=======================+")

def create_product():
    product_name = input("\nProduct Name: ")
    products.append(product_name.title())
    write_product()

def update_product():
    while True:
        try:
            Choice = int(input("Which product you like to update: "))
            products[Choice]
            product = input("Enter updated product: ")
            products[Choice] = product.title()
            break
        except:
            error()
            continue
    write_product()

def delete_product():
    while True:
        try:
            choice = int(input("Which product you like to delete: "))
        except:
            error()
            continue
        del products[choice]
        break
    write_product()

    