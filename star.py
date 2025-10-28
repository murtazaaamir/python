import turtle

turtle.Screen().bgcolor("Green")

board = turtle.Turtle()
#triangel1
board.left(120)
board.forward(100) # draw base
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)
#triangel2
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()