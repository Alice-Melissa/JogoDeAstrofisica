import pygame
from pygame.locals import *
from cores import *
from asteroides3 import *
from asteroides2 import *
from asteroides import *
from asteroides1 import *

color_dept = 8
fps = 50
numero_de_asteroides = 7

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(flags = pygame.FULLSCREEN, depth = color_dept)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Asteroids arcade game')
        self.clock = pygame.time.Clock()

    def run(self):
        self.galaxy = galaxy(self.screen_rect)
        for i in range(numero_de_asteroides):
            self.galaxy.add_entidade(asteroides0(self.galaxy))

        done = False
        while not done:

            event_list = pygame.event.get()
            for event in event_list:
                if event.type == KEYDOWN and event.key == K_q or event.type == QUIT:
                    done = True

            time_passed = self.clock.tick(fps)


            self.galaxy.update(time_passed, event_list)
            self.galaxy.render(self.screen)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    Game().run()