from input import get_int


def main():
    start = get_int("enter the start: ")
    end = get_int("enter the end: ")
    step = get_int("enter the steps: ")
    total = sum(range(start, end, step))
    print(f"the sum of all numbers in range({start}, {end}, {step}) is {total}")


if __name__ == "__main__":
    main()
