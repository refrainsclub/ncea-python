import input

TARGET_TIME = 30
MEMBERS = 2


def main():
    times = []
    differences = []
    fails = 0

    for i in range(MEMBERS):
        time = input.get_float(f"enter time for member {i + 1}: ")
        difference = time - TARGET_TIME

        if difference > 0:
            fails += 1

        times.append(time)
        differences.append(difference)

    average_difference = sum(differences) / len(differences)
    fastest_time = min(times)
    slowest_time = max(times)

    print("\nresults")
    print(f"target time: {TARGET_TIME}")
    print(f"average difference: {average_difference}")
    print(f"fastest time: {fastest_time}")
    print(f"slowest time: {slowest_time}")
    print(f"fails: {fails}")


if __name__ == '__main__':
    main()
