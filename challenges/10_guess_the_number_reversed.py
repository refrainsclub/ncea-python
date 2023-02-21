from random import randint

from input import get_string

INITIAL_MIN = 1
INITIAL_MAX = 100
VALID_CHOICES = ["lower", "higher", "correct"]


def main():
    answer = ""
    minimum = INITIAL_MIN
    maximum = INITIAL_MAX
    guesses = 0

    print(f"Think of a number between {INITIAL_MIN} to {INITIAL_MAX}")
    print("valid choices: [lower, higher, correct]\n")

    while answer != "correct":
        try:
            guess = randint(minimum, maximum)
            guesses += 1
            answer = get_string(f"my guess is {guess:.0f}. ", VALID_CHOICES)

            if answer == "lower":
                maximum = guess - 1
            elif answer == "higher":
                minimum = guess + 1
        except ValueError:
            print("im out of choices")
            break
    else:
        print(f"it took me {guesses} guess(es).")


if __name__ == "__main__":
    main()
