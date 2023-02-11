import random

from input import get_int

LOWEST_NUMBER = 1
HIGHEST_NUMBER = 10


def main():
    number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)

    while 1:
        guess = get_int(f"guess a random number from {LOWEST_NUMBER} to {HIGHEST_NUMBER}: ")

        if guess == number:
            print("congrats! you guessed correctly!")
            break
        else:
            print("you guessed incorrectly!\n")


if __name__ == "__main__":
    main()
