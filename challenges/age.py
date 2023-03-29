import datetime
import input


def main():
    birth_year = input.get_int("enter your birth year: ")
    birthday_passed = input.get_bool("have you had your birthday this year? (y/n): ")
    age = get_age(birth_year, birthday_passed)

    print(f"you are {age} years old")


def get_year() -> int:
    date = datetime.datetime.now()
    return date.year


def get_age(birth_year: int, birthday_passed: bool) -> int:
    year = get_year()
    age = year - birth_year
    if birthday_passed is False:
        age -= 1
    return age


if __name__ == '__main__':
    main()
