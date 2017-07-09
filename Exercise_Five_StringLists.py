'''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

n = input('Provide a word you would like to test : ')

if (str(n) == str(n)[::-1]):
    print('---PALINDROME---')
else:
    print('---NOT A PALINDROME---')
