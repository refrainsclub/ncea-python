import input

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def main():
    total_seconds = input.get_int("enter a whole number of seconds: ")
    hours, minutes = divmod(total_seconds, SECONDS_IN_HOUR)  # returns tuple of quotient and remainder
    minutes, seconds = divmod(minutes, SECONDS_IN_MINUTE)
    print(f"{total_seconds:,}s is equal to {hours:,}h {minutes:,}m {seconds:,}s")


if __name__ == "__main__":
    main()
