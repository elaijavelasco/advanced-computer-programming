class user_update_mixin:
    def change_password (self, new_password):
        self.password = new_password

class user (user_update_mixin):
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.original_username = username

    def update_original_username(self):
        self.original_username = self.username

class user_exists (Exception):
    pass

class user_database:
    def__init__(self):
        self.database = {}
    
    def add_user(self, user):
        if user.username in self.database:
            raise user_exists
        self.database[user.username] = user
    
    def get_user(self):
        return self.user_database
    
    def update_user(self, user):
        if user.username in self.database:

            raise user_exists
        
        self.update_original_username()
        self.database[user.username] = user
        del self.database[user.original_username]

class main_app:
    def __init__(self):
        self.database = {}
        self.logged_in_user = None
    
    def show_main_menu(self):
        while true:
            print ("1 - Register")
            print ("2 - Login")
            print ("3 - Logout")
            print ("4 - Change Password")
            print ("5 - Check Info")
            print ("6 - Exit")

            _ = ""
            try: _ = int (input("What do you want to do? "))
            except value_error:
                print("Incorrect Entry!")
            
            if _ == 6:
                print("Goodbye!")
                break
            
            if _ == 1:
                self.register()
            
            elif _ == 2:
                self.login()
            
            elif _ == 3:
                self.logout()
            
            elif _ == 4:
                self.change_password()
            
            elif _ == 5:
                self.check_info()
            
            else:
                print ("Incorrect entry!, Try again? ")
    
    def register(self):
        username = input("Enter username: ")

        if username in self.database:
            print ("Username is already taken. ")
            return
        
        password = input("Enter password: ")

        self.database[username] = User(username, password)
    
    def login (self):
        username = input("Username: ")

        if username not in self.database:
            print ("Username or password is invalid. ")
            return
        
        password = input("Password: ")

        user = self.database[username]

        if user.password != password:
            print ("Username or password is invalid. ")
            return
        
        self.logged_in_user = user
        print ("Logged in!")
    
    def logout (self):
        if not self.logged_in_user:
            print("Your are not logged in. ")
            return
        
        self.logged_in_user = None
        print ("Logged out! ")
    
    def change_password (self):
        if not self.logged_in_user:
            print ("You are not logged in. ")
            return
        
        new_password = input("Enter new password: ")

        self.logged_in_user.change_password (new_password)
        print ("Password changed! ")
    
    def check_info(self):
        if self.logged_in_user:
            print(f"Your current username: {self.logged_in_user.username}")
            print(f"Your current password: {self.logged_in_user.password}")
        
        if not self.logged_in_user:
            print("Log in first! ")
    
    def run_app():
        app = main_app()
        app.show_main_menu()
    
    run_app()
