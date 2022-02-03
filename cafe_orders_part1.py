product_menu = [    "Latte", "Coffee", "Tea","Iced Tea", "Hot Chocolate ",]

def menu_options():

    options = input("""
    1 --> Display Products
    2 --> Add New Product 
    3 --> Update Existing Product
    4 --> Delete Product
    0 --> Return to Main Menu
    
    Please select an option """)
    print()
    
    if int(options) ==1:
        print()
        print(' , '.join(product_menu))
        menu_options()
        
    elif int(options) ==2:
        new_product = input("\n    Enter a new product: ")
        product_menu.append(new_product)
        print('\n    You have added '+ new_product + ' to the menu. The new menu:\n')
        print(' , '.join(product_menu))
        print()
        menu_options()
    elif int(options) ==3:
        print("Here are list of products with their corresponding numbers:\n" )
        for item in range(len(product_menu)):
            #print(item)
            print(item, product_menu[item])
            print()
            
        user_input = int(input("select the product number you would like to update:\n"))
        update_input =input("What is the new product you would like to change to?\n")
        
        product_menu[user_input] = update_input
        print()
        print( "The new menu is:")
        print()
        print(', '.join(product_menu))
        print()
        menu_options()

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

  menu_open = True 
  while menu_open:

   print("*****************")
   print("\nMENU:")
   print("*****************")
   print("1 - Display the Menu")
   print("0 - Exit App\n")
  

   choice = input("""Choose 1 for Product Menu or 0 to exit the app:""")
   if int(choice) ==1:
        menu_options()
        
   elif int(choice) == 0:
            print()
            print("Exiting, thank you and goodbye")
            menu_open = False
            # print()
            break
        
MainMenu()