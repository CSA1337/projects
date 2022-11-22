from ..pull import *
from tabulate import tabulate
from ..banners import courier_banner
import copy

courier = {}

def load_courier():
    global couriers
    couriers = pull_data('Data/couriers/couriers.json')

def write_couriers():
    save_data(couriers, 'Data/couriers/couriers.json')

def courier_menu():
    while True:
        try:
            print("\n\n0 - Main menu\n1 - All Couriers\n2 - New Courier")
            print("3 - Update Courier\n4 - Delete Courier")
            choice = int(input("\nOption: "))
            if choice not in range(0,5):
                error()
                continue
        except:
            error()
            continue
        if choice == 0:
            return
        elif choice == 1:
            courier_list()
        elif choice == 2:
            create_courier()
            print("Courier has been added...")
        elif choice == 3:
            courier_list()
            update_courier()
            print("Courier has been Updated...")
        elif choice == 4:
            courier_list()
            delete_courier()
            print("Courier has been deleted...")

def courier_list():
    print(tabulate(couriers,showindex=True,headers='keys',tablefmt='fancy_grid'))

def create_courier():
    while True:
        name = input("Customer Name: ")
        if name.isalpha() == True:
            courier["customer_name"] = name.title()
            break
        else:
            print("Invalid input!!!")
            continue
    c_name = input("Courier Name: ")
    courier["courier_name"] = c_name
    address = input("Customer Address: ")
    courier["customer_address"] = address
    while True:
        number = input("Customer Phone: ")
        if len(number) == 11 and number.isdigit() == True:
            courier["customer_phone"] = number
            break
        else:
            print("Invalid input. Try again.")
            continue
    dict_copy = copy.deepcopy(courier)
    couriers.append(dict_copy)

def update_courier():
    while True:
        try:
            option = int(input("Option: "))
            courier = couriers[option]
            break
        except:
            error()
            continue
    for key, value in courier.items():
        print(f"Key: {key}, Value: {value}")
        new_value = input("Enter New Value: ")
        if new_value.strip() == '':
            continue
        else:
            courier[key] = new_value

def delete_courier():
    while True:
        try:
            option = int(input("Which courier you want to delete: "))
            courier = couriers[option]
            break
        except:
            error()
            continue
    couriers.remove(courier)