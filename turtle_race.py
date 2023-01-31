from turtle import Turtle, Screen
import random
steps = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
jerry_steps = 0
timmy_steps = 0
tom_steps = 0
robbo_steps = 0
game_over = False
screen = Screen()

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.penup() 

jerry = Turtle()
jerry.shape("turtle")
jerry.color("blue")
jerry.penup()

tom = Turtle()
tom.shape("turtle")
tom.color("green")
tom.penup()

robbo = Turtle()
robbo.shape("turtle")
robbo.penup()

def start_position():
    timmy.setheading(340)
    timmy.backward(370)
    timmy.setheading(0)
    jerry.setheading(350)
    jerry.backward(355)
    jerry.setheading(0)
    tom.backward(350)  
    robbo.setheading(380)
    robbo.backward(370)
    robbo.setheading(0)

def move():
    timmy_step = timmy.forward(random.choice(steps))
    timmy_step += timmy_steps
    jerry_step = jerry.forward(random.choice(steps))
    jerry_step += jerry_steps
    tom_step = tom.forward(random.choice(steps))
    tom_step += tom_steps
    robbo_step = robbo.forward(random.choice(steps))
    robbo_step += robbo_steps




screen.listen()
screen.onkey(start_position, "space")

while not game_over:
  screen.onkey(move, "Return")

  if timmy[steps]== 500 or jerry[steps] == 500 or tom[steps] ==500 or robbo[steps]==500:
    game_over = True





screen = Screen()
screen.exitonclick()
