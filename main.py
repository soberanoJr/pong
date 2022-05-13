from turtle import Screen
from paddle import Paddle


player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))

screen = Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player_1.up, "q")
screen.onkey(player_1.down, "a")
screen.onkey(player_2.up, "p")
screen.onkey(player_2.down, "l")

play = True

while play:

    screen.update()

screen.exitonclick()
