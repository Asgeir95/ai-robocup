from rules import *
from variables import *
from objects import *
from ball import *
from player import *
import random
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
        self.ball = Ball(SCREEN_X/2 - 100,SCREEN_Y/2, 6, THECOLORS["yellow"])
        self.team1_list = []
        self.team2_list = []
        self.teams = [self.team1_list, self.team2_list]




        self.draw_field()
        self.add_all()                     
        
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

    
    def add_all(self):
        player1red = Keeper(KEEPER_RED_POS.x, KEEPER_RED_POS.y,  10, THECOLORS["red"], 1)
        player2red = Player(SCREEN_X / 2 - 200, SCREEN_Y/2 - 100, 10, THECOLORS["red"], 2)
        player3red = Player(SCREEN_X / 2 - 200, SCREEN_Y/2 + 100, 10, THECOLORS["red"], 3)

        player1blue = Keeper(KEEPER_BLUE_POS.x, KEEPER_BLUE_POS.y, 10, THECOLORS["blue"], 1)
        player2blue = Player(SCREEN_X / 2 + 200, SCREEN_Y/2 - 100, 10, THECOLORS["blue"], 2)
        player3blue = Player(SCREEN_X / 2 + 200, SCREEN_Y/2 + 100, 10, THECOLORS["blue"], 3)

        self.team1_list.extend([player1red, player2red, player3red])
        self.team2_list.extend([player1blue, player2blue, player3blue])


    def draw_all(self):
        for player in self.team1_list:
            player.draw(self.screen)
        
        for player in self.team2_list:
            player.draw(self.screen)

        self.ball.draw(self.screen)

    def move_all_players(self):
        for team in self.teams:
            for player in team:
                # Can not cross other players
                player.personal_space(self.team1_list)
                player.personal_space(self.team2_list)
                if type(player) is Keeper:
                    print("keeper: ", player.number)
                    if player in self.team1_list:
                        distance = (player.pos - KEEPER_RED_POS).get_length()
                        if distance > 50:
                            player.speed *= -1

                if player.pos.get_distance(self.ball.pos) <= 400:
                    if not player.has_ball(self.ball):
                        player._has_ball = False
                        player.speed += player.move_to_ball(self.ball)
                        player.move()
                    else:
                        player._has_ball = True
                        #player.rotate_ball(self.ball, 90)
                        if player in self.team1_list:
                            goalpos = self.goalline_list[1].pos
                        else: 
                            goalpos = self.goalline_list[0].pos
                        direction = (goalpos - self.ball.pos).normalized()
                        self.ball.speed += direction * player.speed.get_length() 
        self.ball.move()
    def event_handler(self):
        """
        A funtion that handle all the events the user is putting in.
        can only end the program.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def run(self):
        """
        The run function that runs all the other functions together and
        make the program "run"
        """
        pygame.init()
        pygame.display.set_caption("ROBOCUP")
        clock      = pygame.time.Clock()
        
        while True:
            clock.tick(FPS)
            self.event_handler()
            self.draw_field()
            self.draw_all()
            self.move_all_players()
            pygame.display.update()


if __name__ == "__main__":
    p = Program()
    p.run()
