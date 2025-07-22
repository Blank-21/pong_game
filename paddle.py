
from turtle import Turtle

class Paddle(Turtle):
  def __init__(self,position) -> None:
    super().__init__()
    # Creating the paddle
    self.shape('square')
    self.color("white")
    self.penup()
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.goto(position)
  
  # Creating the paddle movement
  def paddle_up(self):
    y = self.ycor()
    if y < 350:  # Prevent paddle from going off screen
        self.goto(self.xcor(),y + 20)
  
  def paddle_down(self):
    y = self.ycor()
    if y > -350:  # Prevent paddle from going off screen
        self.goto(self.xcor(),y - 20)
