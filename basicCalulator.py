#takes in user nickname.
nickName = input("Enter your nickname: ")

#Collects 2 numbers to conduct calculations on.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

#Takes input for the type of operation to be performed on those integers.
operation = input("Enter an operation: ")


#Conditions for those operations provided their is correct input by user.
if operation == "+":
  print(num1 + num2)
elif operation == "-":
  print(num1 - num2)
elif operation == "*":
  print(num1 * num2)
elif operation == "/":
  print(num1 / num2)
elif operation == "%":
  print(num1 % num2)
elif operation == "**":
  print(num1**num2)
else:
  print("Invalid operation!")

#Farewell message output using user's nickname.
print(f"Thank you for using the calculator {nickName} !")
