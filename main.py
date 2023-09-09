# Author: Afiq Roslin @https://github.com/afiqroslin

from turtle import Screen
from bat import Bat
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player = Bat(-490)
# print(f"Player 1 {player}")

player2 = Bat(480)
# print(f"Player 2 {player2}")

ball = Ball()
score = Scoreboard()

# Set movement key
screen.listen()
screen.onkeypress(player2.up, "Up")     # Onkeypress let the bat keep moving while holding down the key
screen.onkeypress(player2.down, "Down")
screen.onkeypress(player.up, "w")
screen.onkeypress(player.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.sleep_time)
    print(ball.sleep_time)
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with players bat
    if ball.distance(player2.bat) < 30 and ball.xcor() > 320 or ball.distance(player.bat) < 30 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the ball over the left at right side of the screen, it will be out of bound
    if ball.xcor() > 550:
        ball.out_of_bound()
        score.player_score_up()

    if ball.xcor() < -550:
        ball.out_of_bound()
        score.player2_score_up()


screen.exitonclick()
