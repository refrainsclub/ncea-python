import turtle


def draw_eye(x: float, y: float, color):
    setup(x, y, color)
    turtle.circle(12)
    turtle.penup()


def draw_outline(x: float, y: float, color):
    setup(x, y, color)
    turtle.circle(150)
    turtle.penup()


def setup(x: float, y: float, color):
    turtle.goto(x, y)
    turtle.pencolor(color)
    turtle.pendown()


def main():
    turtle.speed(0)
    turtle.penup()
    draw_outline(-50, -150, "red")  # outline
    draw_eye(-150, 50, "blue")  # first eye
    draw_eye(50, 50, "purple")  # second eye
    turtle.exitonclick()


if __name__ == "__main__":
    main()
