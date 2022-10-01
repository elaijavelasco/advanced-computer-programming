import random

def generate_password(password_len):

    password_letter = "abcdefghijklmnopqrstuvwxyz"
    #passwords list
    passwords_list = [] 

    for i in password_len:
        #generate a random password
        password = "" 
        for j in range(i):
            #pick a random letter from password_letter
            next_letter_idx = random.randrange(len(password_letter))
            #add the picked random letter to the password
            password = password + password_letter[next_letter_idx]

        password = replace_w_number(password)
        password = replace_w_uppercase(password)
        passwords.append(password)
    
    return passwords

def replace_w_number(new_password):
    for i in range(random.randrange(1,3)):
        replace_idx = random.randrange(len(new_passsword)//2)
        new_password = new_password[0:replace_idx] + str(random.randrage(10)) + new_password[replace_idx + 1:]
        return new_password 




