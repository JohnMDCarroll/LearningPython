# Exercise 14
# Write a function that asks the user for a string containing multiple words. Print
# back to the user the same string, except with the words in backwards order.

def reverseText(x):
    y = x.split()
    return " ".join(reversed(y))


# test code
test1 = input("Enter a sentence: ")
print(reverseText(test1))
