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
        
