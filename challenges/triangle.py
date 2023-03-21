import turtle

SIDES = 3
SIDE_LENGTH = 50
ANGLE = 120


def main():
    for _ in range(SIDES):
        turtle.forward(SIDE_LENGTH)
        turtle.left(ANGLE)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
