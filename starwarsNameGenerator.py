#Title
print("Star Wars Name Generator!")
print()

#Collecting input of user names
userFirstName = input("What is your first name? ")
userLastName = input("What is your last name? ")

#string slicing to get first 3 letters of first name and last 3 letters of last name
first = userFirstName[:3].upper()
last = userLastName[:-4].upper()

name = first + last #Conducting string concatenation 

print(f"Your Star Wars name is {name}") #printing the name
    
