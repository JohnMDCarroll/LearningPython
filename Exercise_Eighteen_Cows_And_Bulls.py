import random

if __name__ == "__main__":
    n = True

    while n:
        print("Welcome to cows and bulls game.\nIf you want to quit type 'exit'")

        # If you want unique digits uncomment use the code below
        # numbers = random.sample(range(0, 10), 4)
        # numbers_str = "".join([str(num) for num in numbers])
        #
        #
        numbers_str = str(random.randint(10000, 99999))[1:5]  # and comment or remove this part
        #

        m = True
        counter = 0

        while m:
            # If you want to check count and correctness.
            # print(numbers_str)
            # print(counter)

            guess = input("Guess our 4 digit number: ")

            if guess == 'exit':
                n = False
                break

            elif len(guess) != 4:
                print("Wrong input!")
                continue

            # comparing numbers. I guess my logic works for both case but i think it is about the
            # definition of the game

            cows = len([numbers_str[i] for i in range(len(numbers_str)) if numbers_str[i] == guess[i]])
            s = len([num for num in numbers_str if num in guess])
            bulls = s - cows

            if cows == len(numbers_str):
                counter += 1
                print("Congratulations you predicted in %d tries." % counter)
                m = False
            else:
                counter += 1
                print("You have " + str(cows) + " cows and " + str(bulls) + " bulls.")
