from rules import *
from variables import *
from objects import *
from ball import *
from player import *

class Program:
    """
    The class for the program that runs all the files together
    """
    def __init__(self):
        self.screen     = pygame.display.set_mode(SCREEN_SIZE)
        self.sidelines_list = []
        self.vertical_list = []
        self.goalline_list = []
        self.ball = Ball(150,150, 5, THECOLORS["yellow"])
        self.shit = Ball(750, 400, 10, THECOLORS["black"])
        self.team1_list = []

        self.add_all()                                  # a add_all function
        
    def draw_field(self):
        upperline = Line(DISTANCE_FROM_SCREEN, DISTANCE_FROM_SCREEN)
        lowerline  = Line(DISTANCE_FROM_SCREEN, SCREEN_Y - DISTANCE_FROM_SCREEN)

        self.sidelines_list.extend([upperline, lowerline])

        
        leftlineupper = Line(DISTANCE_FROM_SCREEN, DISTANCE_FROM_SCREEN)
        leftlinelower = Line(DISTANCE_FROM_SCREEN, DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2)
        rigthlineupper = Line(SCREEN_X - DISTANCE_FROM_SCREEN, DISTANCE_FROM_SCREEN)
        rigthlinelower = Line(SCREEN_X - DISTANCE_FROM_SCREEN, DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2)

        self.vertical_list.extend([leftlineupper, leftlinelower, rigthlineupper,rigthlinelower])
        
        goal1 = Line(DISTANCE_FROM_SCREEN, SCREEN_Y/2 - GOAL/2)
        goal2 = Line(DISTANCE_FROM_SCREEN + FIELD_H, SCREEN_Y/2 - GOAL/2)

        self.goalline_list.extend([goal1, goal2])


        # just drawings
        midline = Line(SCREEN_X / 2, DISTANCE_FROM_SCREEN)

        penaltyline1 = Line(DISTANCE_FROM_SCREEN, SCREEN_Y/2 + PENTALTY_VERTICAL/2)
        penaltyline2 = Line(DISTANCE_FROM_SCREEN, SCREEN_Y/2 - PENTALTY_VERTICAL/2)
        penaltyline3 = Line(SCREEN_X - DISTANCE_FROM_SCREEN, SCREEN_Y / 2 + PENTALTY_VERTICAL/2)
        penaltyline4 = Line(SCREEN_X - DISTANCE_FROM_SCREEN, SCREEN_Y / 2 - PENTALTY_VERTICAL/2)
        penaltyline5 = Line(DISTANCE_FROM_SCREEN + PENTALTY_HORISONTAL, SCREEN_Y/2 - PENTALTY_VERTICAL/2 )
        penaltyline6 = Line(SCREEN_X - DISTANCE_FROM_SCREEN - PENTALTY_HORISONTAL, SCREEN_Y/2 - PENTALTY_VERTICAL/2)

        goalline1 = Line(DISTANCE_FROM_SCREEN - GOAL_H , DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2)
        goalline2 = Line(DISTANCE_FROM_SCREEN - GOAL_H , DISTANCE_FROM_SCREEN + FIELD_V/2 - GOAL/2)
        goalline3 = Line(DISTANCE_FROM_SCREEN - GOAL_H, DISTANCE_FROM_SCREEN + FIELD_V/2 - GOAL/2)

        goalline4 = Line(DISTANCE_FROM_SCREEN + FIELD_H, DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2)
        goalline5 = Line(DISTANCE_FROM_SCREEN + FIELD_H, DISTANCE_FROM_SCREEN + FIELD_V/2 - GOAL/2)
        goalline6 = Line(DISTANCE_FROM_SCREEN + FIELD_H + GOAL_H, DISTANCE_FROM_SCREEN + FIELD_V/2 - GOAL/2)


        upperline.draw(self.screen, HORISONTAL, FIELD_H + DISTANCE_FROM_SCREEN)
        lowerline.draw(self.screen, HORISONTAL, FIELD_H + DISTANCE_FROM_SCREEN)
        leftlineupper.draw(self.screen, VERTICAL, DISTANCE_FROM_SCREEN+ FIELD_V/2 - GOAL/2)
        leftlinelower.draw(self.screen, VERTICAL, DISTANCE_FROM_SCREEN +FIELD_V)
        rigthlineupper.draw(self.screen, VERTICAL, DISTANCE_FROM_SCREEN + FIELD_V/2 - GOAL/2)
        rigthlinelower.draw(self.screen, VERTICAL, DISTANCE_FROM_SCREEN +FIELD_V)
        midline.draw(self.screen, VERTICAL, DISTANCE_FROM_SCREEN +FIELD_V)


        pygame.draw.circle(self.screen, THECOLORS["white"], (int(SCREEN_X/2), int(SCREEN_Y/2)), 90, 3)
        penaltyline1.draw(self.screen, HORISONTAL, DISTANCE_FROM_SCREEN + PENTALTY_HORISONTAL)
        penaltyline2.draw(self.screen, HORISONTAL, DISTANCE_FROM_SCREEN + PENTALTY_HORISONTAL)
        penaltyline3.draw(self.screen, HORISONTAL, SCREEN_X - DISTANCE_FROM_SCREEN - PENTALTY_HORISONTAL)
        penaltyline4.draw(self.screen, HORISONTAL, SCREEN_X- DISTANCE_FROM_SCREEN - PENTALTY_HORISONTAL)
        penaltyline5.draw(self.screen, VERTICAL, SCREEN_Y/2 + PENTALTY_VERTICAL/2)
        penaltyline6.draw(self.screen, VERTICAL, SCREEN_Y/2 + PENTALTY_VERTICAL/2)

        goalline1.draw(self.screen, HORISONTAL, DISTANCE_FROM_SCREEN)
        goalline2.draw(self.screen, HORISONTAL, DISTANCE_FROM_SCREEN)
        goalline3.draw(self.screen, VERTICAL,  DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2)

        goalline4.draw(self.screen, HORISONTAL, DISTANCE_FROM_SCREEN + FIELD_H + GOAL_H)
        goalline5.draw(self.screen, HORISONTAL, DISTANCE_FROM_SCREEN + FIELD_H + GOAL_H)
        goalline6.draw(self.screen, VERTICAL,  DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2)

        goal1.draw(self.screen, VERTICAL, DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2, THECOLORS['black'])
        goal2.draw(self.screen, VERTICAL, DISTANCE_FROM_SCREEN + FIELD_V/2 + GOAL/2, THECOLORS['black'])

    
    def add_all(self):
        
        #A function that add all the objects to lists and appending the
        #objects
       # player1 = Player(100,100, 10, THECOLORS["red"])
        player2 = Player(400,400, 10, THECOLORS["blue"])
        #self.team1_list.append(player1)
        self.team1_list.append(player2)


    def draw_all(self):
        """
        A function that first draws the screen,
        and then draws all the objects in the screen
        """
        self.screen.fill(THECOLORS['darkgreen'])
        
        for player in self.team1_list:
            player.draw(self.screen)
        
        self.ball.draw(self.screen)
        self.shit.draw(self.screen)

    
    def move_all_players(self):
        for player in self.team1_list:
            if player.catch_ball(self.ball) != True:
                player.speed -= player.move_to_ball(self.ball)
                player.move()
            else:
                #player.rotate_ball(self.ball, 90)
                self.ball.move(5)
                #print("player.pos = {}, player.angle = {}".format(player.pos, player.pos.get_angle()))
                #print("ball.pos = {}, ball.angle = {}".format(self.ball.pos, self.ball.pos.get_angle()))

            




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
            self.draw_all()
            self.draw_field()
            self.move_all_players()
            pygame.display.update()


if __name__ == "__main__":
    p = Program()
    p.run()
