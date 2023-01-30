from turtle import Turtle, Screen
import random




timmy = Turtle()
timmy.color("black")
timmy.pencolor("blue")
colors = ["red", "blue", "black", "green", "yellow"]

def movement(num_sides):
    turn = 360 / num_sides
    for x in range(num_sides):
        timmy.forward(100)
        timmy.right(turn)

for x in range(3, 11):
    timmy.color(random.choice(colors))
    movement(x)
        
    
    
    

    
    
    

my_screen = Screen()
my_screen.exitonclick()

