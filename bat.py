from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Bat:

    def __init__(self, position):
        self.segment = []
        self.create_bat(position)
        self.bat = self.segment[0]
        # print(self.segment)

    def create_bat(self, position):
        bat = Turtle()
        bat.penup()
        bat.shape("square")
        bat.color("white")
        bat.shapesize(stretch_wid=5, stretch_len=1)     # Stretch the shape longer
        # bat.speed("fastest")
        bat.goto(position, 0)      # Set the initial position of the bat where x is at the end of screen, y at 0
        self.segment.append(bat)    # Add bat to segment list, this list is made to control the movement of the bat

    def up(self):
        new_y = self.bat.ycor() + 50
        self.bat.goto(self.bat.xcor(), new_y)

    def down(self):
        new_y = self.bat.ycor() - 50
        self.bat.goto(self.bat.xcor(), new_y)

