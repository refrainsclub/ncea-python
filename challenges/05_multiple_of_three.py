from input import get_int


def main():
    whole_number = get_int("please enter an int: ")

    if whole_number % 3 == 0:
        print("that number is divisible by 3")
    else:
        print("that number is not divisible by 3")


if __name__ == "__main__":
    main()
