def main():
    hours = int(input("how many hours? "))
    minutes = int(input("how many minutes? "))
    seconds = int(input("how many seconds? "))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    print(f"{hours:,}h, {minutes:,}m, and {seconds:,}s is equal to {total_seconds:,}s")


if __name__ == "__main__":
    main()
