from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)
choice = screen.textinput("Select", "Choose a winner")
is_game_on = False
all_turtles = []

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-90, -50, -10, 30, 70, 110]

for turtle_index in range(0, 6):
   new_turtle = Turtle("turtle")
   new_turtle.color(colors[turtle_index])
   new_turtle.penup() 
   new_turtle.goto(-230, y_positions[turtle_index])

if choice:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        rand_distance =random.randint(0, 10)
        turtle.forward(rand_distance)
    

screen = Screen()
screen.exitonclick()
