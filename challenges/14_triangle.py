from turtle import forward, left, exitonclick

SIZE = 50


def main():
    for _ in range(3):
        forward(SIZE)
        left(120)
    exitonclick()


if __name__ == "__main__":
    main()
