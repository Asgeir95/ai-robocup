from utilities import *
from variables import *
from pygame.color import *
from vector2d import Vec2d

class Team():
    def __init__(self, tID):
        self.id = tID
        self.players = []

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
        else:
            return("Player already added")

    def remove_all(self):
        self.players.clear()

class Object():
    def __init__(self, x, y, radius, color):
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


class Line:
    def __init__(self, x, y):
        self._pos = Vec2d(x,y)
        self.direction = None
        self.length = None
        self.w = None
        self.l = None

    def draw(self, screen, direction, length, color = THECOLORS['white']):
        self.length = length
        if direction == HORISONTAL:
            self.w = 3
            self.l = length
            pygame.draw.line(screen, color, (self._pos.x, self._pos.y), (self._pos.x + length, self._pos.y), 3)
        if direction == VERTICAL: 
            self.w = length
            self.l = 3
            pygame.draw.line(screen, color, (self._pos.x, self._pos.y), (self._pos.x, self._pos.y + length), 3)

    @property
    def pos(self):
        return Vec2d(self._pos.x, self._pos.y + (self.length / 2))