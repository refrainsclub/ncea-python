from turtle import forward, right, exitonclick

SIZE = 50


def main():
    for _ in range(6):
        forward(SIZE)
        right(60)
    exitonclick()


if __name__ == "__main__":
    main()
