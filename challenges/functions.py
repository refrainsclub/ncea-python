import turtle
import input
import random

SPEED = 0
SUNGLASSES = "assets/sunglasses.gif"
COLORS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")


def draw_eye(x: float, y: float, size: float, color):
    setup(x, y, color)
    turtle.circle(size)


def draw_outline(x: float, y: float, size: float, color):
    setup(x, y, color)
    turtle.circle(size)


def setup(x: float, y: float, color="black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)  # sets the orientation of the turtle to 0 degrees
    turtle.pencolor(color)
    turtle.pendown()


def draw_sunglasses(x: float, y: float):
    setup(x, y)
    screen = turtle.Screen()
    screen.addshape(SUNGLASSES)
    turtle.shape(SUNGLASSES)


def get_random_color() -> str:
    return "#" + "".join(random.choices(COLORS, k=6))


def main():
    turtle.speed(SPEED)
    draw_outline(-50, -150, 150, get_random_color())
    draw_eye(-150, 50, 12, get_random_color())  # first eye
    draw_eye(50, 50, 12, get_random_color())  # second eye

    cool = input.get_string("am i cool? (y/n): ", ["y", "n"])
    if cool == "y":
        draw_sunglasses(-50, 50)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
