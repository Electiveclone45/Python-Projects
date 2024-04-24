nickName = input("Enter your nickname: ")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

operation = input("Enter an operation: ")

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

print(f"Thank you for using the calculator {nickName} !")
