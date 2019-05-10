from precode import *
from variables import *
from pygame.color import *

class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        
        super().__init__()
        
        self.radius = PLAYER_RADIUS 
        self.speed = Vector2D(0,0)
        self.img = img

        self.image = self.img

        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 0
        
        self.dir_x = 0
        self.dir_y = 0

    def move(self):
        self.rect.x += math.cos(math.radians(self.angle + 90)) * 2
        self.rect.y -= math.sin(math.radians(self.angle + 90)) * 2
    
    def update(self):
        self.rect.x += self.dir_x
        self.rect.y += self.dir_y
        self.image = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

class Ball(Object):
    pass

class Player(Object):
    def __init__(self, img, x, y):
        super().__init__(img, x, y)

    
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