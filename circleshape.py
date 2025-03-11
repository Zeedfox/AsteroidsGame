import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
    
    def draw(self, screen):
        # sub-classe must override
        pass

    def update(self, dt):
        # sub-classe must override
        pass

    def collision_detect(self, player_obj):
        danger_zone = self.radius + player_obj.radius
        #print(f"this object has....: {danger_zone}")
        #print(f"this object has....: {self.position.distance_to(player_obj.position)}")
        if danger_zone >= self.position.distance_to(player_obj.position):
            return True
        else:
            return False
