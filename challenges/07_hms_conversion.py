from input import get_int


def main():
    hours = get_int("how many hours? ")
    minutes = get_int("how many minutes? ")
    seconds = get_int("how many seconds? ")
    total_seconds = hours * 3600 + minutes * 60 + seconds
    print(f"{hours:,}h, {minutes:,}m, and {seconds:,}s is equal to {total_seconds:,}s")


if __name__ == "__main__":
    main()
