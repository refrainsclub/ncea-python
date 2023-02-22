from input import get_ranged_int

YEARS = 10
GRADUATE_AGE = 18


def main():
    age = get_ranged_int("enter an age: ", 0, 9999)

    future_age = age + YEARS

    print(f"\nin {YEARS:,} years, you will be {future_age:,}")

    if future_age <= GRADUATE_AGE:
        print("and you will be at school")


if __name__ == "__main__":
    main()
