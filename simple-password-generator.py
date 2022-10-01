#This Python program is a simple password generator

import random

print ("\n\t\t**Password Generator**\n")
name = str (input("\tEnter your name: "))
print ("\tHello, " + name + "!")
print()

password_len = int (input("\tEnter the password length: "))
print()

password_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*_()?/"
password = "".join(random.sample(password_char, password_len))
print ("\t" + name + ", your password is: "+ password)
print()
