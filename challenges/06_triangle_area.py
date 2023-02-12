from input import get_float


def main():
    base = get_float("enter the base: ")
    height = get_float("enter the height: ")
    area = base * height / 2
    print(f"the area is {area:,}")


if __name__ == "__main__":
    main()
