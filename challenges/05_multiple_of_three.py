import input


def main():
    whole_number = input.get_int("please enter a whole number: ")

    if whole_number % 3 == 0:
        print(f"{whole_number:,} is divisible by 3")
    else:
        print(f"{whole_number:,} is not divisible by 3")


if __name__ == "__main__":
    main()
