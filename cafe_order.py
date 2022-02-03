import os
from my_functions import * 

print()
print("^^^^^^^^^^CAFE ORDERS^^^^^^^^^^")


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
        #again()
        
    elif int(options) ==2:
        add_new_product()
        menu_options()

    elif int(options) ==3:
        update_product()
        
        


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


    # elif int(options) ==3:
    #     update_product()


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
        
  elif int(choice) ==2:
      menu_options_couriers()

  elif int(choice) == 0:
        print()
        print("Exiting, thank you and goodbye")
        print()
        exit()
 
os.system('clear')
#if __name__ == '__main__':
MainMenu()
