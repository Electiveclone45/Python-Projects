#Tip calculator app

#food_amount = 100
food_amount = float(input('Enter food amount $: '))
#tip_percentage = 20 / 100
tip_percentage = float(input('Enter tip percentage %: ')) / 100
tip_amount = food_amount * tip_percentage

#total 
total = food_amount + tip_amount
print('\n\n\n')
print('---------------------------------')
print(f'Food Amount: ${food_amount}')
print(f'Tip Amount: ${tip_amount}')
print('\n')
print(f'Total Amount: ${total}')
print('---------------------------------')
