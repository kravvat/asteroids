import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets game window size
    clock = pygame.time.Clock() # 'Clock' class will provide methods to help control a game's framerate
    
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable) # Assigns all instances of the Player to group_a & group_b
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (drawable, updatable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Spawns player at the center
    asteroid_field = AsteroidField()    

    dt = 0 # This will be a variable to store delta time

    while True: # Infinite game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Enables exiting the game by clicking on 'X'
                return
            
        updatable.update(dt) # Updates whole group

        for obj in asteroids:
            if obj.is_colliding(player) == True:
                sys.exit("Game over!")

        screen.fill("black") # Fills background with black

        for obj in drawable: # Draws whole group
            obj.draw(screen)

        pygame.display.flip() # Refreshes screen

        dt = clock.tick(60) / 1000 # 'Tick' method locks FPS to 60 and returns the number of ms since the last frame
                                   # Dividing it by 1000 converts ms to seconds
                                   # This gives us new 'dt' (delta time)


if __name__ == "__main__":
    main()
