from random import randint
from turtle import exitonclick, colormode, speed, color, circle, right

SPEED = 0              # the speed
ANGLE = 10             # the angle per step
INNER_RADIUS = 100     # the radius of the inner circle
OUTER_RADIUS = 75      # the radius of the outer circle

RGB_MIN = 0
RGB_MAX = 255
RGB_RANGE = 255
FULL_ANGLE = 360


def main():
    speed(SPEED)
    colormode(RGB_RANGE)  # allow rgb colours from 0 to 255
    for _ in range(FULL_ANGLE // ANGLE):
        color(randint(RGB_MIN, RGB_MAX), randint(RGB_MIN, RGB_MAX), randint(RGB_MIN, RGB_MAX))
        circle(INNER_RADIUS)
        circle(OUTER_RADIUS)
        right(ANGLE)
    exitonclick()


if __name__ == "__main__":
    main()
