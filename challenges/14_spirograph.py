import random
from turtle import Turtle, exitonclick

ANGLE = 10          # the angle per step
INNER_RADIUS = 100  # the radius of the inner circle
OUTER_RADIUS = 75   # the radius of the outer circle


def get_random_colour():
    possibles = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f")
    color = "".join(random.choice(possibles) for _ in range(6))
    code = "#" + color
    return code


def main():
    turtle = Turtle()
    turtle.speed(0)
    for i in range(360 // ANGLE):
        turtle.color(get_random_colour())
        turtle.circle(INNER_RADIUS)
        turtle.color(get_random_colour())
        turtle.circle(OUTER_RADIUS)
        turtle.right(ANGLE)
    exitonclick()


if __name__ == "__main__":
    main()
