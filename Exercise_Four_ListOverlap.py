'''Take two lists, say for example these two:
and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates).

Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)'''

import random

random_list_1 = random.sample(range(100), 10)
random_list_2 = random.sample(range(100), 10)

setlist = set(random_list_1).intersection(random_list_2)

print(random_list_1)
print(random_list_2)

print(setlist)
