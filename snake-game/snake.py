from turtle import Turtle


class Snake(Turtle):
    starting_positions = [(-20, 0), (-40, 0)]

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
        for position in Snake.starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_forward(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            segment = self.segments[seg_num]
            segment.goto(new_x, new_y)

    def move_head_forward(self):
        self._head.forward(20)
        # if is_at_border(head):
        #    head.right(180)

    def turn_around(self):
        self._head.right(180)

    def turn_right(self):
        self._head.right(90)

    def turn_left(self):
        self._head.left(90)

    def get_head_position(self):
        print(self.segments[0].pos())
        return self.segments[0].pos()

    def print_all_segments_pos(self):
        print("All segments")
        for seg in self.segments:
            print(seg.pos())
        print("############")
