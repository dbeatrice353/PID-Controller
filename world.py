import pygame
from pygame.locals import *
from mouse import Mouse

class World:
    def __init__(self,screen_width,screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (0,0,0)
        self.mouse = Mouse()

    def update(self,time_passed):
        self.mouse.update(time_passed)

    def render(self,screen):
        screen.fill(self.background_color)
        self.mouse.render(screen)
