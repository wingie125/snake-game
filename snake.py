from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.timmy = []
        self.create_snake()
        self.head = self.timmy[0]

    # Create our snake
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_new_segment(position)

    def add_new_segment(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.timmy.append(tim)

    def extend(self):
        self.add_new_segment(self.timmy[-1].position())

    def move(self):
        # Move our Snake

        for seg_num in range(len(self.timmy) - 1, 0, -1):
            new_x = self.timmy[seg_num - 1].xcor()
            new_y = self.timmy[seg_num - 1].ycor()
            self.timmy[seg_num].goto(new_x, new_y)
        self.head.forward(MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
