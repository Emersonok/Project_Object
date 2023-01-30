import turtle as t
import random

angles = [90, 180, 270, 360]
jerry = t.Turtle()
t.colormode(255)

def random_color():
    r =random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def direction(turtle_name):
    for x in range(200):
        jerry.speed(0)
        jerry.width(10)
        jerry.color(random_color())
        jerry.forward(20)
        jerry.setheading(random.choice(angles))
        
        

direction(jerry)



screen = t.Screen()
screen.exitonclick()
