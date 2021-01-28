# In this exercise, expand the calculator so that the user can select what kind of calculation is done.
# If the user chooses 1, the calculator does addition as earlier. If 2,
# the calculator does subtraction, if 3, it does multiplication, if 4, division.
# Also, if the user selects anything else besides 1-4, the program prints "Selection was not correct.".

print('Calculator')
number_1 = int(input('Give the first number: '))
number_2 = int(input('Give the second number: '))
print('current numbers = {} {}'.format(number_1, number_2))
operation = input('''
(1) +
(2) -
(3) *
(4) / 
(5) Change numbers
(6) Quit
Please select something (1-6): 
''')


if operation == '1':
    print('{} + {} = '.format(number_1, number_2))
    print(f"The result is: ", number_1 + number_2)
elif operation == "2":
    print('{} - {} = '.format(number_1, number_2))
    print(f"The result is: ", number_1 - number_2)
elif operation == '3':
    print('{} * {} ='.format(number_1, number_2))
    print(f"The result is: ", number_1 * number_2)
elif operation == '4':
    print('{} / {} = '.format(number_1, number_2))
    print(f"The result is: ", number_1 / number_2)
elif operation == '5':
    number_1 = int(input('Give the first number: '))
    number_2 = int(input('Give the second number: '))
    print('current numbers = {} {}'.format(number_1, number_2))
    operation = input('''
    (1) +
    (2) -
    (3) *
    (4) / 
    (5) Change numbers
    (6) Quit
    Please select something (1-6): 
    ''')
    print('{} + {} = '.format(number_1, number_2))
    print(f"The result is: ", number_1 + number_2)
elif operation == '6':
    print("Thank you!")
else:
    print('Selection was not correct.')
