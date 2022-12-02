import os
import sys

def app_menu():
    print("\n\nText File Creator")
    print("\nMain Menu:")
    print("1. Create a text file")
    print("2. Write on text file")
    print("3. Open text file")
    print("4. Delete text file")
    print("5. Exit")

    choice = ""
    try: 
        choice = int(input("\nEnter chooice: "))
    except ValueError:
        print("Invalid Input!")
    
    if choice == 1:
        create_txt_file()
    
    elif choice == 2:
        edit_txt_file()
    
    elif choice == 3:
        open_txt_file()
    
    elif choice == 4:
        delete_txt_file()
    
    elif choice == 5:
        sys.exit()

def create_txt_file():
    file_name = input("Enter text file name: ")
    while (file_name == ""):
        print("File name is required!")
        file_name = input("Enter text file name: ")
    
    if(file_name != ""):
        while(os.path.isfile(file_name + ".txt")):
            print ("File name already taken!")
            file_name = input("Enter another text file name: ")
    
    txt_file = open(file_name + ".txt", "w")
    print("Your new text file has been created!")
    txt_file.close()

    input("Press any key to continue...")
    app_menu()

def edit_txt_file():
    file_name = input("Enter the txt file you want to edit: ")
    while not os.path.isfile(file_name):
        print("File not found...")
        break
    
    print(file_name + " has been opened!")
    file_content = input ("Write something on your text file: ")

    while (file_content == ""):
        print("Don't leave it blank...")
        file_content = input ("Please write something on your text file: ")
    
    txt_file = open(file_name, "w")
    txt_file.writelines(file_content)
    txt_file.close()

    print("\nEdited text file has been saved!")
    input("Press any key to continue...")
    app_menu()
    
