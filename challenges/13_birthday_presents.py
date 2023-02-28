import input

AGE_MIN = 1
AGE_MAX = 18


def main():
    age = input.get_ranged_int("enter an age (between 1 and 18): ", AGE_MIN, AGE_MAX)

    presents = 0
    for i in range(1, age + 1):
        presents += 20 - i

    print(f"at {age} year(s) old, you should have {presents} presents")


if __name__ == "__main__":
    main()
