from  turtle import Turtle
import random
direction = [-1,1]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.x_move = 0.6
        self.y_move = 0.6



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)


    def bounce_y(self):
        self.y_move *= -1



    def bounce_x(self):
        self.x_move *= -1
        if self.x_move < 0:
            self.x_move -= 0.25
        else:
            self.x_move += 0.25

    def rest_position(self):

        self.x_move = 0.6 * random.choice(direction)
        self.y_move = 0.6 * random.choice(direction)
        self.goto(0,0)
