# Importing pygame module
import pygame

# Function to create app window
def myscreen(width , heigth):
    game_window = pygame.display.set_mode([width, heigth], )
    return game_window