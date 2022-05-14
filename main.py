import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from score import Score


screen = Screen()
player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
ball = Ball()
score = Score()

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

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(player_1) < 50 \
            and ball.xcor() < -320 \
            or ball.distance(player_2) < 50 \
            and ball.xcor() > 320:
        ball.bounce_x()

    # Point
    if ball.xcor() > 380:
        ball.reset()
        score.point("player_1")

    if ball.xcor() < -380:
        ball.reset()
        score.point("player_2")

screen.exitonclick()
