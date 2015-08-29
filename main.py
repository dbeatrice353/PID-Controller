from world import World
from pygame.locals import *
from sys import exit

import pygame
import math
import time

SCREEN_LENGTH = 580
SCREEN_WIDTH = 840

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH), 0, 32)
    clock = pygame.time.Clock()
    world = World(SCREEN_WIDTH,SCREEN_LENGTH)
    # Game loop:
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        time_passed_seconds = clock.tick()/ 1000.0

        world.update(time_passed_seconds)
        world.render(screen)

        pygame.display.update()

if __name__ == "__main__":
    main()
