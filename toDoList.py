myToDoList = ["Study", "Play", "Sleep"]

def userResponse(view, edit, remove, myToDoList):
  if view == "view":
    print(myToDoList)
  elif edit == "edit":
    item = input("Which item would you like to edit?")
    if item in myToDoList:
      myToDoList.remove(item)
      newItem = input("What would you like to change it to?")
      myToDoList.append(newItem)
      print(myToDoList)
    else:
      print("That item is not in the list.")
  elif remove == "remove":
    item = input("Which item would you like to remove?")
    if item in myToDoList:
      myToDoList.remove(item)
      print(myToDoList)
    else:
      print("Item is not listed.")
  else:
    print("Invalid input")

userResponse('', 'edit', '', myToDoList)
    
