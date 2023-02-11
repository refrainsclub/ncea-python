def main():
    age = 0
    while age < 1 or age > 18:
        age = input("what is your age (must be between 1 and 18)? ")
        if not age.isdigit():
            continue
        age = int(age)

    presents = 0
    for i in range(1, age + 1):
        presents += 20 - i
    print(f"at {age}, you should have {presents} presents")


if __name__ == "__main__":
    main()
