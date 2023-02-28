from turtle import forward, left, exitonclick

SIDES = 3
SIDE_LENGTH = 50
ANGLE = 120


def main():
    for _ in range(SIDES):
        forward(SIDE_LENGTH)
        left(ANGLE)
    exitonclick()


if __name__ == "__main__":
    main()
