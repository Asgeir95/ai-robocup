from precode import *
from variables import *
from pygame.color import *
from vector2d import Vec2d
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        
        super().__init__()
        self.pos        = Vec2d(x, y)
        self.radius = radius 
        self.speed = Vec2d(0,0)
        self.color = color

    def move(self):
        if self.pos.x > SCREEN_X - self.radius:
            self.pos.x = SCREEN_X - self.radius
        if self.pos.x < 0 + self.radius:
            self.pos.x = 0 + self.radius
        if self.pos.y > SCREEN_Y - self.radius:
            self.pos.y = SCREEN_Y - self.radius
        if self.pos.y < 0 + self.radius:
            self.pos.y = 0 + self.radius
        
        if self.speed.get_length() > BOID_MAXSPEED:
            self.speed = self.speed.normalized()*BOID_MAXSPEED
        
        self.pos += self.speed

    def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)
            pygame.draw.line(screen, THECOLORS['white'], (self.pos.x, self.pos.y), (self.pos.x + self.speed.x*2, self.pos.y + self.speed.y*2), 5)

class Ball(Object):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color)

class Player(Object):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color)

    
    def rotate_right(self, angle):
        self.angle -= angle
        
        if self.angle >=360:
            self.angle = 0

    def rotate_left(self, angle):
        self.angle += angle

        if self.angle >=360:
            self.angle = 0


class Keeper(Player):
    pass

class Defender(Player):
    pass

class Midfielder(Player):
    pass

class Attacker(Player):
    pass