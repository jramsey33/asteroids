# this allows us to use code from
# the open-source pygame library
# throught this file

import pygame
from constants import *


def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        pygame.Surface.fill(screen, color=(0,0,0))
        pygame.display.flip()


pygame.quit











if __name__ == "__main__":
    main()