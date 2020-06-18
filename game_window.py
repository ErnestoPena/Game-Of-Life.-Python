# Importing pygame module
import pygame

# class window:
#     def __init__(self, width , heigth):
#         self.width = width
#         self.heigth = heigth

# Function to create app window
def myscreen(width , heigth):
    game_window = pygame.display.set_mode([width, heigth], )
    return game_window