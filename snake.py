from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for pos in START_POSITIONS:
            self.create_segment(pos)

    def create_segment(self, pos):
        tim = Turtle("circle")
        tim.penup()
        tim.goto(pos)
        tim.color("red")
        self.turtles.append(tim)

    def reset_snake(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def extend(self):
        self.create_segment(self.turtles[-1].position())

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            prev_x = self.turtles[i - 1].xcor()
            prev_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(prev_x, prev_y)
        self.head.speed("slowest")
        self.head.forward(MOVE_DISTANCE)

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

