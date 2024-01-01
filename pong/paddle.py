from turtle import Turtle


class Paddle(Turtle):

    STEP_SIZE = 10

    def __init__(self, width=20, height=100, x_pos=350, y_pos=0):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.width = width
        self.height = height
        self.speed('fastest')
        self.penup()
        self.goto(x_pos, y_pos)
        self.pendown()

    def set_pos(self, x, y):
        self.position(x, y)

    def move_up(self):
        self.penup()
        self.clear()
        new_y = self.ycor() + self.STEP_SIZE
        self.sety(new_y)

    def move_down(self):
        self.penup()
        self.clear()
        new_y = self.ycor() - self.STEP_SIZE
        self.sety(new_y)
