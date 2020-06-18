# Importing pygame module
import pygame

class window:
    def __init__(self, width , heigth):
        self.width = width
        self.heigth = heigth

    # Function to create app window
    def myscreen(self):
        game_window = pygame.display.set_mode([self.width, self.heigth], )
        return game_window