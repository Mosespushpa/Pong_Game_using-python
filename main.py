from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
s = Screen()
s.setup(width=800,height=600)
s.bgcolor("black")
s.title("___Pong___")
s.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball((0,0))
scoreboard = Scoreboard()
s.listen()
s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")
s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s")



game_is_on = True
while game_is_on:
    time.sleep(ball.speed_move)
    s.update()
    ball.move()
    # Detect the collision of ball to top and buttom walls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    # Detect the collision with r_paddle
    if ball.distance(r_paddle) < 45 and ball.xcor() > 320 or ball.distance(l_paddle) < 45 and ball.xcor() < -320:
        ball.bounce_x()

    # ball missing the paddle
    if ball.xcor() > 380:
        ball.res_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.res_position()
        scoreboard.r_point()

s.exitonclick()