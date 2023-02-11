from input import get_ranged_int


def main():
    number = get_ranged_int("enter a number between 1 and 100: ", 1, 100)

    if number % 2 == 0:
        print("that number is even")
    else:
        print("that number is odd")


if __name__ == "__main__":
    main()
