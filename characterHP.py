import random

print("Random HP")
anyNumber = int(input("Enter the number of sides on the dice: "))  #Entering number for first dice.


def playerHealth():  #Defining the function.
  dice1 = random.randint(1, anyNumber)
  dice2 = random.randint(1, 6)
  dice3 = random.randint(1, 8)
  health = dice1 * dice2 * dice3  #Calculating health
  return health  #Returning the hp stored in health variable.


while True:  #Setting loop for prompts to user.
  characterName = input("Enter the character's name: ")
  hp = playerHealth()
  print(f"Name: Character: {characterName}, hp: {hp}")
  continue
