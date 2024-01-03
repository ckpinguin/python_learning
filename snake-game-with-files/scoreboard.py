from turtle import Turtle


class ScoreBoard(Turtle):

    FONT = ("Courier", 22, "normal")
    ALIGNMENT = "center"

    def __init__(self, screen_height):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, (screen_height / 2) - 30)
        self.show_score_on_screen()

    def show_score_on_screen(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}",
                   align=self.ALIGNMENT, font=self.FONT)

    def update_score(self, new_score):
        self.score = new_score

    def increase_score(self, amount):
        self.score += amount
        
    def save_hiscore(self):
        with open('hiscore.txt', 'w') as file:
            file.write(self.high_score)
            

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("G A M E   O V E R", align=self.ALIGNMENT, font=self.FONT)
        self.reset()
