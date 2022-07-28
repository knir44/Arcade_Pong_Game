from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800,800)
screen.title("Pong")





r_player = Paddle(350,0)
l_player = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()





screen.listen()
screen.onkeypress(r_player.go_up, "Up")
screen.onkeypress(r_player.go_down, "Down")
screen.onkeypress(l_player.go_up, "w")
screen.onkeypress(l_player.go_down, "s")


game_on = True
while game_on:

    screen.update()
    ball.move()
    #if the ball collide the wall
    if ball.ycor() > 360 or ball.ycor() < - 360:
        ball.bounce_y()
    #if the ball collide the paddle
    if ball.distance(r_player) < 50 and ball.xcor() > 340 or ball.distance(l_player) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    #right's paddle score
    if ball.xcor() > 380:
        ball.rest_position()
        scoreboard.l_point()

    #left's paddle score
    if ball.xcor() < -380:
        ball.rest_position()
        scoreboard.r_point()

    #if we have a winner   - 5 scores
    game_on = scoreboard.winner()



screen.exitonclick()

