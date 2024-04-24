#Custom Compliment & Insult Generator
#Instructions
print("""
-----------------------------------------------------
| Welcome to the Complimenter! |
-----------------------------------------------------
Anser the questions provided.
-----------------------------------------------------
After, you answer your name and the day of the week \
you will be prompted with a question on what you did \
that week day. You will answer, then you will get a \
customized compliment or an insult.

-----------------------------------------------------
List of accepted answers include:

- Relax and Unwind
- Outdoor Adventures
- Family Time
- Work and Productivity
- Exercise
- Plan Ahead
- Team Sports
- Cooking and Dining 
- Learn Something New
- Midweek Break
- Socialize 
- Creative Pursuits 
- Drinking 
- Volunteering 
- Cultural Activities
- Dancing 
- Movie Night
- Date Night 
- Outdoor Sports 
- Shopping 
- Home Improvement 

-----------------------------------------------------

""")

#Prompt user for Name and Current day of week.
userName = input("Enter your name: ")
currentDay = input("Enter the current day of the week: ")

#Unique message output for each day of the week based on user input.

#Concatenation of strings and variables to create a customized message.

if currentDay == "Sunday":
  print("A day to unwind, bask in the sun, and savor leisure.")
  # Secondary input taken from within nested control flow
  favouriteThing = input("Enter your favourite thing: ")
  if favouriteThing == "Relax and Unwind.":
    print(f"Yawn, {userName} is boring!")
  elif favouriteThing == "Outdoor Adventures ":
    print(f" {userName} likes living life to the extreme !")
  elif favouriteThing == "Family Time":
    print(f"Nice {userName}, love is the key my friend!")
  else:
    print(f"Fair enough {userName}, each to their own!")

elif currentDay == "Monday":
  print("The start of the week, where possibilities bloom anew.")
  favouriteThing = input("Enter your favourite thing: ")
  if favouriteThing == "Work and Productivity":
    print(f"{userName} likes to stay focused and productive!")
  elif favouriteThing == "":
    print(f"{userName} is getting physical!")
  elif favouriteThing == "Plan Ahead":
    print(f"{userName} is very organized!")
  else:
    print("Fair enough, each to their own!")

elif currentDay == "Tuesday":
  print("A steady rhythm, like a midweek heartbeat.")
  favouriteThing = input("Enter your favourite thing: ")
  if favouriteThing == "Team Sports":
    print(f"Team work makes the dreamwork {userName}!")
  elif favouriteThing == "Cooking and Dining":
    print(f"Cooking and eating are the best {userName}!")
  elif favouriteThing == "Learn Something New":
    print(f"New beginnings for {userName}. That's what it's all about!")
  else:
    print("Fair enough, each to their own!")

elif currentDay == "Wedesday":
  favouriteThing = input("Enter your favourite thing: ")
  print("The hump day, where we climb toward the weekend.")
  if favouriteThing == "Midweek Break":
    print(f"{userName} is taking it easy! What a sluggard!")
  elif favouriteThing == "Socialize":
    print(f"{userName} has friends? Hard to believe! :D ")
  elif favouriteThing == "Creative Pursuits":
    print(f"{userName} speaks with their heart!")
  else:
    print("Fair enough, each to their own!")

elif currentDay == "Thursday":
  print("Anticipation fills the air; the weekend beckons.")
  favouriteThing = input("Enter your favourite thing: ")
  if favouriteThing == "Drinking":
    print(f"Don't throw your life away {userName}")
  elif favouriteThing == "Volunteering":
    print(f"Volunteering is a great way to make a difference {userName}!")
  elif favouriteThing == "Cultural Activities":
    print(
        f"Cultural activities are a great way to connect with others {userName}!"
    )
  else:
    print("Fair enough, each to their own!")

elif currentDay == "Friday":
  print("Cheers to freedom, laughter, and late-night adventures.")
  favouriteThing = input("Enter your favourite thing: ")
  if favouriteThing == "Dancing":
    print(f"Dancing is a great way to express yourself {userName}!")
  elif favouriteThing == "Movie Night":
    print(f"Why not watch a movie {userName}?")
  elif favouriteThing == "Date Night":
    print(f"You're too good for them! Find another one {userName}!")
  else:
    print("Fair enough, each to their own!")

elif currentDay == "Saturday":
  print("A canvas for dreams, where time dances freely.")
  favouriteThing = input("Enter your favourite thing: ")
  if favouriteThing == "Outdoor Sports":
    print(f"{userName} is an outdoorsy type!")
  elif favouriteThing == "Shopping":
    print(f"Shopping is a great way to spend time {userName}!")
  elif favouriteThing == "Home Improvement":
    print(f"{userName}, just be thankful to have a home!")
  else:
    print("Fair enough, each to their own!")

else:
  print(f"{userName} , WTF! wrong planet bro, try again?!")

#Case sensitivity dealt with so that the user can enter the day of the week in any case.
