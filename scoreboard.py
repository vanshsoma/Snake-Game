from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial Black", 24, "normal"))

    def another(self):
        self.goto(0, 0)
        self.write("CHOOSE ANOTHER LEVEL", align="center", font=("Arial Black", 24, "normal"))
        time.sleep(3)
        
    def increase_score(self):
        self.score += 10
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def decrease_score(self):
        self.score -= 10
        self.clear()
        self.update_scoreboard()
