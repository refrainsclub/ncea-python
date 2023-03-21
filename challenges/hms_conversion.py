import input

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def main():
    hours = input.get_int("how many hours? ")
    minutes = input.get_int("how many minutes? ")
    seconds = input.get_int("how many seconds? ")
    total_seconds = hours * SECONDS_IN_HOUR + minutes * SECONDS_IN_MINUTE + seconds
    print(f"{hours:,}h, {minutes:,}m, and {seconds:,}s is equal to {total_seconds:,}s")


if __name__ == "__main__":
    main()
