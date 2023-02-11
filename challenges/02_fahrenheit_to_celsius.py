from input import get_int

WARM_TEMP = 16
HOT_TEMP = 24


def convert_to_celsius(fahrenheit: float):
    return (fahrenheit - 32) * 5 / 9


def main():
    fahrenheit_temp = get_int("enter a temperature in fahrenheit: ")

    celsius_temp = convert_to_celsius(fahrenheit_temp)
    celsius_temp_rounded = round(celsius_temp)

    print(f"{fahrenheit_temp:,}°F is equal to {celsius_temp_rounded:,}°C")

    output = "That temperature is "

    if celsius_temp < WARM_TEMP:
        output += "cold"
    elif celsius_temp < HOT_TEMP:
        output += "warm"
    else:
        output += "hot"

    print(output)


if __name__ == "__main__":
    main()
