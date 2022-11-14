import turtle
def rectangle(edge=100):
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)

def triangle(edge=15):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)

rectangle()

turtle.circle(40)
turtle.circle(25)

turtle.forward(100)

turtle.circle(40)
turtle.circle(25)

turtle.right(138)
turtle.penup()
turtle.forward(26)
turtle.pendown()
turtle.circle(10)

turtle.right(46)
turtle.penup()
turtle.forward(47)
turtle.pendown()
turtle.circle(10)



turtle.left(130)
turtle.penup()
turtle.forward(38)
turtle.pendown()
triangle()

turtle.left(23)
turtle.penup()
turtle.forward(28)
turtle.pendown()
turtle.circle(13, 200)
