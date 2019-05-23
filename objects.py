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
        self._pos = Vec2d(x,y)
        self.direction = None
        self.length = None
        self.w = None
        self.l = None

    def draw(self, screen, direction, length, color = THECOLORS['white']):
        self.length = length
        pygame.draw.circle(screen, THECOLORS["red"], (int(self._pos.x), int(self._pos.y)), 5 )
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
        

class Text:
    def __init__(self, x,y, text='text'):
        self.pos = Vec2d(x,y)
        self.font = pygame.font.Font(font_type, 5)
        self.text = str(text)
 
    # Text is adjusted to be in the middle of the screen and setting color to be white
    def text_(self, screen, color = (pygame.color.THECOLORS["white"])):
        x = int(SCREEN_X/2 - self.font.size(self.text)[0]/2)
        y = int(SCREEN_Y/2)
        self.text = self.font.render(self.text, True, color)
        screen.blit(self.text, (x, y))