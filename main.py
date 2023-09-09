# Author: Afiq Roslin @https://github.com/afiqroslin

from turtle import Screen
from bat import Bat
from ball import Ball
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

# Set movement key
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with players bat
    if ball.distance(player2.bat) < 25 and ball.xcor() > 320 or ball.distance(player.bat) < 25 and ball.xcor() < -320 :
        ball.bounce_x()

    # Detect if the ball over the left at right side of the screen, it will be out of bound
    if ball.xcor() > 550:
        ball.out_of_bound()

    if ball.xcor() < -550:
        ball.out_of_bound()



screen.exitonclick()