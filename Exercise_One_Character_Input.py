'''Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.'''

userName = input("Hi, what is your name?")
userAge = int(input("How old are you?"))
centenary = str((2017-userAge) +100)
print(userName + " will be 100 years old in the year " + centenary)