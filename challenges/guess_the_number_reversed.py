import random
import input

INITIAL_MIN = 1
INITIAL_MAX = 100
VALID_CHOICES = ["lower", "higher", "correct"]


def main():
    answer = ""
    minimum = INITIAL_MIN
    maximum = INITIAL_MAX
    guesses = 0

    print(f"Think of a number between {INITIAL_MIN:,} to {INITIAL_MAX:,}")
    print(f"Valid choices: {VALID_CHOICES}\n")

    while answer != "correct":
        try:
            guess = random.randint(minimum, maximum)
            guesses += 1
            answer = input.get_string(f"my guess is {guess:,}. ", VALID_CHOICES)

            if answer == "lower":
                maximum = guess - 1
            elif answer == "higher":
                minimum = guess + 1
        except ValueError:
            print("im out of choices")
            break
    else:
        print(f"it took me {guesses:,} guess(es).")


if __name__ == "__main__":
    main()
