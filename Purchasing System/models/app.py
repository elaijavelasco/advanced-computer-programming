from models.shop import Shop
from models.purchase import Purchase
import sys

class App:
    def app_menu(self):
        print("Welcome to Purchasing System!")
        print("User Mode: ")
        print("1 - Seller Mode")
        print("2 - Customer Mode")
        print("3 - Exit Application")

        self.choice = ""
        try:
            self.choice = int(input("Enter user mode: "))
        except ValueError:
            print("Invalid Entry!")
            self.app_menu()
        
        if self.choice == 1:
            Shop.shop_menu(self)
        
        elif self.choice == 2:
            Purchase.order_menu(self)
        
        elif self.choice == 3:
            print("You've exited the application :) ")
            sys.exit()
