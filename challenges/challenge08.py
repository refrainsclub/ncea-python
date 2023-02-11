def main():
    total_seconds = int(input("enter a whole number of seconds: "))
    hours, minutes = divmod(total_seconds, 3600)  # returns tuple of quotient and remainder
    minutes, seconds = divmod(minutes, 60)
    print(f"{total_seconds:,}s is equal to {hours:,}h {minutes:,}m {seconds:,}s")


if __name__ == "__main__":
    main()
