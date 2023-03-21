import turtle

SPEED = 0


def draw_eye(x: float, y: float, size: float, color):
    setup(x, y, color)
    turtle.circle(size)
    turtle.penup()


def draw_outline(x: float, y: float, size: float, color):
    setup(x, y, color)
    turtle.circle(size)
    turtle.penup()


def setup(x: float, y: float, color):
    turtle.goto(x, y)
    turtle.pencolor(color)
    turtle.pendown()


def main():
    turtle.speed(SPEED)
    turtle.penup()
    draw_outline(-50, -150, 150, "red")  # outline
    draw_eye(-150, 50, 12, "blue")  # first eye
    draw_eye(50, 50, 12, "purple")  # second eye
    turtle.exitonclick()


if __name__ == "__main__":
    main()
