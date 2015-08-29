import pygame
import math

class Follower:
    def __init__(self):
        self.px = 0
        self.py = 0
        self.vx = 0
        self.vy = 0
        self.radius = 40
        self.color = (50,200,50)

    def update(self,time_passed,mouse_position):
        self.px = int(self.px + self.vx*time_passed)
        self.py = int(self.py + self.vy*time_passed)

    def render(self,screen):
        pygame.draw.circle(screen,self.color,(self.px,self.py),self.radius)
