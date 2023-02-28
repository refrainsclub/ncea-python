from turtle import forward, right, exitonclick

SIDES = 6
SIDE_LENGTH = 50
ANGLE = 60


def main():
    for _ in range(SIDES):
        forward(SIDE_LENGTH)
        right(ANGLE)
    exitonclick()


if __name__ == "__main__":
    main()
