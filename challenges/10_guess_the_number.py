import random
import input

LOWEST_NUMBER = 1
HIGHEST_NUMBER = 50


def main():
    number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
    guess = None

    while guess != number:
        guess = input.get_int(f"guess a random number between {LOWEST_NUMBER:,} and {HIGHEST_NUMBER:,}: ")

        if guess < number:
            print("your guess is too low!\n")
        else:
            print("you guess is too high!\n")
    else:
        print("congrats! you guessed correctly!")


if __name__ == "__main__":
    main()
