print("Rock, paper, scissors game")
print("Select your move (R, P or S)")
print()

player1Move = input("Player 1 : ").upper()
player2Move = input("Player 2 : ").upper()
print(player1Move, player2Move)

score1 = 0
score2 = 0

while score1 < 5 and score2 < 5:
  player1Move = input("Player 1 : ").upper()
  player2Move = input("Player 2 : ").upper()

  if player1Move == "R":
    if player2Move == "R":
      print("You both picked Rock, draw!")
    elif player2Move == "S":
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      score1 += 1
    elif player2Move == "P":
      print("Player1's Rock is smothered by Player2's Paper!")
      score2 += 1
    else:
      print("Invalid Move Player 2!")
      break

  elif player1Move == "P":
    if player2Move == "P":
      print("You both picked paper, draw!")
    elif player2Move == "S":
      print("Player1's paper is cut into tiny pieces by Player2's Scissors!")
      score2 += 1
    elif player2Move == "S":
      print("Player2's Rock is smothered by Player1's Paper!")
      score1 += 1
    else:
      print("Invalid Move Player 2!")
      break

  elif player1Move == "S":
    if player2Move == "R":
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
    elif player2Move == "S":
      print(
          "Ka-Shing! Scissors bounce off each other like a dodgy sword fight!")
      score2 += 1
    elif player2Move == "P":
      print("Player1's Scissors make confetti out of Player2's paper!")
      score1 += 1
    else:
      print("Invalid Move Player 2!")
      break
  else:
    print("Invalid Move Player 1")
    break


print("Game Over!")

