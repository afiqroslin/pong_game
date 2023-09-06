from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Bat:

    def __init__(self, position):
        self.segment = []
        self.create_bat(position)
        self.bat = self.segment[0]

    def create_bat(self, position):
        bat = Turtle()
        bat.penup()
        bat.shapesize(stretch_wid=5, stretch_len=1)
        bat.shape("square")
        bat.color("white")
        bat.speed("fastest")
        bat.goto(position, 0)
        self.segment.append(bat)

    def up(self):
        new_y = self.bat.ycor() + 20
        self.bat.goto(self.bat.xcor(), new_y)

    def down(self):
        new_y = self.bat.ycor() - 20
        self.bat.goto(self.bat.xcor(), new_y)

    def comp_move(self):
        new_y = self.bat.ycor() + 20
        self.bat.goto(self.bat.xcor(), new_y)
        if self.bat.ycor() < 290:
            new_y = self.bat.ycor() - 20
            self.bat.goto(self.bat.xcor(), new_y)

