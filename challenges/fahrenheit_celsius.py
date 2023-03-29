import input


def main():
    fahrenheit_temp = get_fahrenheit_temp()

    celsius_temp = convert_to_celsius(fahrenheit_temp)
    celsius_temp_rounded = round(celsius_temp, 2)

    print(f"{fahrenheit_temp:,}°F is equal to {celsius_temp_rounded:,}°C")


def get_fahrenheit_temp() -> float:
    return input.get_float("enter a temperature in fahrenheit: ")


def convert_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


if __name__ == '__main__':
    main()
