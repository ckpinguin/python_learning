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

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
    snake.move_head_forward()
    if is_at_border(snake):
        snake.turn_around()
    snake.print_all_segments_pos()


screen.exitonclick()
