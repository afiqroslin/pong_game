from turtle import Screen, Turtle
from bat import Bat
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player = Bat(-490)
computer = Bat(480)

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()  # Refresh the graphics after all squares moved so it looks like it is one entity moving
    time.sleep(0.1)
    computer.comp_move()

screen.exitonclick()