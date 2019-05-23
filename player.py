from objects import *
class Player(Object):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color)

    def move_to_ball(self, ball):
        distance = ball_distance(self, ball)
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

    def rotate_ball(self, ball, angle):
        #self.pos.rotated(angle)
        ball.pos.rotated(angle)

            
class Keeper(Player):
    pass

class Defender(Player):
    pass

class Midfielder(Player):
    pass

class Attacker(Player):
    pass