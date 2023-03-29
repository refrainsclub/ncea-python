import turtle
import input
import random

# Turtle Settings
SPEED = 0
PEN_SIZE = 1
HEADING = 0

# Assets
SUNGLASSES = "assets/sunglasses.gif"

# Colors
COLORS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")

# Prompt
PROMPT = "am i cool? (y/n): "
VALID_CHOICES = ["y", "yes", "n", "no"]
YES = ("y", "yes")
NO = ("n", "no")
YES_OUTPUT = "Yay! I'm cool!"
NO_OUTPUT = "Aww, I'm not cool :("

# Outline Shape
OUTLINE_LOCATION = (-50, -150)
OUTLINE_SIZE = 150

# Left Eye Shape
LEFT_EYE_LOCATION = (-150, 50)
LEFT_EYE_SIZE = 12

# Right Eye Shape
RIGHT_EYE_LOCATION = (50, 50)
RIGHT_EYE_SIZE = 12

# Sunglasses Shape
SUNGLASSES_LOCATION = (-50, 50)


def main():
    # set up the turtle
    turtle.speed(SPEED)
    turtle.pensize(PEN_SIZE)

    # draw the base
    draw_circle(OUTLINE_LOCATION[0], OUTLINE_LOCATION[1], OUTLINE_SIZE, get_color())  # outline
    draw_circle(LEFT_EYE_LOCATION[0], LEFT_EYE_LOCATION[1], LEFT_EYE_SIZE, get_color())  # first eye
    draw_circle(RIGHT_EYE_LOCATION[0], RIGHT_EYE_LOCATION[1], RIGHT_EYE_SIZE, get_color())  # second eye

    # ask the user if it is cool
    cool = input.get_string(PROMPT, VALID_CHOICES)
    if cool in YES:
        draw_sunglasses(SUNGLASSES_LOCATION[0], SUNGLASSES_LOCATION[1])
        print(YES_OUTPUT)
    elif cool in NO:
        print(NO_OUTPUT)

    turtle.exitonclick()


def draw_circle(x: float, y: float, size: float, color):
    setup(x, y, color)
    turtle.circle(size)


def setup(x: float, y: float, color=None):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(HEADING)  # sets the orientation of the turtle
    if color is not None:
        turtle.pencolor(color)
    turtle.pendown()


def draw_sunglasses(x: float, y: float):
    setup(x, y)
    draw_gif(SUNGLASSES)


def draw_gif(gif: str):
    screen = turtle.Screen()
    screen.addshape(gif)
    turtle.shape(gif)


def get_color() -> str:
    return "#" + "".join(random.choices(COLORS, k=6))


if __name__ == "__main__":
    main()
