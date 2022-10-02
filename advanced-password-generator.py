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
        passwords_list.append(password)
    
    return passwords_list

def replace_w_number(new_password):
    for i in range(random.randrange(1,3)):
        replace_idx = random.randrange(len(new_password)//2)
        new_password = new_password[0:replace_idx] + str(random.randrange(10)) + new_password[replace_idx + 1:]
        return new_password 

def replace_w_uppercase(new_password):
    for i in range(random.randrange(1,3)):
        replace_idx = random.randrange(len(new_password)//2)
        new_password = new_password[0:replace_idx] + new_password[replace_idx].upper() + new_password[replace_idx + 1:]
        return new_password

def main():
    
    password_num = int (input("How many passwords you wan to generate? "))
    print("Generating " +str(password_num) + " passwords")

    pword_length = []
    print("The minimum length of password should be 6")

    for i in range(password_num):
        length = int(input("Enter you desired password length on password [" + str(i+1) + "] : " ))
        if length <= 6:
            length = 6
        pword_length.append(length)
    
    Password = generate_password(pword_length)

    for i in range(password_num):
        print ("Password [" +str(i+1) + "]" + " = " + Password[i]) 

main()

