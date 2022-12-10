from models.seller import Seller

import csv, sys

class Shop_Database:
    shop_fields = ['Product ID', 'Product Name', 'Type', 'Quantity', 'Price']
    shop_database = "products_database.csv"

class Shop(Shop_Database):
    def shop_menu(self):
        print("Seller Mode")

        while True:
            print("Seller Menu: ")
            print("1 - Login")
            print("2 - Add Products")
            print("3 - View Products")
            print("4 - Search Products")
            print("5 - Remove Products")
            print("6 - Exit")

            self.choice = ""
            try:
                self.choice = int(input("Enter choice: "))
            except ValueError:
                print("Invalid Entry!")
                Shop.shop_menu(self)
            
            if self.choice == 1:
                Seller.login(self)
            
            elif self.choice == 2:
                Shop.add_product(self)
            
            elif self.choice == 3:
                Shop.view_product(self)
            
            elif self.choice == 4:
                Shop.search_product(self)
            
            elif self.choice == 5:
                Shop.remove_product(self)
            
            elif self.choice:
                sys.exit()
            
            else:
                print("Invalid Entry!")
                sys.exit()
    
    def add_product(self):
        self.product_data = []

        print("Fill-in Product Information")

        for field in Shop_Database.shop_fields:
            value = input("Enter " + field + ": ")
            self.product_data.append(value)
        with open(Shop_Database.shop_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([self.product_data])
            print("Product successfully added!")
        Shop.shop_menu(self)
    
    def view_product(self):
        with open(Shop_Database.shop_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for x in Shop_Database.shop_fields:
                print(x ,end="\t| ")
            print("\n", 70*'-')
            for row in reader:
                for item in row:
                    print(item, end="\t| ")
                print("\n")
            sys.exit()
    
    def search_product(self):
        productId = input ("Enter the product id to search: ")
        with open(Shop_Database.shop_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    if productId == row[0]:
                        print("Product ID: ", row[0])
                        print("Product Name: ", row[1])
                        print("Type: ", row[2])
                        print("Quantity: ", row[3])
                        print("Price: ", row[4])
                        break
            else:
                print("Product ID not found!")
        sys.exit()
    
    def remove_product(self):
        productId = input("Enter product id to remove: ")
        self.product_found = False
        self.updated_data = []
        with open(Shop_Database.shop_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if productId != row[0]:
                        self.updated_data.append(row)
                        counter += 1
                    else:
                        self.product_found = True
        if self.product_found is True:
            with open(Shop_Database.shop_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(self.updated_data)
            print("Product ID ", productId, "deleted successfully!")
        else:
            print("Product ID not found!")
                
            