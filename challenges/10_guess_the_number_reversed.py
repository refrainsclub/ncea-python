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
        try:
            guess = randint(minimum, maximum)
            guesses += 1
            answer = get_string(f"my guess is {guess:.0f}. ", ["lower", "higher", "correct"])
            if answer == "lower":
                maximum = guess - 1
            elif answer == "higher":
                minimum = guess + 1
        except ValueError:
            print("i am out of available options.")
            break
    else:
        print(f"i guessed it in {guesses} guesses.")


if __name__ == "__main__":
    main()
