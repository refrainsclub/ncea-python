def main():
    cows = int(input("how many cows do you have? "))
    sheep = int(input("how many sheep do you have? "))
    horses = int(input("how many horses do you have?"))
    lizards = int(input("how many lizards do you have? "))
    chickens = int(input("how many chickens do you have? "))
    legs = cows * 4 + sheep * 4 + horses * 4 + lizards * 4 + chickens * 4
    print(f"you have {legs} legs on your farm")


if __name__ == "__main__":
    main()
