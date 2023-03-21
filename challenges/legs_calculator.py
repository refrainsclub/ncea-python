import input

COW_LEGS = 4
SHEEP_LEGS = 4
HORSE_LEGS = 4
LIZARD_LEGS = 4
CHICKEN_LEGS = 2


def main():
    cows = input.get_int("how many cows do you have? ")
    sheep = input.get_int("how many sheep do you have? ")
    horses = input.get_int("how many horses do you have?")
    lizards = input.get_int("how many lizards do you have? ")
    chickens = input.get_int("how many chickens do you have? ")
    legs = cows * COW_LEGS + sheep * SHEEP_LEGS + horses * HORSE_LEGS + lizards * LIZARD_LEGS + chickens * CHICKEN_LEGS
    print(f"you have {legs:,} legs on your farm")


if __name__ == "__main__":
    main()
