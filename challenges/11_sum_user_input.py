from input import get_int


def main():
    start = get_int("enter the start: ")
    end = get_int("enter the end: ")
    step = get_int("enter the steps: ")
    total = sum(range(start, end + 1, step))
    print(f"the sum of all numbers in that range is {total:,}")


if __name__ == "__main__":
    main()
