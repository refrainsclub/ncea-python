from input import get_int


def main():
    cows = get_int("how many cows do you have? ")
    sheep = get_int("how many sheep do you have? ")
    horses = get_int("how many horses do you have?")
    lizards = get_int("how many lizards do you have? ")
    chickens = get_int("how many chickens do you have? ")
    legs = cows * 4 + sheep * 4 + horses * 4 + lizards * 4 + chickens * 4
    print(f"you have {legs} legs on your farm")


if __name__ == "__main__":
    main()
