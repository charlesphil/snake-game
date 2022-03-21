from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randrange(-280, 280, 20)
        rand_y = random.randrange(-280, 280, 20)
        self.goto(rand_x, rand_y)