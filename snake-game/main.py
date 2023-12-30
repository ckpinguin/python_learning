from turtle import Screen
import time
from snake import Snake

screen_width = 700
screen_height = 700


screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.title("Sssssnake!")
screen.bgcolor("black")
screen.tracer(0)


# This feels like it's snake's responsibility...
def is_at_border(snake):
    x_pos, y_pos = snake.get_head_position()
    if x_pos >= screen_width / 2 or x_pos <= -(screen_width / 2):
        print("Boing x")
        return True
    if y_pos >= screen_height / 2 or y_pos <= -(screen_height / 2):
        print("Boing y")
        return True
    return False


snake = Snake()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_up, "v")

screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_left, "u")

screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_right, "a")

screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_down, "i")

# screen.onkey(clear, "Escape")

game_is_on = True
while game_is_on:
    snake._move_forward()
    time.sleep(0.1)
    screen.update()

    if is_at_border(snake):
        snake.turn_around()
    snake.print_all_segments_pos()


screen.exitonclick()
