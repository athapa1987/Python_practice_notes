# addition
print (2 + 2)
# Subtraction
print (4 - 2)
# division
print (6/3)
#multiplication
print(2 * 2)
# exponent
print (2**4)
# reminder
print (21%6)
# division and get intenger
print(13//2)
# rule of precendent
print(4*9/3)
print (6/3*4)
print  (6 - 2 + 5)
print (6+7-2)
print (100-4**3*4/8+10-2)
print ((2+2)**2/4)
print ('Ardee'+'Thapa')
print ('Ardeep'*5)
# assign variable to numbers:
price = 5
quantity = 5
total_price = price * quantity
print (total_price)
# assigning multiple values
x, y, z = 1, 2, 3
quantity_x = 2
quantity_y = 3
quantity_z = 4
sub_total= x * quantity_x + y * quantity_y + z * quantity_z
total_price = sub_total+sub_total*0.2
print (f'your total price is ${total_price}. \n Thank you for the shopping.')
print ('your total price is $' + str(total_price) + '\nThank you for the shopping with us.')
x = 5
print (x == 6)
print (x > 4 and x < 7)
print (x != 2)
print (x < 6 or x > 6)
print (x >= 5)
print (x <=5)
print (x<2 and x > 4)
# trying with input function:
print (input ('Please enter your name? :\t '.upper()).upper())
print (input ('please enter your age? : \t'. upper()))
name = input ('What is your name?: ')
age = input ('How old are you?: ')
print ('Nice to meet you ' + name.title())
print ('You will be ' + str(int(age) + 1)  + ' next year.')
#exercise:
print ((('='*5) + "This will ask two numbers from user and give the sum of the number" + ('='*5)).center(50).upper())
first_number = input('please enter the first number:\t' .upper())
second_number = input('please enter the second number:\t'.upper())
sum = int(first_number) + int(second_number)
print (f'the total of your given number is {sum}.'.capitalize())

print ((('='*5) + 'This will ask the quantity and price and caculate total price' + ('='*5)).center(50).upper())
quantity = input ('Please enter the quantity?:\t\t'.title())
price = input ('Please enter the price of product?:\t\t'.title())
total_price = int(quantity) * float(price)
print (f'Your Total is {total_price}\n')

print ((('='*5) + 'welcome to your age calculator' + ('='*5)).center(50).upper())
birth_year = input ('please enter your birth year:\t\t'.upper())
age = 2026 - int(birth_year)
print (f'You are {age} years old.')
print ((('-'*10) + 'end' + ('-'*10)).center(50).upper())
