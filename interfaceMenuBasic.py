print("Menu")
print("--------------")
print("1. Option 1")
print("2. Option 2")
print("3. Option 3")
print("--------------")

userName = input("Please enter your name: ")
print(userName)
menuChoice = input("Please make a selection from the above: ")
print(menuChoice)

if menuChoice == "1":
  print("Welcome", userName, "Selected Option 1")
elif menuChoice == "2":
  print("Welcome", userName, "Selected Option 2")
elif menuChoice == "3":
  print("Welcome", userName, "Selected Option 3")
else:
  print("Not a valid choice")
