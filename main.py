from variables import *
from objects import *
from ball import *
from player import *
import random
import time
class Program:
    """
    The class for the program that runs all the files together
    """
    def __init__(self):
        self.screen     = pygame.display.set_mode(SCREEN_SIZE)
        self.sidelines_list = []
        self.vertical_list = []
        self.goalline_list = []
        self.keeper_line_list = []
        ball = Ball(random.uniform(0.75, 1.25)*BALL_POS.x, BALL_POS.y, 6, THECOLORS["yellow"])
        self.red = Team(RED)
        self.blue = Team(BLUE)
        self.add_players()                     
        self.teams = [self.red, self.blue]

        self.ball_list = []
        self.ball_list.append(ball)
        self.redgoals = 0
        self.bluegoals = 0

        self.draw_field()
        
    def draw_field(self): 
        self.screen.fill(THECOLORS['darkgreen'])

        upperline = Line(DISTANCE_FROM_SCREEN, DISTANCE_FROM_SCREEN)
        lowerline  = Line(DISTANCE_FROM_SCREEN, SCREEN_Y - DISTANCE_FROM_SCREEN)

        self.sidelines_list = [upperline, lowerline]

        
        leftlineupper = Line(DISTANCE_FROM_SCREEN, DISTANCE_FROM_SCREEN)
        leftlinelower = Line(DISTANCE_FROM_SCREEN, DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2)
        rigthlineupper = Line(SCREEN_X - DISTANCE_FROM_SCREEN, DISTANCE_FROM_SCREEN)
        rigthlinelower = Line(SCREEN_X - DISTANCE_FROM_SCREEN, DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2)

        self.vertical_list = [leftlineupper, leftlinelower, rigthlineupper,rigthlinelower]
        
        goal1 = Line(DISTANCE_FROM_SCREEN, SCREEN_Y/2 - GOAL/2)
        goal2 = Line(DISTANCE_FROM_SCREEN + FIELD_H, SCREEN_Y/2 - GOAL/2)

        self.goalline_list = [goal1, goal2]


        # just drawings
        midline = Line(SCREEN_X / 2, DISTANCE_FROM_SCREEN)

        penaltyline1 = Line(DISTANCE_FROM_SCREEN, SCREEN_Y/2 + PENTALTY_VERTICAL/2)
        penaltyline2 = Line(DISTANCE_FROM_SCREEN, SCREEN_Y/2 - PENTALTY_VERTICAL/2)
        penaltyline3 = Line(SCREEN_X - DISTANCE_FROM_SCREEN - PENTALTY_HORISONTAL, SCREEN_Y / 2 + PENTALTY_VERTICAL/2)
        penaltyline4 = Line(SCREEN_X - DISTANCE_FROM_SCREEN -PENTALTY_HORISONTAL, SCREEN_Y / 2 - PENTALTY_VERTICAL/2)
        penaltyline5 = Line(DISTANCE_FROM_SCREEN + PENTALTY_HORISONTAL, SCREEN_Y/2 - PENTALTY_VERTICAL/2 )
        penaltyline6 = Line(SCREEN_X - DISTANCE_FROM_SCREEN - PENTALTY_HORISONTAL, SCREEN_Y/2 - PENTALTY_VERTICAL/2)

        self.keeper_line_list = [penaltyline1, penaltyline2, penaltyline3, penaltyline4, penaltyline5, penaltyline6]
        goalline1 = Line(DISTANCE_FROM_SCREEN - GOAL_H , DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2)
        goalline2 = Line(DISTANCE_FROM_SCREEN - GOAL_H , DISTANCE_FROM_SCREEN + FIELD_V/2 - GOAL/2)
        goalline3 = Line(DISTANCE_FROM_SCREEN - GOAL_H, DISTANCE_FROM_SCREEN + FIELD_V/2 - GOAL/2)
        goalline4 = Line(DISTANCE_FROM_SCREEN + FIELD_H, DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2)
        goalline5 = Line(DISTANCE_FROM_SCREEN + FIELD_H, DISTANCE_FROM_SCREEN + FIELD_V/2 - GOAL/2)
        goalline6 = Line(DISTANCE_FROM_SCREEN + FIELD_H + GOAL_H, DISTANCE_FROM_SCREEN + FIELD_V/2 - GOAL/2)


        upperline.draw(self.screen, HORISONTAL, FIELD_H)
        lowerline.draw(self.screen, HORISONTAL, FIELD_H)
        
        leftlineupper.draw(self.screen, VERTICAL, FIELD_V/2 - GOAL/2)
        leftlinelower.draw(self.screen, VERTICAL, FIELD_V/2 - GOAL/2)
        rigthlineupper.draw(self.screen, VERTICAL, FIELD_V/2 - GOAL/2)
        rigthlinelower.draw(self.screen, VERTICAL, FIELD_V/2 - GOAL/2)
        midline.draw(self.screen, VERTICAL, FIELD_V)


        pygame.draw.circle(self.screen, THECOLORS["white"], (int(SCREEN_X/2), int(SCREEN_Y/2)), 90, 3)
        penaltyline1.draw(self.screen, HORISONTAL,  PENTALTY_HORISONTAL)
        penaltyline2.draw(self.screen, HORISONTAL, PENTALTY_HORISONTAL)
        penaltyline3.draw(self.screen, HORISONTAL,  PENTALTY_HORISONTAL)
        penaltyline4.draw(self.screen, HORISONTAL, PENTALTY_HORISONTAL)
        penaltyline5.draw(self.screen, VERTICAL,  PENTALTY_VERTICAL)
        penaltyline6.draw(self.screen, VERTICAL,  PENTALTY_VERTICAL)

        goalline1.draw(self.screen, HORISONTAL, GOAL_H)
        goalline2.draw(self.screen, HORISONTAL, GOAL_H)
        goalline3.draw(self.screen, VERTICAL,  GOAL)

        goalline4.draw(self.screen, HORISONTAL,  GOAL_H)
        goalline5.draw(self.screen, HORISONTAL,  GOAL_H )
        goalline6.draw(self.screen, VERTICAL,  GOAL)

        goal1.draw(self.screen, VERTICAL, GOAL, THECOLORS['black'])
        goal2.draw(self.screen, VERTICAL, GOAL, THECOLORS['pink'])

    
    def add_players(self):
        player1red = Keeper(KEEPER_RED_POS.x, KEEPER_RED_POS.y,  PLAYER_RADIUS, THECOLORS["red"], 1, RED)
        player2red = Player(RED_PLAYER2.x, RED_PLAYER2.y, PLAYER_RADIUS, THECOLORS["red"], 2, RED)
        player3red = Player(RED_PLAYER3.x, RED_PLAYER3.y, PLAYER_RADIUS, THECOLORS["red"], 3, RED)
        player4red = Player(RED_PLAYER4.x, RED_PLAYER4.y, PLAYER_RADIUS, THECOLORS["red"], 4, RED)

        player1blue = Keeper(KEEPER_BLUE_POS.x, KEEPER_BLUE_POS.y, PLAYER_RADIUS, THECOLORS["blue"], 12, BLUE)
        player2blue = Player(BLUE_PLAYER2.x, BLUE_PLAYER2.y, PLAYER_RADIUS, THECOLORS["blue"], 13, BLUE)
        player3blue = Player(BLUE_PLAYER3.x, BLUE_PLAYER3.y, PLAYER_RADIUS, THECOLORS["blue"], 14, BLUE)
        player4blue = Player(BLUE_PLAYER4.x, BLUE_PLAYER4.y, PLAYER_RADIUS, THECOLORS["blue"], 15, BLUE)

        self.red.add_player(player1red)
        self.red.add_player(player2red) 
        self.red.add_player(player3red)
        self.red.add_player(player4red)

        self.blue.add_player(player1blue)
        self.blue.add_player(player2blue)
        self.blue.add_player(player3blue)
        self.blue.add_player(player4blue)


    def draw_all(self):
        for team in self.teams:
            for player in team.players:
                player.draw(self.screen)
        self.ball_list[0].draw(self.screen)

    def move_all_players(self):
        redgoal = self.goalline_list[0]
        bluegoal = self.goalline_list[1]
        ball = self.ball_list[0]
        for team in self.teams:
            for player in team.players:
                # Can not cross other players
                player.personal_space(self.red.players)
                player.personal_space(self.blue.players)

                teammate = player.team_has_ball(team.players)
                if not teammate:
                    player.move_to_ball(ball, 1000)
                    if player._has_ball == True:
                        if player in self.red.players:
                            goal = bluegoal
                            distance_to_goal = player.pos.get_distance(goal.pos)
                            if  distance_to_goal < VIEW_DISTANCE:
                                mate = player.find_free_teammate(self.teams, RED)
                                if mate:
                                    player.pass_ball(mate, ball)
                            if distance_to_goal < SHOOT_DISTANCE:
                                player.shoot(goal, ball)
                        else:
                            goal = redgoal
                            distance_to_goal = player.pos.get_distance(goal.pos)
                            if  distance_to_goal < VIEW_DISTANCE:
                                mate = player.find_free_teammate(self.teams, BLUE)
                                if mate:
                                    player.pass_ball(mate, ball)
                            if distance_to_goal < SHOOT_DISTANCE:
                                player.shoot(goal, ball)
                
                # If our team has the ball
                if teammate:
                    if teammate.team == RED:
                        goal = bluegoal
                    else:
                        goal = redgoal

                    player.find_free_space(teammate, goal)
                # If our team does not have the ball
        ball.move()

    def rules(self):
        redgoal = self.goalline_list[0]
        bluegoal = self.goalline_list[1]
        
        if self.ball_list[0].is_goal(redgoal):
            print("goal to blue")
            self.bluegoals += 1
            self.reset()
            print("Score is {}:{}".format(self.bluegoals, self.redgoals))

        if self.ball_list[0].is_goal(bluegoal):
            print("goal to red")
            self.redgoals += 1
            self.reset()
            print("Score is {}:{}".format(self.bluegoals, self.redgoals))

        for line in self.sidelines_list:
            if self.ball_list[0].is_throwin(line):
                print("Throwin, reseting")
                self.reset()
        for line in self.vertical_list:
            if self.ball_list[0].is_corner(line):
                print("Corner, reseting")
                self.reset()
        
    def reset(self):
        self.red.remove_all()
        self.blue.remove_all()
        self.ball_list.clear()

        self.add_players()
        ball = Ball(random.uniform(0.75, 1.25)*BALL_POS.x, BALL_POS.y, 6, THECOLORS["yellow"])
        self.ball_list.append(ball)
    

    def event_handler(self):
        """
        A funtion that handle all the events the user is putting in.
        can only end the program.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.reset()
    def scoreboard(self):
        font = pygame.font.Font('freesansbold.ttf', 32) 
  
        text = font.render("Red {} | Blue {}".format(self.redgoals, self.bluegoals), True, THECOLORS["black"], THECOLORS["white"]) 
        
        textRect = text.get_rect()  

        textRect.center = (SCREEN_X // 2, 20)
        self.screen.blit(text, textRect)  

    def run(self):
        """
        The run function that runs all the other functions together and
        make the program "run"
        """
        pygame.init()
        pygame.display.set_caption("ROBOCUP")
        clock = pygame.time.Clock()
        
                
        while True:
            clock.tick(FPS)
            self.event_handler()
            self.draw_field()
            self.draw_all()
            self.move_all_players()
            self.rules()
            

            self.scoreboard()
            pygame.display.update()


if __name__ == "__main__":
    p = Program()
    p.run()
