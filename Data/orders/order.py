from ..pull import *
from tabulate import tabulate
from ..banners import order_banner
import copy

order = {}

def load_orders():
    global orders 
    orders = pull_data('Data/orders/orders.json')

def write_orders():
    save_data(orders, 'Data/orders/orders.json')

def order_menu():
    while True:
        try:
            print("\n\n0 - Main menu\n1 - All Orders\n2 - New Order")
            print("3 - Order Status\n4 - Update order\n5 - Delete Order")
            choice = int(input("\nOption: "))
            if choice not in range(0,6):
                error()
                continue
        except:
            error()
            continue
        if choice == 0:
            return
        elif choice == 1:
            order_list()
        elif choice == 2:
            create_order()
            print("Order has been added...")
        elif choice == 3:
            order_list()
            order_status()
            print("Status has been Updated...")
        elif choice == 4:
            order_list()
            update_order()
            print("Order has been Updated...")
        elif choice == 5:
            order_list()
            delete_order()
            print("Order has been deleted...")

def order_list():
    print(tabulate(orders,showindex=True,headers='keys',tablefmt='fancy_grid'))

def create_order():
    while True:
        name = input("Customer Name: ")
        if name.isalpha() == True:
            order["customer_name"] = name.title()
            break
        else:
            print("Invalid input!!!")
            continue
    address = input("Customer Address: ")
    order["customer_address"] = address
    while True:
        number = input("Customer Phone: ")
        if len(number) == 11 and number.isdigit() == True:
            order["customer_phone"] = number
            break
        else:
            print("Invalid input. Try again.")
            continue
    order["order_status"] = "Received"
    dict_copy = copy.deepcopy(order)
    orders.append(dict_copy)

def update_order():
    while True:
        try:
            option = int(input("Option: "))
            order = orders[option]
            break
        except:
            error()
            continue
    for key, value in order.items():
        print(f"Key: {key}, Value: {value}")
        new_value = input("Enter New Value: ")
        if new_value.strip() == '':
            continue
        else:
            order[key] = new_value

def delete_order():
    while True:
        try:
            option = int(input("Which order you want to delete: "))
            order = orders[option]
            break
        except:
            error()
            continue
    orders.remove(order)

def order_status():
    while True:
        try:
            option = int(input("Option: "))
            orders[option]
        except:
            error()
            continue
        else:
            while True:
                status = ["Received", "Preparing", "Shipped","Delivered"]
                print("\n0 - Received\n1 - Preparing\n2 - Shipped\n3 - Delivered")
                status_update = int(input("Choice: "))
                order = orders[option]
                if status_update not in range(0,4):
                    error()
                    continue
                else:
                    order["order_status"] = status[status_update]
                    break
            break