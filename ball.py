from objects import *
from math import log
class Ball(Object):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color)

    def move(self):
        if self.speed.get_length() >= BALL_MAXSPEED:
            self.speed = self.speed.normalized()*BALL_MAXSPEED

        self.pos += self.speed
        self.speed *= 0.98

    def draw(self, screen):
        x = self.radius
        y = self.speed.get_length()
        radius = clamp(x*y, 6, 8)

        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), int(radius))
        pygame.draw.line(screen, THECOLORS['white'], (self.pos.x, self.pos.y), (self.pos.x + self.speed.x*2, self.pos.y + self.speed.y*2), 5)

    def is_goal(self, goal):
        x = goal.pos.x 
        y = goal.pos.y
        y1 = y - (goal.length / 2)
        v = Vec2d(x, y1)

        impact = intersect_rectangle_circle(v, 3, goal.length, self.pos, self.radius, self.speed)
       # print("distance to goal: ", distance)
        if impact: 
            return True
        
        return False

    def is_throwin(self, line):
        x = line.pos.x
        y = line.pos.y
        y1 = y - (line.length/2)
        v = Vec2d(x, y1)

        impact = intersect_rectangle_circle(v, line.length, 3, self.pos, self.radius, self.speed)
        # print("distance to goal: ", distance)
        if impact: 
            return True
        
        return False

    def is_corner(self, line):
        x = line.pos.x
        y = line.pos.y
        y1 = y - (line.length/2)
        v = Vec2d(x, y1)

        impact = intersect_rectangle_circle(v, 3, line.length, self.pos, self.radius, self.speed)
        # print("distance to goal: ", distance)
        if impact: 
            return True
        
        return False

def clamp(my_value, min_value, max_value):
    return max(min(my_value, max_value), min_value)