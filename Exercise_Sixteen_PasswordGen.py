# Exercise 16
# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input('How many characters should your password be? (Max 50) ---'))
p = "".join(random.sample(s, passlen))
print(p)
