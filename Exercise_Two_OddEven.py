'''Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. '''

userNumber = int(input("Hi, Please input a number : "))

if (userNumber % 2) > 0:
    print('--- ODD ---')
else:
    print('--- EVEN ---')