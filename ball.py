from objects import *

class Ball(Object):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color)

    def move(self, speed):
        if self.speed.get_length() >= BALL_MAXSPEED:
            self.speed = self.speed.normalized()*BALL_MAXSPEED

        self.pos += speed
        self.speed += self.pos
