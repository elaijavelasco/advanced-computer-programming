import csv

class Customer_Database:
    customer_fields = ['Customer ID', 'Customer Name', 'Phone', 'Address']
    customer_database = "customer_database.csv"

class Customer(Customer_Database):
    def register(self):
        self.customer_data = []

        print("Sign in first.")
        for field in Customer_Database.customer_fields:
            value = input("Enter " + field + ": ")
            self.customer_data.append(value)
        
        with open(Customer_Database.customer_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([self.customer_data])
            print("Successfully registered!")

    