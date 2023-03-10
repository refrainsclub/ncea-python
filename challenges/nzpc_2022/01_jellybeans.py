def main():
    jelly_beans = get_ranged_int("How many jelly beans are in the jar? ", 50, 1000)
    guesses = get_ranged_int("How many guesses were there? ", 1, 250)

    top_name = None
    top_close = None

    for i in range(guesses):
        name = input("What is the name of the person who guessed? ")
        guess = get_positive_int(f"What was {name}'s guess? ")
        close = get_difference(jelly_beans, guess)

        if top_close is not None and close >= top_close:
            continue

        top_name = name
        top_close = close

    print(top_name)


def get_ranged_int(prompt: str, minimum: int, maximum: int) -> int:
    while 1:
        try:
            result = int(input(prompt))
            if minimum <= result <= maximum:
                return result
            print(f"Please enter a number between {minimum}-{maximum}\n")
        except ValueError:
            print("Please enter an integer!\n")


def get_positive_int(prompt: str):
    while 1:
        try:
            result = int(input(prompt))
            if result >= 0:
                return result
            print("Please enter a positive number!\n")
        except ValueError:
            print("Please enter an integer!\n")


def get_difference(first_number: int, second_number: int) -> int:
    return abs(first_number - second_number)


if __name__ == "__main__":
    main()
