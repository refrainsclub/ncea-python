def is_arithmetic(sequence):
    delta = sequence[1] - sequence[0]  # difference between the first and second element
    for i in range(len(sequence) - 1):
        if not sequence[i + 1] - sequence[i] == delta:  # if the diff between current and next element is equal to delta
            return False
    return True


def main():
    numbers = []
    for i in range(4):
        number = int(input("input number #" + str(i + 1) + ": "))
        numbers.append(number)

    if is_arithmetic(numbers):
        print("that pattern is arithmetic")
    else:
        print("that pattern is not arithmetic")


if __name__ == "__main__":
    main()
