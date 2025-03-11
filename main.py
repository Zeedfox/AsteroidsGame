import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    #This initialize the module of pygame. The library for games.
    pygame.init() 

    #this suppose to be groups... of pygame... 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    #We will call a function to set up the window/display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_ship = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2),PLAYER_RADIUS)
    field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    
    #infinit loop that makes the game refresh and run
    exit_flag = 0
    while exit_flag == 0:
        #Event to stop the execution of the game
        #this is important on mac... I dont know the reason.. but it won't work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Painting the screen with black
        pygame.Surface.fill(screen, (0,0,0))
        #funtion of roting the player
        #player_ship.update(dt)
        #Print the player on the screen
        #player_ship.draw(screen)

        #this suppose to update and draw all the objects on the groups.. i dont know
        updatable.update(dt)
        for obj in drawable:
            if(obj != player_ship):
                if obj.collision_detect(player_ship):
                    print("You collided! GAME OVER!!!!!")
                    exit_flag = 1
            obj.draw(screen)
        


        #Refreshing the Screen: it is important to be on the end
        #player_ship.rotation += 1 #let's rotate xD
        pygame.display.flip()
        dt = (clock.tick(60)/1000) #this will pause the game loop

    #JUST FOR TESTING!!!!!!!! FIRST ATTEMPTS
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()