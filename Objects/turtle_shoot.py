from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")


jerry = Turtle()
jerry.shape("classic")
for x in range(15):
    jerry.forward(10)
    jerry.pendown()
    jerry.forward(10)
    jerry.penup()




screen = Screen()
screen.exitonclick()

