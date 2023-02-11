from input import get_ranged_int

LOWEST_NUMBER = 1
HIGHEST_NUMBER = 100


def is_even(number: int):
    return number % 2 == 0


def main():
    number = get_ranged_int(f"enter a number between {LOWEST_NUMBER} and {HIGHEST_NUMBER}: ",
                            LOWEST_NUMBER,
                            HIGHEST_NUMBER)

    if is_even(number):
        print("that number is even")
    else:
        print("that number is odd")


if __name__ == "__main__":
    main()
