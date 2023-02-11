def main():
    number = 0
    while number < 1 or number > 100:
        number = input("enter a number between 1 and 100: ")
        if not number.isdigit():
            print("please enter a number\n")
            continue
        number = int(number)

    if number % 2 == 0:
        print("that number is even")
    else:
        print("that number is odd")


if __name__ == "__main__":
    main()
