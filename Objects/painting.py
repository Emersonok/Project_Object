import turtle as t
import random

jerry = t.Turtle()
t.colormode(255)
jerry.speed(0)
jerry.hideturtle()
jerry.penup()


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

def back():
    jerry.left(180)
    jerry.forward(200)
    jerry.right(90)
    jerry.forward(20)
    jerry.right(90)

def movement():
    for y in range(10):
        jerry.color(colors())
        jerry.dot(10)
        jerry.forward(20)

for x in range(10):
    movement()
    back()
    
    

        

screen = t.Screen()
screen.exitonclick()

