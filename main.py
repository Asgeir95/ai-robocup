from rules import *
from variables import *
from objects import *

class Program:
    """
    The class for the program that runs all the files together
    """
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("ROBOCUP")
        self.screen     = pygame.display.set_mode(SCREEN_SIZE)
        self.clock      = pygame.time.Clock()

        self.sidelines_list = []
        self.vertical_list = []
        self.goalline_list = []
        self.boid_list      = []                        # a list of boids
        self.hoik_list      = []                        # a list of hoiks
        self.obstacle_list   = []                       # a list of obstacles
        self.add_all()                                  # a add_all function
        self.draw_all()                                 # a draw_all function
     
        self.run()                                      # the run function that runs all the functions together

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
        """
        A function that add all the objects to lists and appending the
        objects
        """
        for i in range(NUMBER_OF_BOIDS):
            self.boid_list.append(Boid())

        for i in range(NUMBER_OF_HOIKS):
            self.hoik_list.append(Hoik())

        for i in range(NUMBER_OF_OBSTACLES):
            self.obstacle_list.append(Obstacle())

    def draw_all(self):
        """
        A function that first draws the screen,
        and then draws all the objects in the screen
        """
        self.screen.fill(THECOLORS['darkgreen'], None, )


        for boid in self.boid_list:
            boid.draw(self.screen)

        for hoik in self.hoik_list:
            hoik.draw(self.screen)

        for obstacle in self.obstacle_list:
            obstacle.draw(self.screen)

    def move_all_boids_to_new_positions(self):
        """
        A function that put all the rules for the boids together and
        then moves the boid with those rules.
        """
        for b in self.boid_list:
            v1 = Rule1(self.boid_list, b)
            v2 = Rule2(self.boid_list, b)
            v3 = Rule3(self.boid_list, b)
            v4 = Rule4(self.hoik_list, b)
            v5 = Rule5(self.obstacle_list, b)

            b.speed += v1 + v2 + v3 + v4 + v5
            b.move()

        pygame.display.update()

    def move_all_hoiks_to_new_positions(self):
        """
        A function that put all the rules for the hoiks together and
        then moves the boid with those rules.
        """
        for h in self.hoik_list:
            v1 = Hoik_Rule1(self.boid_list, h)
            v2 = Hoik_Rule2(self.hoik_list, h)
            v3 = Rule5(self.obstacle_list, h)

            h.speed += v1 + v2 + v3
            h.move()

        pygame.display.update()

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
        image = pygame.transform.scale(pygame.image.load("images/blue.png"), (10, 10))
        blue = Player(image, 100, 100)
        l = pygame.sprite.Group()
        l.add(blue)
        l.draw(self.screen)    
        while True:
            self.clock.tick(FPS)
            self.event_handler()
            self.draw_all()
            self.draw_field()
            l.update()
            self.move_all_boids_to_new_positions()
            self.move_all_hoiks_to_new_positions()


if __name__ == "__main__":
    p = Program()
    p.run()
