# Importing required modules
import sys
import pygame
import game_window
import game_grid
import live_object
import side_panel
import buttons


# Initializing pygame
pygame.init()

# Setting the caption for the Main window
pygame.display.set_caption("Game of Life. Lambdaschool Computer Science Project 1")

# Setting the window properties. I can refine this code to obtain the display resolution 
# but I will leave that for another time. There are complexities associated in accomplishing this
# multi display enviroments and different OS.

SCREEN_HEIGTH = 1000
SCREEN_WIDTH = 1200
SIDE_P_WIDTH = 200
SIDE_P_HEIGTH = 1000
BACKGROUND = "FFFFFF"
SQUARE_W = 100
SQUARE_H= 100

#Set the state of our program
program_is_runing = True

# Creating the window to host the application
new_window = game_window.myscreen(SCREEN_WIDTH , SCREEN_HEIGTH)
# white background
new_window.fill([255,255,255])

# Creating the grid
grid = game_grid.grid(SQUARE_W, SQUARE_H)
grid.draw_grid(new_window)

# Creating the side panel
side_panel.side_panel(new_window)

# Creating the buttons
draw_pattern = buttons.buttonsClass(100, 40, 1050, 40, "Draw Pattern", (255,255,255))
start_stop = buttons.buttonsClass(100, 40, 1050, 100, "Start/Stop", (255,255,255))
clear = buttons.buttonsClass(100,40, 1050, 160, "Clear All", (255,255,255))

# Draw buttons
draw_pattern.create_button(new_window, (144,238,144)) 
start_stop.create_button(new_window, (144,238,144))
clear.create_button(new_window, (144,238,144))

# Draw a separation line
pygame.draw.line(new_window, (255,255,255), (1000, 230) , (1200,230))

# Creating the live object
live_object = live_object.live("alive.png",50,50,10,10)

def run():
   

    # draw the live object
    live_object.draw_object(new_window, grid)

    # update our display
    pygame.display.flip()


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

    
    run()  