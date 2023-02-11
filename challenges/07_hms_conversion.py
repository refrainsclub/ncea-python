from input import get_int

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def main():
    hours = get_int("how many hours? ")
    minutes = get_int("how many minutes? ")
    seconds = get_int("how many seconds? ")
    total_seconds = hours * SECONDS_IN_HOUR + minutes * SECONDS_IN_MINUTE + seconds
    print(f"{hours:,}h, {minutes:,}m, and {seconds:,}s is equal to {total_seconds:,}s")


if __name__ == "__main__":
    main()
