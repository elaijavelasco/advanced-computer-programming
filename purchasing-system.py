"""product_list = [{"id" : 21021, "name" : "Mouse", "quantity" : 100, "type" : "Gadget Accessory", "price" : 399}
    {"id" : 21022, "name" : "Mouse Pad", "quantity" : 100, "type" : "Gadget Accessory", "price" : 199}
    {"id" : 21023, "name" : "Keyboard", "quantity" : 50, "type" : "Gadget Accessory", "price" : 599}]

item1 = product_list
temp_product_list = []
order = "" 
"""


class admin_menu:
    def show_menu(self):
        while True:
            print ("Purchasing System")
            print ("1 - Admin Login")
            print ("2 - Display Products")
            print ("3 - Add Products")
            print ("4 - Remove Products")
            print ("5 - Search Products")
            print ("6 - Total Products Available")
            print ("7 - Log out")
            print ("8 - Exit")
        
        admin_choice = ""
        try: admin_choice = int (input ("What do you want to do? "))
        except value_error:
            print ("Invalid Input!")
        
        if admin_choice == 1:
            self.login()
        elif admin_choice == 2:
            self.display_product()
        elif admin_choice == 3:
            self.add_product()
        elif admin_choice == 4:
            self.remove_product()
        elif admin_choice == 5:
            self.search_product()
        elif admin_choice == 6:
            self.total_product()
        elif admin_choice == 7:
            self.admin_logout()
        elif admin_choice == 8:
            print ("Admin menu terminated...")
            break

#Function Definition
    def admin_login(self):
        pass

    def display_product(self):
        pass
    
    #function for adding new products
    def add_product(self):
        num = int (input ("Enter the number of items you want to add: "))
        
        for i in range(num):
            new_product_id = int (input ("Enter the Product ID": ))
            new_product_name = input ("Enter the Product Name: ")
            new_product_quantity = int (input ("Enter the Quantity of Product:"))
            new_product_type = input ("Enter the Product Type: ")
            new_product_price = int (input ("Enter the Product Price: "))
            item = [{"id" : new_product_id, "name" : new_product_name, "quantity" : new_product_quantity, "type" : new_product_type, "price" : new_product_price}]
            dress.extend(item)
    
    #function for removing products
    def remove_product(self):
        item_id = int (input("Enter the product ID you want to remove: "))
        
        found = False #To renew found variable to False at the end of each loop
        
        for item in product_list:
            found = item["id"] == item_id
            if found != True:
                temp_product_list.append(item)
                continue
            elif found == True:
                item["quantity"] -= 1
        print ("Deleting the item...")

        if len(temp_product_list) == item:
            print(f"{item_id} not found") #{} placeholder for integer value
        else:
            print (f"{item_id} is removed from the list.")
    
    #function for searching products
    def search_product(self):
        if product_list == NULL:
            print ("There is no product listed in the product list!")
    
        while product_list != NULL:
            item_id = int (input("Enter the product ID to see product details: "))
            false = False

            for item in product_list:
                found = item["id"] == item_id
                if found != True:
                    print (f"Product ID: {item_id}")
                    print (f"Product Name: {item_id["name"]}")
                    print (f"Quantity: {item_id["quantity"]}")
                    print (f"Type: {item_id["type"]}")
                    print (f"Price: {item_id["price"]}")
    
    def total_product(self):
        total = 0
        for item in product_list:
            print (f"{d["name"]} = {d["quantity"]}")
            total += ({d["quantity"]})
            print( "Total products available: ", total)
    
    def admin_logout(self):
        pass





                



        

     
