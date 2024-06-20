from turtle import Turtle
import random
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
COLOURS = ["yellow", "red", "green", "purple", "orange"]
MOVING_DISTANCE = 20
random_color = "white"

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#A snake class with its funtionalities
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, posititon):
        new_segment = Turtle("circle")
        new_segment.penup()
        new_segment.color(random_color)
        new_segment.goto(posititon)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVING_DISTANCE)

    def speedUp(self):
        time.sleep(0.1)
        self.move()

    def changeColor(self):
        global random_color
        random_color= random.choice(COLOURS)
        for seg in self.segments:
            seg.color(random_color)

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


