import csv

class Seller_Database:
    seller_fields = ['username', 'password']
    seller_database = 'seller_database.csv'

class Seller(Seller_Database):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        self.seller_data = []

        print("Sign in first.")
        for field in Seller_Database.seller_fields:
            value = input("Enter " + field + ": ")
            self.seller_data.append(value)
        
        with open(Seller_Database.seller_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([self.seller_data])
            print("Successfully signed in!")
    
    

