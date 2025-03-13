from circleshape import *
import pygame
from constants import (
    ASTEROID_MIN_RADIUS
)
import random

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self)
        self.add(self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),(self.position),self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20.0, 50.0)
            positive_ran = self.velocity.rotate(random_angle)
            negative_ran = self.velocity.rotate(-random_angle)
            #print(positive_ran)
            #print(negative_ran)
            small_radius = self.radius - ASTEROID_MIN_RADIUS
            new1_asteroid = Asteroid(
                self.position.x,
                self.position.y,
                small_radius
                )
            new2_asteroid = Asteroid(
                self.position.x,
                self.position.y,
                small_radius
                )
            new1_asteroid.velocity = positive_ran * 1.2
            new2_asteroid.velocity = negative_ran * 1.2