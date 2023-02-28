import random
import turtle

SPEED = 0              # the speed
ANGLE = 10             # the angle per step
INNER_RADIUS = 100     # the radius of the inner circle
OUTER_RADIUS = 75      # the radius of the outer circle

RGB_MIN = 0
RGB_MAX = 255
RGB_RANGE = 255
FULL_ANGLE = 360


def main():
    turtle.speed(SPEED)
    turtle.colormode(RGB_RANGE)  # allow rgb colours from 0 to 255
    for _ in range(FULL_ANGLE // ANGLE):
        turtle.color(random.randint(RGB_MIN, RGB_MAX),
                     random.randint(RGB_MIN, RGB_MAX),
                     random.randint(RGB_MIN, RGB_MAX))
        turtle.circle(INNER_RADIUS)
        turtle.circle(OUTER_RADIUS)
        turtle.right(ANGLE)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
