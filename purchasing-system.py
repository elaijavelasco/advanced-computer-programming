class Main:
    def show_menu(self):
        while True:
            print ("Purchasing System")
            print ("1 - Display Products")
            print ("2 - Add Products")
            print ("3 - Remove Products")

    def display_menu(self):
        pass
    
    def add_item(self):
        num = int (input ("Enter the number of items you want to add: "))
        
        for i in range(num):
            new_product_id = int (input ("Enter the Product ID": ))
            new_product_name = input ("Enter the Product Name: ")
            new_product_quantity = int (input ("Enter the Quantity of Product:"))
            new_product_type = input ("Enter the Product Type: ")
            new_product_price = int (input ("Enter the Product Price: "))
            item = [{"id" : new_product_id, "name" : new_product_name, "quantity" : new_product_quantity, "type" : new_product_type, "price" : new_product_price}]
            dress.extend(item)

     
