from objects import *
class Player(Object):
    def __init__(self, x, y, radius, color, number):
        super().__init__(x, y, radius, color)
        self._has_ball = False
        self.number = number

    def move_to_ball(self, ball):
        distance = self.pos.get_distance(ball.pos)
        senter = Vec2d(0, 0)
        
        senter += self.pos

        if senter.get_length() != 0:
            return (ball.pos - senter) / 10
        
        return Vec2d(0, 0)

    def has_ball(self, ball):
        distance = self.pos.get_distance(ball.pos)

        impact = intersect_circles(self.pos, self.radius, ball.pos, ball.radius)
        if impact:
            return True
        else:
            return False
    
    def personal_space(self, player_list):
        closeplayers = []
        for player in player_list:
            if self is player:
                continue
            if(player.pos - self.pos).get_length() < self.radius * 3:
                closeplayers.append(player)
            
        if not closeplayers:
            return
        for player in closeplayers:
            dist = self.pos - player.pos
            self.speed += dist * 100


    def pass_ball(self, teammate, ball):
        pos = teammate.pos

    def rotate_ball(self, ball, angle):
        #self.pos.rotated(angle)
        ball.pos.rotated(angle)

            
class Keeper(Player):
    def __init__(self, x, y, radius, color, id):
        super().__init__(x, y, radius, color, id)

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

class Defender(Player):
    pass

class Attacker(Player):
    pass