import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets game window size

    clock = pygame.time.Clock() # 'Clock' class will provide methods to help control a game's framerate
    dt = 0 # This will be a variable to store delta time

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Spawns player at the center

    while True: # Infinite game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Enables exiting the game by clicking on 'X'
                return
            
        screen.fill("black") # Fills background with black
        player.draw(screen) # Re-renders the player
        pygame.display.flip() # Refreshes screen

        dt = clock.tick(60) / 1000 # 'Tick' method locks FPS to 60 and returns the number of ms since the last frame
                                   # Dividing it by 1000 converts ms to seconds
                                   # This gives us new 'dt' (delta time)


if __name__ == "__main__":
    main()
