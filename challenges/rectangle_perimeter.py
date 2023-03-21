import input


def main():
    base = input.get_float("enter the base: ")
    height = input.get_float("enter the height: ")
    perimeter = base * 2 + height * 2
    print(f"the perimeter is {perimeter:,}")


if __name__ == "__main__":
    main()
