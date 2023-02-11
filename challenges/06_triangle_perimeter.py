from math import hypot
from input import get_float


def main():
    print("this only works with right-angled triangles")
    base = get_float("enter the base: ")
    height = get_float("enter the height: ")
    hypotenuse = hypot(base, height)
    print(f"the hypotenuse is {round(hypotenuse, 2):,}")
    perimeter = base + height + hypotenuse
    print(f"the perimeter is {round(perimeter, 2):,}")


if __name__ == "__main__":
    main()
