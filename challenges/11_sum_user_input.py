import input


def main():
    start = input.get_int("enter the start: ")
    end = input.get_int("enter the end: ")
    step = input.get_int("enter the steps: ")
    total = sum(range(start, end + 1, step))
    print(f"the sum of all numbers in the range {start:,}, {end:,}, {step:,} is {total:,}")


if __name__ == "__main__":
    main()
