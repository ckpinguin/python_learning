from turtle import Screen
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

right_paddle = Paddle()
left_paddle = Paddle(x_pos=-350)

""" screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "v")
screen.onkeypress(left_paddle.move_down, "i")
 """


def tick():
    for action in keys_pressed:
        actions[action]()
    screen.update()


keys_pressed = set()

actions = dict(
    up_right=lambda: right_paddle.sety(right_paddle.ycor()+Paddle.STEP_SIZE),
    down_right=lambda: right_paddle.sety(right_paddle.ycor()-Paddle.STEP_SIZE),
    up_left=lambda: left_paddle.sety(left_paddle.ycor()+Paddle.STEP_SIZE),
    down_left=lambda: left_paddle.sety(left_paddle.ycor()-Paddle.STEP_SIZE)
)

screen.onkeypress(lambda: keys_pressed.add("up_right"), key="Up")
screen.onkeypress(lambda: keys_pressed.add("down_right"), key="Down")
screen.onkeyrelease(lambda: keys_pressed.remove("up_right"), key="Up")
screen.onkeyrelease(lambda: keys_pressed.remove("down_right"), key="Down")
screen.onkeypress(lambda: keys_pressed.add("up_left"), key="v")
screen.onkeypress(lambda: keys_pressed.add("down_left"), key="i")
screen.onkeyrelease(lambda: keys_pressed.remove("up_left"), key="v")
screen.onkeyrelease(lambda: keys_pressed.remove("down_left"), key="i")
screen.listen()

game_is_running = True
while game_is_running:
    screen.update()

screen.exitonclick()
