from math import sqrt


def main():
    base = int(input("please enter the base of the triangle: "))
    height = int(input("please enter the height of the triangle: "))
    hypotenuse = sqrt(base**2+height**2)
    perimeter = base + height + hypotenuse
    print("the perimeter of that triangle is " + str(perimeter))


if __name__ == "__main__":
    main()