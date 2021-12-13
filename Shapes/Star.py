import turtle

aws=turtle.Turtle()
aws.pensize(5)
aws.speed(5)
aws.color("#66B032","#B2D732")

aws.begin_fill()
for i in range(12):
    aws.forward(100)
    aws.left(135)
aws.end_fill()

aws.penup()
aws.forward(150)
aws.pendown()

aws.begin_fill()
for i in range(12):
    aws.forward(100)
    aws.left(135)
aws.end_fill()

aws.penup()
aws.forward(-150)
aws.pendown()

aws.begin_fill()
for i in range(12):
    aws.forward(100)
    aws.left(135)
aws.end_fill()

aws.hideturtle()

turtle.done()
