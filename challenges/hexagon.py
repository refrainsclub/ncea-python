import turtle

SIDES = 6
SIDE_LENGTH = 50
ANGLE = 60


def main():
    for _ in range(SIDES):
        turtle.forward(SIDE_LENGTH)
        turtle.right(ANGLE)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
