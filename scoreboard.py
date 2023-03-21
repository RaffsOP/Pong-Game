from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard_left()
        self.update_scoreboard_right()

    def game_over(self):
        if self.l_score == 1 or self.r_score == 1:
            self.goto(0, 0)
            self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def update_scoreboard_left(self):
        self.write(f"Score: {self.l_score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard_right(self):
        self.write(f"Score: {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_score_right(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard_right()

    def increase_score_left(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard_left()