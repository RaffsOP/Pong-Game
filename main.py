from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


player_1_scoreboard = ScoreBoard((-300, 260))
player_2_scoreboard = ScoreBoard((300, 260))


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move_ball()

    # collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # code collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        speed_x = ball.x_move
        speed_y = ball.y_move
        ball.bounce_x()

    #  checking for collision with left and right walls. writing score
    if ball.xcor() > 380:
        ball.reset_position()
        player_1_scoreboard.increase_score_right()

    if ball.xcor() < -380:
        ball.reset_position()
        player_2_scoreboard.increase_score_left()


screen.exitonclick()

