from utilities import *
from variables import *
from pygame.color import *
from vector2d import Vec2d
from rules import *
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        
        super().__init__()
        self.pos = Vec2d(x, y)
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
        
        if self.speed.get_length() >= PLAYER_MAXSPEED:
            self.speed = self.speed.normalized()*PLAYER_MAXSPEED
        
        self.pos += self.speed

    def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)
            pygame.draw.line(screen, THECOLORS['white'], (self.pos.x, self.pos.y), (self.pos.x + self.speed.x*2, self.pos.y + self.speed.y*2), 5)

class Line:
    
    def __init__(self, x, y):
        self.posx = x
        self.posy = y
        self.direction = None
        self.length = None

    def draw(self, screen, direction, length, color = THECOLORS['white']):
        self.length = length
        if direction == HORISONTAL:
            pygame.draw.line(screen, color, (self.posx, self.posy), (length, self.posy), 3)
        if direction == VERTICAL: 
            pygame.draw.line(screen, color, (self.posx, self.posy), (self.posx, length), 3)

    def get_pos(self):
        return ((self.posx, self.posy), self.length)
        
