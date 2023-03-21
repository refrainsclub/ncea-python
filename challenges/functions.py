import turtle


def draw_eye():
    turtle.pendown()
    turtle.pencolor("red")
    turtle.circle(12)
    turtle.penup()


def draw_outline():
    turtle.pendown()
    turtle.pencolor("blue")
    turtle.circle(150)
    turtle.penup()


turtle.penup()
turtle.goto(-50, -150)
draw_outline()
turtle.goto(-150, 50)
draw_eye()
turtle.goto(50, 50)
turtle.left(45)
draw_eye()
turtle.exitonclick()
