# this allows us to use code from
# the open-source pygame library
# throught this file

import pygame, player
from constants import *


def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p = player.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        p.draw(screen)
        pygame.display.flip()
        
        #limit frames to 60fps
        dt = clock.tick(60) / 1000












if __name__ == "__main__":
    main()