import input


def main():
    base = input.get_float("enter the base: ")
    height = input.get_float("enter the height: ")
    area = base * height / 2
    print(f"the area is {area:,}")


if __name__ == "__main__":
    main()
