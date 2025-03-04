import pygame
from constants import *

def main():
    #This initialize the module of pygame. The library for games.
    pygame.init() 
    #We will call a function to set up the window/display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()