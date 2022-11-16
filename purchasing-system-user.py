class User_Update_Mixin:
    def change_user_password (self, new_user_password):
        self.user_password = new_user_password

class User (User_Update_Mixin):
    def __init__(self, user_username, user_password):
        self.user_username = user_username
        self.user_password = user_password
        self.original_user_username = user_username
    
    def update_admin_orig_username (self):
        self.original_admin_username = self.admin_username

class User_Menu:
    def show_menu(self):
        while True:
            print ("Purchasing System")
            print ("1 - User Login")
            print ("2 - Change Password")
            print ("3 - Display Products")
            print ("4 - Place Order")
            print ("5 - Cancel Order")
            print ("6 - Log out")
            print ("7 - Exit")
        
        user_choice = ""
        try: user_choice = int (input ("What do you want to do? "))
        except value_error:
            print ("Invalid Input!")
        
        if user_choice == 1:
            self.user_login()
        elif user_choice == 2:
            self.change_user_password()
        elif user_choice == 3:
            self.display_product()
        elif user_choice == 4:
            self.place_order()
        elif user_choice == 5:
            self.cancel_order()
        elif user_choice == 6:
            self.user_logout()
        elif user_choice == 7:
            print ("User menu terminated...")
        else:
            print ("Invalid input. Please enter valid choice.")
            self.user_login()

#Function Definition

    def user_login (self):
        pass

    def change_user_password(self):
        pass

    def display_product(self):
        pass

    def place_order(self):
        pass

    def cancel_order(self):
        pass

    def user_logout(self):
        pass

