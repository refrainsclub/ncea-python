import datetime
import input


def main():
    age = input.get_int("enter your age: ")
    birthday_passed = input.get_bool("have you had your birthday this year? (y/n): ")
    year = get_birth_year(age, birthday_passed)

    print(f"you were born in {year}")


def get_year() -> int:
    date = datetime.datetime.now()
    return date.year


def get_birth_year(age: int, birthday_passed: bool) -> int:
    current_year = get_year()
    birth_year = current_year - age
    if birthday_passed is False:
        birth_year -= 1
    return birth_year


if __name__ == '__main__':
    main()
