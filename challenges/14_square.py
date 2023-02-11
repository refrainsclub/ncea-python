from turtle import forward, right, exitonclick

SIZE = 50


def main():
    for _ in range(4):
        forward(SIZE)
        right(90)
    exitonclick()


if __name__ == "__main__":
    main()
