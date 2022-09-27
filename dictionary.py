print("\nPYTHON COLLECTIONS")

#List items are ordered, changeable, and allow duplicate values.
#List items are indexed.
#Enclosed in square brackets []

print("\nList")
myList = ["C++", "Java", "Python", "PHP", "SQL"]
print(myList)
print(type(myList))
print(len(myList))

#Access the items in the list
print("\nAccess Items in the List:")
print(myList[2]) #Prints "Python" from the list

#Access the items through indexing
print("\nIndexing:")
print(myList[2:4])
print("\nNegative Indexing:")
print(myList[-4:-1])

#Change the value of the item in the list
print("\nChange Item Value:")
myList[4] = "Bootstrap"
print(myList)

#Insert Items - use to insert an item at a specified index
#thislist = ["apple", "banana", "cherry"]
#thislist.insert(2, "watermelon")
#print(thislist)

#Append Items - to add item to the end of the list
#thislist = ["apple", "banana", "cherry"]
#thislist.append("orange")
#print(thislist)

#List constructor
print("\nList Constructor:")
myNewList = list(("VSC" , "Sublime", "Notepad"))
print(myNewList)
print(type(myNewList))

print ("\n----------------------------------")
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed
#Tuple can contain different data types
#Enclosed in round brackets ()

print("\nTuples")
myTuple = ("C++", "Java", "Python", "PHP", "SQL")
print(myTuple)
print(type(myTuple))
print(len(myTuple))

#Access the items in the tuple
print("\nAccess Items in the List:")
print(myTuple[2]) #Prints "Python" from the tuple

#Check IF the item is in the tuple
print("\nCheck If Item Exists:")
if "Java" in myTuple:
    print('Yes, "Java" is in the tuple!')

#Change tuple values
print("\nChange Tuple Values: ")
myChangedTuple = list(myTuple)
myChangedTuple[0] = "C"
myTuple = tuple(myChangedTuple)
print(myTuple)

#Tuple constructor
print("\nTuple Constructor: ")
myNewTuple = tuple(("VSC" , "Sublime", "Notepad"))
print(myNewList)
print(type(myNewTuple))

print ("\n----------------------------------")


#Set items are unordered, unchangeable, and do not allow duplicate values.
#A set can contain different data types
#Sets are written with curly brackets {}

print("\nSets")
mySet = {"C++", "Java", "Python", "PHP", "SQL"}
print(mySet)
print(type(mySet))
print(len(mySet))



#Tuple constructor
print("\nSet Constructor: ")
myNewSet = set(("VSC" , "Sublime", "Notepad"))
print(myNewSet)
print(type(myNewSet))
