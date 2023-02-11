from math import sqrt
from input import get_int


def main():
    base = get_int("please enter the base of the triangle: ")
    height = get_int("please enter the height of the triangle: ")
    hypotenuse = sqrt(base * base + height * height)  # multiplication is faster than exponentiation
    perimeter = base + height + hypotenuse
    print(f"the perimeter of that triangle is {perimeter:,} units")


if __name__ == "__main__":
    main()
