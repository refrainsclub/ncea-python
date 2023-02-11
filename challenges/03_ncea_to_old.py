def main():
    year_level = int(input("Please enter a year level: "))
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

    print("The old level system's equivalent is " + equivalents.get(year_level))


if __name__ == "__main__":
    main()
