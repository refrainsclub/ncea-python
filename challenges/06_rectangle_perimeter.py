from input import get_float


def main():
    base = get_float("enter the base: ")
    height = get_float("enter the height: ")
    perimeter = base * 2 + height * 2
    print(f"the perimeter is {perimeter:,}")


if __name__ == "__main__":
    main()
