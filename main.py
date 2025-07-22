"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

scoreboard = Scoreboard()

#paddle creation
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#moving the paddle
screen.listen()
screen.onkey(r_paddle.paddle_up,"Up")
screen.onkey(r_paddle.paddle_down,"Down")

screen.onkey(l_paddle.paddle_up,"w")
screen.onkey(l_paddle.paddle_down,"s")

#ball
ball = Ball()

# Game
game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(ball.move_speed)
  ball.move()

  #detect ball off grid
  if ball.ycor() > 280 or ball.ycor() < -250:
    ball.bounce_y()

  #detect ball off paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
    ball.bounce_x()

  #detect missed ball - right
  if ball.xcor() > 380 :
    ball.reset_position()
    scoreboard.update_l_score()

  #detect missed ball - left
  if ball.xcor() < -380 :
    ball.reset_position()
    scoreboard.update_r_score()

screen.exitonclick()
