from rules import *


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

        self.boid_list      = []                        # a list of boids
        self.hoik_list      = []                        # a list of hoiks
        self.obstacle_list   = []                       # a list of obstacles
        self.add_all()                                  # a add_all function
        self.draw_all()                                 # a draw_all function
        self.event_handler()                            # a event handler function
        self.move_all_boids_to_new_positions()          # a moving function for boids
        self.move_all_hoiks_to_new_positions()          # a moving function for hoiks




        self.run()                                      # the run function that runs all the functions together

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
        self.screen.fill(THECOLORS['darkgreen'])


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

        while True:
            self.clock.tick(FPS)
            self.event_handler()
            self.draw_all()
            aline = Line()
            aline.draw(self.screen)
            self.move_all_boids_to_new_positions()
            self.move_all_hoiks_to_new_positions()


if __name__ == "__main__":
    p = Program()
    p.run()
