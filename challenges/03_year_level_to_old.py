from input import get_ranged_int

equivalents = {
    1: "J1",
    2: "J2",
    3: "Standard 1",
    4: "Standard 2",
    5: "Standard 3",
    6: "Standard 4",
    7: "Form 1",
    8: "Form 2",
    9: "Form 3",
    10: "Form 4",
    11: "Form 5",
    12: "Form 6",
    13: "Form 7"
}


def main():
    year_level = get_ranged_int("enter a year level (between 1 and 13): ", 1, 13)
    print(f"{year_level} is equivalent to {equivalents.get(year_level)}")


if __name__ == "__main__":
    main()
