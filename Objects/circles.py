import turtle as t
import random

jerry = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_choice = (r, g, b)
    return color_choice
jerry.speed(0)

def spirograph(gap_size):
    for x in range(int(360/gap_size)):
        jerry.color(random_color())
        jerry.circle(60)
        jerry.setheading(jerry.heading() + gap_size)

spirograph(2)





screen = t.Screen()
screen.exitonclick()