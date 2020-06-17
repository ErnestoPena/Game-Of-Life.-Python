# Importing required modules
import sys
import pygame
import game_map
import live_object

# Initializing pygame
pygame.init()

# Setting the caption for the Main window
pygame.display.setcaption("Gae of Life. Lambdaschool Computer Science Project 1")

# Setting the window properties. I can refine this code to obtain the display resolution 
# but I will leave that for another time. There are complexities associated in accomplishing this
# multi display enviroments and different OS.

SCREEN_HEIGTH = 1000
SCREEN_WIDTH = 1000

#Set the state of our program
program_is_runing = True

class gameoflife:
    def __init__(self):
        pass

# Main program loop
while program_is_runing:

    # Chequing for mouse and key press events
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            program_is_runing = False
        # Describe other


    newmap = game_map.myscreen()