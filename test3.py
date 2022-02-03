colors = ["red", "green", "blue", "purple"]
for i, item in enumerate((colors)):
    print(i, item)
    #print(colors[item])
    #print(item)




for i, item in enumerate((product_menu)):
         print(i,'.  ' +item)
         user_input = int(input("select the product number you would like to update:"))
         update_input =("What name would you like to change it to?\n")

         product_menu[user_input] = update_input
         print(product_menu)