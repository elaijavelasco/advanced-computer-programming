product_list = [{"id" : 21021, "name" : "Mouse", "quantity" : 100, "type" : "Gadget Accessory", "price" : 399}
    {"id" : 21022, "name" : "Mouse Pad", "quantity" : 100, "type" : "Gadget Accessory", "price" : 199}
    {"id" : 21023, "name" : "Keyboard", "quantity" : 50, "type" : "Gadget Accessory", "price" : 599}]

item1 = product_list
temp_product_list = []
order = ""

class admin_menu:
    def show_menu(self):
        while True:
            print ("Purchasing System")
            print ("1 - Display Products")
            print ("2 - Add Products")
            print ("3 - Remove Products")
            print ("4 - Search Products")
            print ("5 - Total")
            print ("6 - Exit")
  
#Function Definition
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
    
    def total(self):
        pass
                



        

     
