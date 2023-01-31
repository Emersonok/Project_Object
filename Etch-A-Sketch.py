from turtle import Turtle, Screen

jerry = Turtle()
screen = Screen()


def move_forward():
    jerry.forward(10)
def move_left():
    new_heading = jerry.heading() + 10
    jerry.setheading(new_heading)
def move_backwards():
    jerry.backward(10)
def move_right():
    new_heading = jerry.heading() - 10
    jerry.setheading(new_heading)
def hide_line():
    jerry.penup()
def appear_line():
    jerry.pendown()
def clear_all():
    jerry.reset()

    
    

screen.listen()
screen.onkey(move_forward, "space")
screen.onkey(move_backwards, "Left")
screen.onkey(move_right, "Down")
screen.onkey(move_left, "Up")
screen.onkey(hide_line, "b")
screen.onkey(appear_line, "c")
screen.onkey(clear_all, "x")
screen.exitonclick()