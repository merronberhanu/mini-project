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
    menu_options()


def read_from_couriers():
    with open('couriers.txt','r') as prod:
        courier = sorted(prod.readlines())
        #print(courier)
        for product in courier:
            #eachItem = product.split(",")
            print(product.replace('\n',''))
            print()

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

def menu_options():
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
        again()
        
    elif int(options) ==2:
        add_new_product()
        menu_options()

    # elif int(options) ==3:
    #     print("Here are list of products with their corresponding numbers:\n" )
    #     for products in file:
    #         products.
        
        for item in range(len(read_from_products())):
            #print(item)
            print(item, read_from_products()[item])
            print()
            
            
        user_input = int(input("select the product number you would like to update:\n"))
        update_input =input("What is the new product you would like to change to?\n")
        
        user_input = update_input
        print()
        print( "The new menu is:")
        print()
        print(', '.join(user_input))
        print()
        menu_options()

    # elif int(options) ==4:
    #     print("Here are list of products with their corresponding numbers:\n" )
    #     for item in range(len(product_menu)):
    #         #print(item)
    #         print(item, product_menu[item])
    #         print()

    #     delete_prod = int(input("select the product number you would like to Delete:\n"))
    #     del product_menu[delete_prod]
    #     print(', ' .join(product_menu))
    #     menu_options()

    elif int(options)==0:
        MainMenu()
    else:
        print('You have not chosen a valid option, please run the program again.')
        #again()
        print()  

def MainMenu():
  
  print("\nMENU:")
  print("*****************")
  print("1. Display Product Menu")
  print("2. Display Couriers Menu")
  print("0 - Exit App\n")
  

  choice = input("Make selection from the above list :""")
  print()
  if int(choice) ==1:
    menu_options()
        
  elif int(choice) == 0:
        print()
        print("Exiting, thank you and goodbye")
        print()
        exit()   