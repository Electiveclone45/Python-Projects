import random

numberGuess = random.randint(1, 21)
low = 1
high = 20
attempt = 1

while True:  #While the conditions are true, the loop will continue
  personGuess = int(input("Enter a number between 1 and 20: "))
  if personGuess == numberGuess:  #If number equals number, then print success and end loop
    print("You guessed the number!")
    break
  elif personGuess < numberGuess and personGuess >= low:  #If number is less than number and greater than low, then print too low and continue loop
    print("Too low!")
    attempt += 1
    continue
  elif personGuess > numberGuess and personGuess <= high:  #If number is greater than number and less than high, then print too high and continue loop
    print("Too high!")
    attempt += 1
    continue
  else:  #If number is not in range, then print invalid and continue loop
    print("Number not recognised. Please try again.")

print(f"Well done! {attempt} attempts!")
