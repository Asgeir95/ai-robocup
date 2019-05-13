from precode import *
from variables import *
from pygame.color import *
import random

class Bird:
    """
    The main class for birds
    """
    def __init__(self):
        self.pos        = Vec2d(int(random.random()*SCREEN_X), int(random.random()*SCREEN_Y))
        self.radius     = BOID_RADIUS
        self.speed      = Vec2d(int(random.random()*0), int(random.random()*-0))

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


class Boid(Bird):
    """
    The class for each boid
    """
    def draw(self, screen):
        pygame.draw.circle(screen, THECOLORS['green'], (int(self.pos.x), int(self.pos.y)), self.radius)
        pygame.draw.line(screen, THECOLORS['blue'], (self.pos.x, self.pos.y), (self.pos.x + self.speed.x*2, self.pos.y + self.speed.y*2), 5)

class Hoik(Bird):
    """
    The class for Hoiks
    """

    def draw(self, screen):
        pygame.draw.circle(screen, THECOLORS['red'], (int(self.pos.x), int(self.pos.y)), HOIK_RADIUS)
        pygame.draw.line(screen, THECOLORS['white'], (self.pos.x, self.pos.y), (self.pos.x + self.speed.x*2, self.pos.y + self.speed.y*2), 5)

class Obstacle:
    """
    The class for obstacles
    """
    def __init__(self):
        self.pos        = Vec2d(int(random.random()*SCREEN_X), int(random.random()*SCREEN_Y))
        self.radius     = OBSTACLE_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, THECOLORS['blue'], (int(self.pos.x), int(self.pos.y)), self.radius)

class Line:
    
    def __init__(self, x, y):
        self.posx = x
        self.posy = y

    def draw(self, screen, direction, length, color = THECOLORS['white']):
        if direction == HORISONTAL:
            pygame.draw.line(screen, color, (self.posx, self.posy), (length, self.posy), 3)
        if direction == VERTICAL: 
            pygame.draw.line(screen, color, (self.posx, self.posy), (self.posx, length), 3)
