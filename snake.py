from turtle import Turtle

# List of first 3 tuples of snake body
POS = [(0, 0), (-20, 0), (-40, 0)]
# Amount of distance the snake segments should move
MOVE_DISTANCE = 20
# Directional constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # Create list to append snake body Turtle objects to
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    # Create first 3 body segments of snake and append to body list
    def create_snake(self):
        for position in POS:
            self.add_segment(position)

    # Function to add a new segment to the body
    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.body.append(segment)

    # Function to add additional segments at the end of the current body
    def extend(self):
        self.add_segment(self.body[-1].position())

    # Moves the last segment to the position of the segment above it, etc. The first segment is directed elsewhere.
    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg - 1].xcor()
            new_y = self.body[seg - 1].ycor()
            self.body[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Reset the snake to the starting position to begin the game
    def reset_snake(self):
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    # Following four functions are to change the heading of the first segment (head) in the snake's body
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
