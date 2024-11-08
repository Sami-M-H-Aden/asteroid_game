from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position),self.radius,2)
    def update(self,dt):
        self.position += self.velocity*dt
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        import random
        random_angle=random.uniform(20,50)
        velocity_one=self.velocity.rotate(random_angle)
        velocity_2=self.velocity.rotate(-random_angle)
        new_radius=self.radius - ASTEROID_MIN_RADIUS
        asteroid_one=Asteroid(self.position,self.position,new_radius)
        asteroid_two=Asteroid(self.position,self.position,new_radius)
        asteroid_one.velocity=velocity_one*1.2
        asteroid_two.velocity=velocity_2*1.2
    