from circleshape import *
import pygame

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),(self.position),self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt