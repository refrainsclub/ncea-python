import input

LOWEST_NUMBER = 1
HIGHEST_NUMBER = 100


def is_even(number: int) -> bool:
    return number % 2 == 0


def main():
    number = input.get_ranged_int(f"enter a number between {LOWEST_NUMBER:,} and {HIGHEST_NUMBER:,}: ",
                                  LOWEST_NUMBER,
                                  HIGHEST_NUMBER)

    if is_even(number):
        print(f"{number:,} is even")
    else:
        print(f"{number:,} is odd")


if __name__ == "__main__":
    main()
