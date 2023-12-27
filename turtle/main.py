from turtle import Turtle, Screen

tt = Turtle()

tt.shape("turtle")
tt.color("forest green")
tt.width(5)
tt.speed(5)
for _ in range(0, 4):
    tt.forward(100)
    tt.right(90)


screen = Screen()
screen.exitonclick()
