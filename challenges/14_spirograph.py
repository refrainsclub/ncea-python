from random import randint
from turtle import exitonclick, colormode, speed, color, circle, right

SPEED = 0              # the speed
ANGLE = 10             # the angle per step
INNER_RADIUS = 100     # the radius of the inner circle
OUTER_RADIUS = 75      # the radius of the outer circle


def main():
    speed(SPEED)
    colormode(255)  # allow rgb colours from 0 to 255
    for _ in range(360 // ANGLE):
        color(randint(0, 255), randint(0, 255), randint(0, 255))
        circle(INNER_RADIUS)
        circle(OUTER_RADIUS)
        right(ANGLE)
    exitonclick()


if __name__ == "__main__":
    main()
