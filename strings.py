#This is a multiline string
print("Multiline string:")

chorus_lyrics = """ >> You know, without you, I'm so lonely
When you're not here, 911 calling
Into your heat again, I'm diving
Darling you, darling you, baby <<\n """

print (chorus_lyrics)


#Strings are Array
print("Strings are array: ")

my_PL= "PYTHON"
print("0 = " + my_PL[0])
print("1 = " + my_PL[1])
print("2 = " + my_PL[2])
print("3 = " + my_PL[3])
print("4 = " + my_PL[4])
print("5 = " + my_PL[5])


#Looping in string
print("\nLooping of string:")

for x in "Python Tutorial":
    print(x)


#String length
print("\nLength of string my_PL:")
print(len(my_PL))


#Check string
print("\nCheck string:")
text= "My programming language is Python."
if "Python" in text:
    print('Yes, "Python" is present!')

#Check if NOT
print("Check if NOT:")
if "Java" not in text:
    print('Yes, "Java" is NOT present!')

#Slicing of string
print("\nSlicing of string:")
print(my_PL[1:4])
print(my_PL[:6]) #slice from start
print(my_PL[2:]) #slice to end
print(my_PL[-5:-2]) #negative indexing

#Modifying strings
print("\nModifying strings:")
print("\nUpper case:")
print(text.upper())
print("\nLower case:")
print(text.lower())
print("\nRemove whitespace:")
print(text.strip())
print("Split string:")
print(text.split(","))
print("\nReplace:")
print(text.replace("a","x"))


#String concatenation
print("\nString concatenation:")
course1 = "Information"
course2 = "Technology"
my_course = course1 + " " + course2
print(my_course)

#String format
print("\nString Format")
code = 121
course_code = "CS {}" #{} is a placeholder
print(course_code.format(code))

print("\nString Format with Arguments")
units = 23
year_level = 2
semester = 1
my_status = "I'm taking {} units for {}st semester in my {}nd year"
print(my_status.format(units, semester, year_level))


