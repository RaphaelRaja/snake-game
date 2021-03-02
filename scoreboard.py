from food import Turtle
ALIGNMENT = "center"
FONT = ("Comic Sans MS", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.count}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.count += 1
        self.clear()
        self.update_scoreboard()
