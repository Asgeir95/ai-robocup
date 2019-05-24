from objects import *
class Player(Object):
    def __init__(self, x, y, radius, color, number, tID):
        super().__init__(x, y, radius, color)
        self._has_ball = False
        self.number = number
        self.team = tID
    
    def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)
            
    def move_to_ball(self, ball, view):
        distance = self.pos.get_distance(ball.pos)
        
        senter = Vec2d(0, 0)
        senter += self.pos
        if senter.get_length() != 0:
            speed = (ball.pos - senter) / 10
        
        if distance <= view:
            if not self.has_ball(ball):
                self._has_ball = False
                self.speed += speed
                self.move()
            else: 
                self._has_ball = True

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

    def team_has_ball(self, team):
        for player in team:
            if self is player:
                continue
            if player._has_ball:
                return player
        
        return None

    def find_free_teammate(self, teams, myteam):
        team_list = []
        opposition = []
        for team in teams:
            for player in team.players:
                if self is player:
                    continue
                if player.team == myteam:
                    team_list.append(player)
                else:
                    opposition.append(player)
        
        for opp in opposition:
            a = self.pos.get_angle_between(opp.pos)
            d = self.pos.get_distance(opp.pos)

            for player in team_list:
                angle = self.pos.get_angle_between(player.pos)
                distance = self.pos.get_distance(player.pos)

                if(a - 15 < angle < a+ 15):
                    return player
        
        return None

    def find_free_space(self, teammate, goal):
        goal_dir = (goal.pos - self.pos).normalized()
        teammate_dir = (teammate.pos - self.pos).normalized()
        self.speed *= goal_dir * teammate_dir
        self.move()

    def shoot(self, goal, ball):
        direction = (goal.pos - ball.pos).normalized()
        ball.speed += direction * self.speed.get_length()

    def pass_ball(self, teammate, ball):
        direction = (teammate.pos - ball.pos).normalized()
        ball.speed += direction * self.speed.get_length() + 0.

            
class Keeper(Player):
    def __init__(self, x, y, radius, color, number, tID):
        super().__init__(x, y, radius, color, number, tID)

    def move(self):
        if self.pos.x > SCREEN_X - self.radius:
            self.pos.x = SCREEN_X - self.radius
        if self.pos.x < 0 + self.radius:
            self.pos.x = 0 + self.radius
        if self.pos.y > SCREEN_Y - self.radius:
            self.pos.y = SCREEN_Y - self.radius
        if self.pos.y < 0 + self.radius:
            self.pos.y = 0 + self.radius
        
        if self.number == 1:
            distance = (self.pos - KEEPER_RED_POS).get_length()
        if self.number == 12:
            distance = (self.pos - KEEPER_BLUE_POS).get_length()
        
        if distance > 160:
            self.speed -= self.speed.normalized()*distance

        if self.speed.get_length() >= PLAYER_MAXSPEED:
            self.speed = self.speed.normalized()*PLAYER_MAXSPEED
        
        self.pos += self.speed

class Defender(Player):
    pass

class Attacker(Player):
    pass