import random

from input import get_int


def main():
    number = random.randint(1, 10)

    while 1:
        guess = get_int("guess a random number from 1 to 10: ")

        if guess == number:
            print("congrats! you guessed correctly!")
            break
        else:
            print("you guessed incorrectly!\n")


if __name__ == "__main__":
    main()
