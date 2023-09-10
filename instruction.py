from turtle import Turtle


class Instruction(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, -280)
        instruction_text = "  Press 'Up or W' to move up\nPress'Down or S' to move down"
        self.write(instruction_text, align="center", font=('Arial', 10, 'normal'))
