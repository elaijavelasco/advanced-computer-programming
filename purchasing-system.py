product_list = [{"id" : 21021, "name" : "Mouse", "quantity" : 100, "type" : "Gadget Accessory", "price" : 399}
    {"id" : 21022, "name" : "Mouse Pad", "quantity" : 100, "type" : "Gadget Accessory", "price" : 199}
    {"id" : 21023, "name" : "Keyboard", "quantity" : 50, "type" : "Gadget Accessory", "price" : 599}]

class Main:
    def show_menu(self):
        while True:
            print ("Purchasing System")
            print ("1 - Display Products")
            print ("2 - Add Products")
            print ("3 - Remove Products")
            print ("4 - Search Products")
            print ("5 - Exit")
  
  #Function Definition
    def display_menu(self):
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
    
    #function for searching products
    def search_product(self):
        pass

     
