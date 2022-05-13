from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()

    def move(self):
        x = self.xcor() + 10
        y = self.ycor() + 10
        self.goto(x, y)
