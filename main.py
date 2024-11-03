# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
pygame.init()
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
dt=0
clock=pygame.time.Clock()


def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        #Allows for the close button to work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Below is the code that allows the screen to be drawn
        pygame.Surface.fill(screen,"black")
        pygame.display.flip()
        clock.tick(60)
        dt=clock.tick(60)/1000

#making sure the code only runs when "python3 main.py" is run, not any modules which may have the main function imported into them
if __name__ == "__main__":
    main()