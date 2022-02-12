import csv
import sys
sys.setrecursionlimit(8000)
from distutils import core
import os
from my_functions import * 
from pprint import pprint 


print()
print("^^^^^^^^^^^^^^^^^^^ ^^^^^")
print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
print("|       OUR CAFE        |")
print("|    Ordering System    |")
print(" ~~~~~~~~~~~~~~~~~~~~~~~ ")
print("")
print("Welcome to our ordering system.")


def product_menu_options():
    print()
    options = input("""   PRODUCT MENU
    -----------------------------------
    1 -> Display Products 
    2 --> Add New Product 
    3 --> Update Existing Product
    4 --> Delete Product
    0 --> Return to Main Menu
    
    Please select an option """)
    print()
    
    if int(options) ==1:
        print("Here is a list of all products")
        print('______________________________')
        read_from_products()
        product_menu_options()
        #again()
        
    elif int(options) ==2:
        add_new_product()
        product_menu_options()

    elif int(options) ==3:
        update_product()
        product_menu_options()
        
        


    elif int(options)==0:
        MainMenu()
    else:
        print('You have not chosen a valid option, please run the program again.')

        #again()
        print()

def menu_options_couriers():

    options = input("""---'''COURIERS MENU'''---

    1 --> Display All Couriers 
    2 --> Add New Courier 
    3 --> Update Existing Courier
    4 --> Delete Courier
    0 --> Return to Main Menu
    
    Please select an option """)
    print()

    if int(options) ==1:
        print("Here is a list of all Couriers")
        print('______________________________')
        read_from_couriers()

    elif int(options) ==2:
        add_new_courier()
        menu_options_couriers()


def order_status_menu():
    print()
    options = input(""" ORDER STATUS MENU
    ----------------------------------------
    1 ->  Out for Delivery
    2 --> Preparing
    3 --> Pending
    4 --> Delivered
    0 --> Order Received
    
    Please select an option """)
    print()

def order_menu_options():
    print()
    options = input("""  ORDER MENU
    -----------------------------------
    1 ->  Display an order 
    2 --> Create Order 
    3 --> Update Order Status
    4 --> Delete Order
    0 --> Return to Main Menu
    
    Please select an option """)
    print()


    if int(options) ==1:
        print("Here is a list of all Orders")
        print()
        with open("customer_data.csv","r") as file:
                reader = csv.DictReader(file)
                order_list = list(reader)
                
        pprint(order_list)
        order_menu_options()

    elif int(options) ==2:
        #order_input()


        def read_from_file():
            with open("customer_data.csv","r") as file:
                reader = csv.DictReader(file)
                #creates the list
                order_list = list(reader)
                
            return order_list
        

        def write_to_file(order_list):
            with open ('customer_data.csv', 'w', newline='') as file:
                myfieldnames = ["first_name","last_name","address","phone_number","order_status","courier"]
                writer = csv.DictWriter(file, fieldnames=myfieldnames, delimiter =',')
                writer.writeheader()
                writer.writerows(order_list)
                
        first_name = input("Enter First name: ")
        last_name = input("Enter Last name: ")
        address = input("Enter your address ")
        phone_number = input("Enter your phone number ")
        order_status = "PREPARING"
        #courier = input("enter curier")
        print()
        print("____________________")
        print("COURIERS\n")
    
        
        with open('couriers.txt', 'r+') as couriers:
            order_record = couriers.readlines()

        for item in order_record:
            index = order_record.index(item)
            print(f'{index} - {item}')

         

        courier = int(input("Please select the corresponding number for the courier you want to add:\n"))
        order_record.append(courier)
        record ={'first_name': first_name , 'last_name': last_name, 'address':address, 'order_status': "PENDING",'courier': courier}

        order_list = read_from_file()
        # order_list[0]["first_name"] = "John"
        order_list.append(record)

        write_to_file(order_list)
        pprint(order_list)

    elif int(options) ==3:
    
    
        statuses = ["Preparing", "Pending", "Order Received","Delivered"]
        def read_from_file(filename):
                
            with open(filename) as file:
                reader = csv.DictReader(file)
                #creates the list
                order_list = list(reader)

            return order_list

        def write_csv(file_name, record):
            with open(file_name, mode="w") as file:
                writer = csv.DictWriter(file, fieldnames=record[0].keys())
                writer.writeheader()
                writer.writerows(record)
                
        orders = read_from_file("customer_data.csv")
        def update_order(orders):
            # for index, order in enumerate(orders):
            #     print(f'{index} --  {order}') 
        
            for key, order in enumerate(orders):
                print(key, order)
                

            chosen_order_index = int(input("pick an order: "))

            for index, status in enumerate(statuses):
                print(index, status)

            chosen_status_index = int(input("pick a status: "))

            orders[chosen_order_index]["order_status"] = statuses[chosen_status_index]

            return orders

        update_order(orders)
        write_csv("customer_data.csv", orders)
        pprint(orders)
    
    #         choose_status_record = int(input("choose status:\n"))


    #         orders[chosen_order_index]["status"] = statuses[choose_status_record]

    #         return orders
    # orders = read_from_file("orders.csv")    
    # update_order(orders)
    # write_to_file("orders.csv", orders) 
    #order_list[0]["first_name"] = "Samson"
    # order_status_menu()
    # read_from_file()
    # order_list.append(order_record)
    
    # order_list = read_from_file()
    #     # order_list[0]["first_name"] = "John"
    # order_list.append(order_record)

    # else:
    #     print('You have not chosen a valid option, please make a new selection.')


def MainMenu():

    print("\nMENU:")
    print("*****************")
    print("1. Product Menu")
    print("2. Couriers Menu")
    print("3. Order Menu")
    print("0 - Exit App\n")
    
    choice = input("Make selection from the above list :""")
    print()
    if int(choice) ==1:
        product_menu_options()
            
    elif int(choice) ==2:
        menu_options_couriers()

    elif int(choice) ==3:
        order_menu_options()

    elif int(choice) == 0:
            print()
            print("Exiting, thank you and goodbye")
            print()
            exit()
 
#os.system('clear')
#if __name__ == '__main__':
MainMenu()
