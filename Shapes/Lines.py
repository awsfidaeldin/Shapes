import turtle

screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Drawing Lines Practice")

turtle1=turtle.Turtle()
turtle1.shape("turtle")
turtle1.pensize(5)

for i in range(1,11):
    turtle1.forward(100)
    turtle1.backward(100)
    turtle1.left(45)


turtle1.hideturtle()
turtle1.done()

    


