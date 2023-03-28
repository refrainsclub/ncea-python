MIN = 11
MAX = 20


def main():
    print(f"The captain is {get_captain()}")


def get_captain():
    user_input: str = input(f"enter between {MIN} and {MAX} names: ")
    names: list = user_input.split(" ")
    size: int = len(names)

    if size < MIN or size > MAX:
        print("not enough names! \n")
        get_captain()
        return

    names.sort()

    return names[2]


if __name__ == '__main__':
    main()
