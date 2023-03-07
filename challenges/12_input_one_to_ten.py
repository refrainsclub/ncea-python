import input


def main():
    number = input.get_ranged_int("Enter a number between 1 and 10: ", 1, 10)
    print(f"Your number was {number}")


if __name__ == "__main__":
    main()
