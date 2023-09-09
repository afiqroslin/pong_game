from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.x_move = 15
        self.y_move = 15
        self.sleep_time = 0.1  # Set ball speed using time delay

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # print(f"y movement: {self.y_move}")
        # print(f"x movement: {self.x_move}")

    # When the ball hit the top or bottom wall, the y movement will be multiplied with -1 which means it will reverse
    # it direction at same pace
    def bounce_y(self):
        self.y_move *= -1

    # When the ball hit the bat, the x movement will be multiplied with -1 which means it will reverse
    # it direction at same pace
    def bounce_x(self):
        self.x_move *= -1
        self.sleep_time *= 0.9  # Increase the speed of the ball everytime it hits the bat

    # If the ball is out of bound, it will reset it's position to 0
    def out_of_bound(self):
        self.goto(0, 0)
        self.sleep_time = 0.1
