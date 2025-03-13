from circleshape import *
import pygame
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self)
        self.add(self.containers)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),(self.position),self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def rotate(self, dt):
        self.rotation += PLAYER_SHOOT_SPEED * dt