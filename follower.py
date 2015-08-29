import pygame
import math
from PID import PIDController

class Follower:
    def __init__(self):
        self.px = 0
        self.py = 0
        self.vx = 0
        self.vy = 0
        self.radius = 30
        self.color = (10,100,230)
        self.pid_controller = PIDController()

    def update(self,time_passed,mouse_position):
        # the mouse's position is the setpoint
        # the follower's position is the current value
        current_value = (self.px,self.py)
        self.vx, self.vy = self.pid_controller.get_u(mouse_position,current_value)

        self.px = int(self.px + self.vx*time_passed)
        self.py = int(self.py + self.vy*time_passed)

    def render(self,screen):
        pygame.draw.circle(screen,self.color,(self.px,self.py),self.radius)
