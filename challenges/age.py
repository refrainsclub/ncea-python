import datetime
import input


def main():
    birth_year = input.get_int("enter your birth year: ")
    birthday_passed = input.get_bool("have you had your birthday this year? (y/n): ")
    year = get_year()
    age = year - birth_year
    if birthday_passed is False:
        age -= 1
    print(f"you are {age} years old")


def get_year() -> int:
    date = datetime.datetime.now()
    return date.year


if __name__ == '__main__':
    main()
