def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    fahrenheit_temp = int(input("Please enter a temperature in fahrenheit: "))
    celsius_temp = convert_to_celsius(fahrenheit_temp)
    celsius_temp_rounded = round(celsius_temp)

    print(str(fahrenheit_temp) + "°F is equal to " + str(celsius_temp_rounded) + "°C")

    output = "That temperature is "

    if celsius_temp < 16:
        output += "cold"
    elif celsius_temp < 24:
        output += "warm"
    else:
        output += "hot"

    print(output)


if __name__ == "__main__":
    main()
