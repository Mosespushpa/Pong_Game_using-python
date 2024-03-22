from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(position)

    def go_up(self):
        new_Ycor = self.ycor() + 20
        self.goto(self.xcor(), new_Ycor)

    def go_down(self):
        new_Ycor = self.ycor() - 20
        self.goto(self.xcor(), new_Ycor)
