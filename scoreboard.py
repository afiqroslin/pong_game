from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.player2_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-300, 200)
        self.write(f"{self.player_score}", align="center", font=('Arial', 30, 'normal'))
        self.goto(300, 200)
        self.write(f"{self.player2_score}", align="center", font=('Arial', 30, 'normal'))

    def player_score_up(self):
        self.player_score += 1
        self.clear()
        self.update_score()
        print(self.player_score)

    def player2_score_up(self):
        self.player2_score += 1
        self.clear()
        self.update_score()
        print(self.player2_score)
