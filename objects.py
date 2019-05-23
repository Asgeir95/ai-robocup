from precode import *
from variables import *
from pygame.color import *
from pygame import draw

T1_KEEPER_START_POSX = SCREEN_X / 2 - 150
T1_KEEPER_START_POSY = SCREEN_Y / 2 - 100
T1_DEFENDER_START_POSX = SCREEN_X / 2 - 150
T1_DEFENDER_START_POSY = SCREEN_Y / 2
T1_MIDFIELDER_START_POSX = SCREEN_X / 2 - 150
T1_MIDFIELDER_START_POSY = SCREEN_Y / 2 + 100

T2_KEEPER_START_POSX = SCREEN_X / 2 - 150
T2_KEEPER_START_POSY = SCREEN_Y / 2 + 100
T2_DEFENDER_START_POSX = SCREEN_X / 2 + 150
T2_DEFENDER_START_POSY = SCREEN_Y / 2
T2_MIDFIELDER_START_POSX = SCREEN_X / 2 + 150
T2_MIDFIELDER_START_POSY = SCREEN_Y / 2 - 100


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):

        super().__init__()
        self.pos = Vector2D(x, y)
        self.radius = radius
        self.speed = Vector2D(55, 5)
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

        if self.speed.magnitude() > BOID_MAXSPEED:
            self.speed = self.speed.normalized() * BOID_MAXSPEED

        self.pos += self.speed

    def draw(self, screen):
        pygame.draw.circle(
            screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius
        )
        pygame.draw.line(
            screen,
            THECOLORS["blue"],
            (self.pos.x, self.pos.y),
            (self.pos.x + self.speed.x * 2, self.pos.y + self.speed.y * 2),
            3,
        )


class Ball(Object):
    ...


class Player(Object):
    def rotate_right(self, angle):
        self.angle -= angle

        if self.angle >= 360:
            self.angle = 0

    def rotate_left(self, angle):
        self.angle += angle

        if self.angle >= 360:
            self.angle = 0


class Keeper(Player):
    ...


class Defender(Player):
    ...


class Midfielder(Player):
    ...


class Attacker(Player):
    ...
