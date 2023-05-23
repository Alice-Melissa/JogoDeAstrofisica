from asteroides1 import suprema1
from random import random
from pygame.math import Vector2
from cores import *

width = (230, 237, 232)
scale_factor = 3
asteroid_wireframe = [
    Vector2(-20.0, 20.0), Vector2(-25.0, 5.0), Vector2(-25.0, -10.0),
    Vector2(-5.0, -10.0), Vector2(-10.0, -20.0), Vector2(5.0, -20.0),
    Vector2(20.0, -10.0), Vector2(20.0, -5.0), Vector2(0.0, 0.0),
    Vector2(20.0, 10.0), Vector2(10.0, 20.0), Vector2(0.0, 15.0)
]

class asteroides0(suprema1):
    def __init__(self, galaxy):
        super().__init__(galaxy, 'asteroide', white, asteroid_wireframe, width)
        self.position = Vector2(random()*self.galaxy.rect.width, random()*self.galaxy.rect.height)
        self.size = scale_factor

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

    def render(self, surface):
        super().render(surface)