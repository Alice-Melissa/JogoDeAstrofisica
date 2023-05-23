import pygame
from pygame.locals import *
from pygame.math import Vector2
from asteroides import suprema
from cores import *
from asteroides2 import *

class suprema1:
    def __init__(suprema):
        def __init__(self, galaxy, nome, color, wireframe, width):
            super().__init__(galaxy, nome, color)
            self.wireframe = wireframe
            self.width = width
            self.angle = 0.0
            self.size = 1

        def update(self, time_passed, event_list):
            super().update(time_passed, event_list)

        def render(self, surface):
            super().render(surface)
            draw = []
            for point in self.wireframe:
                draw.append(
                    Vector2(point).rotate(self.angle) * self.size + self.position
                )
            pygame.draw.lines(surface, self.color, True, draw, self.width)
