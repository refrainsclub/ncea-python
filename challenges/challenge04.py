# https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-20.php
def is_arithmetic(sequence):
    delta = sequence[1] - sequence[0]
    for index in range(len(sequence) - 1):
        if not (sequence[index + 1] - sequence[index] == delta):
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
