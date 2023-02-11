from input import get_ranged_int


def main():
    age = get_ranged_int("enter an age: ", 0, 9999)

    age_in_ten_years = age + 10
    graduate_age = 18

    print(f"\nin 10 years, you will be {age_in_ten_years}")

    if age_in_ten_years < graduate_age:
        print("and you will be at school")


if __name__ == "__main__":
    main()
