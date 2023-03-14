import input
import turtle


def main():
    sides = input.get_ranged_int("how many sides should the shape have? ", 3, 40)
    length = input.get_ranged_int("what should the length of the sides be? ", 1, 200)
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(360 / sides)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
