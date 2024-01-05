from turtle import *
import random
#super class inside parenthesis
#food will have all properties of turtle,just that it will be circular
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("red")
        self.shapesize(0.6,0.6)
        self.relocate()

    def relocate(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)


