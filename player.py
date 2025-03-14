from circleshape import *
from shot import *
from constants import (
    PLAYER_RADIUS, 
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    SHOT_RADIUS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN
)
import pygame

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self)
        self.rotation = 0
        self.shoot_cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            #print("you are pressing the key K_a")
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            #print("you are presing the key K_d")
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.shoot_cooldown <= 0:
            shot_obj = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            direction = pygame.Vector2(0,1)
            direction = direction.rotate(self.rotation)
            shot_obj.velocity = direction * PLAYER_SHOOT_SPEED
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        else:
            self.shoot_cooldown -= dt