import input

MIN = 20
MAX = 100


def main():
    number = input.get_ranged_int(f"enter a number between {MIN} and {MAX}: ", MIN, MAX)
    get_fizzbuzz_order(number)


def get_fizzbuzz_order(number: int):
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


if __name__ == '__main__':
    main()
