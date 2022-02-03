

def read_from_products():  
    with open('products.txt','r') as prod: 
        products = prod.readlines()
        #print(products)
        for product in products:
            print(product)
            print()

    # #for i in enumerate(read_file):
    #print(read_file)


def add_new_product(): 

 new_product = input("\n    Enter a new product: ")
 file = open("products.txt", "a")
 file.write(new_product + "\n") 
 print("    " + new_product + " " "has been added.\n")


def update_product():
    pass

def read_from_couriers():

    with open('couriers.txt','r') as prod:
        read_file = prod.readlines()
        print(read_file)


def add_courier(): 

    new_product = input("\n    Enter a new product: ")
    file = open("products.txt", "a")
    file.write(new_product + "\n") 
    print("    " + new_product + " " "has been added.\n")


def menu_options():

    options = input("""---'''PRODUCT MENU'''---

    1 --> Display Products 
    2 --> Add New Product 
    3 --> Update Existing Product
    4 --> Delete Product
    0 --> Return to Main Menu
    
    Please select an option """)
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
    
    # if int(options) ==1:
    #     print("Here is a list of all products")
    #     print('__________________________')
    #     read_from_products()
    #     print('__________________________')
    #    #print(read_file)
    #     menu_options()
    if int(options) ==1:
        print("Here is a list of all products")
        print('______________________________')
        read_from_products()
        print('______________________________')
        menu_options()
        
    
    elif int(options) ==2:
        add_new_product()
        menu_options()
        
    # elif int(options) ==3:
    #     print("Here are list of products with their corresponding numbers:\n" )
    #     for item in range(len(product_menu)):
    #         #print(item)
    #         print(item, product_menu[item])
    #         print()
            
    #     user_input = int(input("select the product number you would like to update:\n"))
    #     update_input =input("What is the new product you would like to change to?\n")
        
    #     product_menu[user_input] = update_input
    #     print()
    #     print( "The new menu is:")
    #     print()
    #     print(', '.join(product_menu))
    #     print()
    #     menu_options()
    
    elif int(options) ==3:
     read_from_products()
     #x= prod1.readlines()
     #lines = read_from_products()
     for item, line in enumerate(lines):
      print("Line {}: {}".format(index, line.strip()))
    

    # for i, item in enumerate((f)):
    #      print(i,'.  ' +item)
    #      user_input = int(input("select the product number you would like to update:"))
    #      update_input =("What name would you like to change it to?\n")

    #      product_menu[user_input] = update_input
    #      print(product_menu)

     
    elif int(options) ==4:
        print("Here are list of products with their corresponding numbers:\n" )
        for item in range(len(product_menu)):
            #print(item)
            print(item, product_menu[item])
            print()

        delete_prod = int(input("select the product number you would like to Delete:\n"))
        del product_menu[delete_prod]
        print(', ' .join(product_menu))
        menu_options()

    elif int(options)==0:
         MainMenu()
      


def MainMenu():
  print("*****************")
  print("\nMENU:")
  print("*****************")
  print("1. Display Product Menu")
  print("2. Display Couriers Menu")
  print("0. Exit App\n")
  

  choice = input("Make selection from the above list :""")
  if int(choice) ==1:
     menu_options()
        
  elif int(choice) ==2:
      menu_options_couriers()

  elif int(choice) == 0:
            print()
            print("Exiting, thank you and goodbye")
            print()
        
MainMenu()