from utilities import *
from variables import *
from pygame.color import *
from vector2d import Vec2d
from rules import *
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
        
        if self.speed.get_length() > PLAYER_MAXSPEED:
            self.speed = self.speed.normalized()*PLAYER_MAXSPEED
        
        self.pos += self.speed

    def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)
            pygame.draw.line(screen, THECOLORS['white'], (self.pos.x, self.pos.y), (self.pos.x + self.speed.x*2, self.pos.y + self.speed.y*2), 5)

class Ball(Object):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color)

    def move(self, speed):
        self.pos += speed

class Player(Object):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color)

    def move_to_ball(self, ball):
        distance = ball_distance(self, ball)
        print("balldistance = {}".format(distance))
        senter = Vec2d(0, 0)
        
        senter += self.pos

        if senter.get_length() != 0:
            return (senter - ball.pos) / 10
        
        return Vec2d(0, 0)

    def catch_ball(self, ball):
        distance = ball_distance(self, ball)

        impact = intersect_circles(self.pos, self.radius, ball.pos, ball.radius)
        if impact:
            return True
        else:
            return False
    
    def pass_ball(self, teammate, ball):
        pos = teammate.pos

            
class Keeper(Player):
    pass

class Defender(Player):
    pass

class Midfielder(Player):
    pass

class Attacker(Player):
    pass