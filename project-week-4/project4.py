from os import system, name
from Data.pull import error
from Data.banners import main_banner
from Data.couriers.courier import *
from Data.orders.order import *
from Data.products.product import *

def main():
    while True:
        try:
            clear()
            main_banner()
            print("0 - Exit\n1 - Product Menu\n2 - Courier Menu\n3 - Order Menu")
            choice = int(input("\nOption: "))
            if choice not in range(0, 4):
                error()
                continue
        except:
            error()
            continue
        if choice == 0:
            write_couriers()
            write_product()
            write_orders()
            quit()
        elif choice == 1:
            clear()
            product_banner()
            product_menu()
        elif choice == 2:
            clear()
            courier_banner()
            courier_menu()
        elif choice == 3:
            clear()
            order_banner()
            order_menu()

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

if __name__ == "__main__":
    load_products()
    load_orders()
    load_courier()
    main()