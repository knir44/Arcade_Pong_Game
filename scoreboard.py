from turtle import Turtle

BLOCK_IN_THE_MIDDLE = []
NUM_OF_LINES = 22





class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.create_line()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def create_line(self):
        y = 360

        for i in range(NUM_OF_LINES):
            sum_cor = (0, y)
            BLOCK_IN_THE_MIDDLE.append(sum_cor)
            y = y - 40

        for index in range(NUM_OF_LINES):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.speed("fastest")
            new_turtle.shapesize(0.7)
            new_turtle.goto(BLOCK_IN_THE_MIDDLE[index])


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def winner(self):
        if self.l_score > 5 or self.r_score > 5:
            if self.r_score > self.l_score:
                winner = "Right"
            else:
                winner = "Left"

            self.penup()
            self.hideturtle()
            self.goto(-150, 20)
            self.color("white")
            self.write(f"{winner} ", align="center", font=("Courier", 60, "normal"))
            self.goto(180, 20)
            self.write("won! ", align="center", font=("Courier", 60, "normal"))
            return False
        return True