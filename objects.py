from precode import *
from variables import *
from pygame.color import *

class Object:

    def __init__(self, x, y):
        self.pos    = Vector2D(int(x), int(y))
        self.radius = PLAYER_RADIUS 
        self.speed = Vector2D(0,0)

    def move(self, move):
        # Can not move outside screen
        if self.pos.x > SCREEN_X - self.radius:
            self.pos.x = SCREEN_X - self.radius
        if self.pos.x < 0 + self.radius:
            self.pos.x = 0 + self.radius
        if self.pos.y > SCREEN_Y - self.radius:
            self.pos.y = SCREEN_Y - self.radius
        if self.pos.y < 0 + self.radius:
            self.pos.y = 0 + self.radius
        
        if self.speed.magnitude() > PLAYER_MAXSPEED:
            self.speed = self.speed.normalized()*BOID_MAXSPEED

        self.pos += self.speed
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.pos.x, int(self.pos.y)), self.radius))

class Ball(Object):
    pass

class Player(Object):
    pass

class Keeper(Player):
    pass

class Defender(Player):
    pass

class Midfielder(Player):
    pass

class Attacker(Player):
    pass