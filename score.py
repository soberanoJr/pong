from turtle import Turtle


class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_1 = 0
        self.player_2 = 0
        self.update_score()

    def update_score(self):

        self.clear()
        self.goto(-100, 200)
        self.write(self.player_1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player_2, align="center", font=("Courier", 80, "normal"))

    def point(self, player):
        if player == "player_1":
            self.player_1 += 1
        else:
            self.player_2 += 1
        self.update_score()
