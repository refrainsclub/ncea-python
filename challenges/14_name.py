import turtle


def main():
    turtle.color("red")
    turtle.pensize(2)

    # j
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(100)

    # gap
    turtle.up()
    turtle.forward(25)
    turtle.right(90)
    turtle.down()

    # b1
    turtle.forward(200)

    # b2
    for _ in range(3):
        turtle.left(90)
        turtle.forward(100)

    # b3
    for _ in range(2):
        turtle.right(90)
        turtle.forward(100)

    turtle.right(90)
    turtle.forward(80)

    turtle.right(90)
    turtle.forward(100)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
