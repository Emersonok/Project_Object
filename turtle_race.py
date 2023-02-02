from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)
user_choice = screen.textinput("Select", "Choose a winner")
is_game_on = False
all_turtles = []

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-90, -50, -10, 30, 70, 110]

#use 'for' to multiply the turtles by 6
#create the turtle called new_turtle
#give each turtle a color from colors variable
#make the turtles penup
#create the initial position of turtles using goto(x,y)
#add all the turles to all_turtles list
for each_turtle in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[each_turtle])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[each_turtle])
    all_turtles.append(new_turtle)



#start the game after user selects
if user_choice:
    is_game_on = True
#use while to start the game
#loop through the all turtles list 
#if the x.cor() surpasses 230, then the game ends
#create a variable to get color of the winning turtle
#messages for if the player wins or not
#get the random distances at which turtles move
#ask the turtles to move
while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_turtle = turtle.pencolor()
            if user_choice == winning_turtle:
                print(f"You win! The {winning_turtle} is the winner")
            else:
                print(f"You lose! The {winning_turtle} is the winner")
        random_pace = random.randint(0, 6)
        turtle.forward(random_pace)
screen = Screen()
screen.exitonclick()
