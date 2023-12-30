from turtle import Turtle


class Snake(Turtle):
    STARTING_POSITIONS = [(-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20

    def __init__(self):
        super().__init__()
        self.segments = []
        self._setup_snake()
        self._head = self.segments[0]

    def _setup_head(self):
        head = Turtle("square")
        head.color("green")
        head.penup()
        head.goto(0, 0)
        self.segments.append(head)

    def _setup_snake(self):
        self._setup_head()
        for position in Snake.STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def _segments_follow_head(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            segment = self.segments[seg_num]
            segment.goto(new_x, new_y)

    def _move_forward(self):
        self._segments_follow_head()
        self._head.forward(self.MOVE_DISTANCE)

    def turn_around(self):
        self._head.right(180)

    def move_up(self):
        self._head.setheading(90)

    def move_down(self):
        self._head.setheading(270)

    def move_right(self):
        self._head.setheading(0)

    def move_left(self):
        self._head.setheading(180)

    def get_head_position(self):
        print(self.segments[0].pos())
        return self.segments[0].pos()

    def print_all_segments_pos(self):
        print("All segments")
        for seg in self.segments:
            print(seg.pos())
        print("############")
