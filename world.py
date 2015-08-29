import pygame
from pygame.locals import *
from mouse import Mouse
from follower import Follower

class World:
    def __init__(self,screen_width,screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_color = (0,0,0)
        self.mouse = Mouse()
        self.follower = Follower()

    def update(self,time_passed):
        mouse_position = self.mouse.get_position()
        self.mouse.update(time_passed)
        self.follower.update(time_passed,mouse_position)

    def render(self,screen):
        screen.fill(self.background_color)
        self.mouse.render(screen)
        self.follower.render(screen)
