# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
pygame.init()
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
dt=0
clock=pygame.time.Clock()


def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers=(updatable,drawable)
    AsteroidField.containers=(updatable)
    Shot.containers = (shots,updatable,drawable)
    asteroid_field=AsteroidField()
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while True:
        #Allows for the close button to work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Below is the code that allows the screen to be drawn
        pygame.Surface.fill(screen,"black")
        #making computer speed independent of refresh speed.
        clock.tick(60)
        dt=clock.tick(60)/1000
        #draws the player character, using groups to do so
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        #allows for rotation and movement, will be using groups now
        for object in updatable:
            object.update(dt)
        for object in asteroids:
            if object.collision(player):
                print("Game Over!")
                return

#making sure the code only runs when "python3 main.py" is run, not any modules which may have the main function imported into them
if __name__ == "__main__":
    main()