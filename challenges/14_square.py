from turtle import forward, right, exitonclick

SIDES = 4
SIDE_LENGTH = 50
ANGLE = 90


def main():
    for _ in range(SIDES):
        forward(SIDE_LENGTH)
        right(ANGLE)
    exitonclick()


if __name__ == "__main__":
    main()
