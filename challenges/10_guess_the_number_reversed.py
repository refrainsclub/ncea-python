from random import randint

from input import get_string

INITIAL_MIN = 0
INITIAL_MAX = 50


def main():
    answer = ""
    minimum = INITIAL_MIN
    maximum = INITIAL_MAX
    guesses = 0

    print("Think of a number between 1 to 50")
    print("valid choices: [lower, higher, correct]\n")

    while answer != "correct":
        if minimum == maximum:
            print("im out of options.")
            break

        guess = randint(minimum, maximum)
        guesses += 1
        answer = get_string(f"my guess is {guess:.0f}. ", ["lower", "higher", "correct"])

        if answer == "lower":
            maximum = guess - 1
        elif answer == "higher":
            minimum = guess + 1
    else:
        print(f"it took me {guesses} guesses.")


if __name__ == "__main__":
    main()
