from input import get_int

NUMBERS = 4


def is_arithmetic(sequence: list) -> bool:
    delta = sequence[1] - sequence[0]  # difference between the first and second element
    for i in range(len(sequence) - 1):
        if not sequence[i + 1] - sequence[i] == delta:  # if the diff between current and next element is equal to delta
            return False
    return True


def main():
    numbers = []
    for i in range(NUMBERS):
        number = get_int(f"input number #{i + 1}: ")
        numbers.append(number)

    if is_arithmetic(numbers):
        print(f"{numbers} is an arithmetic sequence")
    else:
        print(f"{numbers} is not an arithmetic sequence")


if __name__ == "__main__":
    main()
