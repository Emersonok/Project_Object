from turtle import Turtle, Screen

jerry = Turtle()
screen = Screen()


def move_forward():
    jerry.forward(10)
def move_upwards():
    jerry.setheading(90)
def move_downwards():
    jerry.setheading(270)
def move_backwards():
    jerry.setheading(180)
def move_right():
    jerry.setheading(0)
def curve():
    jerry.tilt(25)
    
    

screen.listen()
screen.onkey(key= "space", fun = move_forward)
screen.onkey(key = "Up", fun = move_upwards)
screen.onkey(key = "Down", fun = move_downwards)
screen.onkey(key = "Left", fun = move_backwards)
screen.onkey(key = "Right", fun = move_right)
screen.onkey(key = "v", fun = curve)
screen.exitonclick()