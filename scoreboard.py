import turtle
from turtle import Turtle
alignment = 'center'
font = ("Arial", 24,"normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.write(f"score: {self.score}", align=alignment, font=font)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score}, high score: {self.high_score}", align=alignment, font=font)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode='w') as data:
                data.write(f"{self.high_score}")
            self.score = 0
            self.update_scoreboard()


    # reads

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("white")
    #     self.write(f"Game over!", align=alignment, font=font)









