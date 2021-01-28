

while True:
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
    elif operation == '6':
        break
    else:
        print('Selection was not correct.')


print("Thank you!")
