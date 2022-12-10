from models.shop import Shop
from models.customer import Customer
import csv, sys

class Purchase_Database:
    purchase_fields = ['Customer ID', 'Product ID', 'Product Name', 'Quantity', 'Price']
    purchase_database = "customer_purchased_database.csv"

class Purchase:
    def order_menu(self):
        print("Welcome to our Shop!")
        print("Customer Menu: ")
        print("1 - Register")
        print("2 - Display available products")
        print("3 - Purchase products")
        print("4 - View purchased products ")
        print("5 - Exit")

        self.option = ""
        try:
            self.option = int(input("What would you like to do? "))
        except ValueError:
            print("Invalid Entry!")
            Purchase.order_menu(self)
        
        if self.option == 1:
            Customer.register(self)
        
        elif self.choice == 2:
            Shop.view_product(self)
        
        elif self.option == 3:
            Purchase.purchase_product(self)
        
        elif self.option == 4:
            Purchase.view_purchases(self)
        
        elif self.option == 5:
            print("Thank you for purchasing! Come again :) ")
            sys.exit()
    
    def purchase_product(self):
        self.purchase_data = []

        print("What to do you want to purchase? ")

        for field in Purchase_Database.purchase_fields:
            value = input("Enter " + field + ": ")
            self.purchase_data.append(value)
        with open(Purchase_Database.purchase_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([self.purchase_data])
            print("You have successfully purchased the product!")
        Purchase.order_menu(self)
    
    def view_purchases(self):
        with open(Purchase_Database.student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for x in Purchase_Database.purchase_fields:
                print(x, end="\t| ")
            print("\n", 70*'-')
            for row in reader:
                for item in row:
                    print(item, end="\t| ")
                print("\n")
            sys.exit()