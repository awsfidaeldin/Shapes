#Two Triangles
import turtle

board = turtle.Turtle()
board.pencolor("black")
board.pensize(5)
board.fillcolor("blue")
board.begin_fill()
board.forward(100) # draw base
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.end_fill()
board.right(162)
board.forward(240)
board.right(156)
board.forward(240)
board.hideturtle()
turtle.done()