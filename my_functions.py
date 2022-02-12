import csv
import cafe_order



        
#Fuction to read file 
def read_from_products():  

 with open('products.txt','r') as prod:
    #products = prod.readlines()
    products = sorted(prod.readlines())
    #print(products)
    for product in products:
        #eachItem = product.split(",")
        print(product.replace('\n',''))
        print()

        # with open('couriers.txt','r') as prod:
        # courier = sorted(prod.readlines())
        # print(courier)

#Function to add to product list
def add_new_product(): 

 new_product = input("\n    Enter a new product: ")
 file = open("products.txt", "a")
 file.write(new_product + "\n") 
 
#  print()
 print("    " + new_product + " " "has been added.\n")

def update_product():

    #productlist = []
    
    
    with open('products.txt', 'r+') as products:
        products_list = products.readlines()

    #print("Here are list of products with their corresponding numbers:\n" )
        for product in products_list:
            index = products_list.index(product)
            print(f'{index} - {product}')
    

        user_input = int(input("select the product number you would like to update:\n"))
        update_input =input("What is the new product you would like to change to?\n")
        
        products_list[user_input] = update_input +'\n'

        with open('products.txt','w') as file:
            for item in products_list:
                file.write(item)
                #print(products_list)
    #file.close()
        print( "The new menu is:")
        print(', '.join(products_list))
        # print()
        #product_menu_options()


def read_from_couriers():
    with open('couriers.txt','r') as prod:
        courier = sorted(prod.readlines())
        #print(courier)
        for product in courier:
            #eachItem = product.split(",")
            print(product.replace('\n',''))
            print()

def display_courier():
    with open('couriers.txt', 'r+') as courier:
        courier_list = courier.readlines()

    #print("Here are list of products with their corresponding numbers:\n" )
        for courier in courier_list:
            index = courier_list.index(courier)
            print(f'{index} - {courier}')
    

def add_new_courier(): 

    add_courier = input("\n    Enter a new Courier: ")
    file = open('couriers.txt', "a")
    file.write(add_courier + "\n") 
    #  print()
    print("    " + add_courier + " " "has been added.\n")
        
# def again():
#     list_again = input('''
# Would you like to see main menu again? (Y/N)
# ''')
#     if list_again.upper() =='Y':
#         menu_options()
#     elif list_again.upper() =='N':
#         print('OK. Bye bye.:)')
#         exit()
#     else:
#         again()
#         menu_options()


def read_from_customer_file():
        with open("customer_data.csv","r") as file:
            reader = csv.DictReader(file)
            order_list = list(reader)
                
        return order_list

        

