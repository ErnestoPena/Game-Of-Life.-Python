# Importing required modules
import sys
import os
import pygame
import game_window
import game_grid
import live_object
import side_panel
import buttons
import load_music
import app_credits
import mouse_menu

# https://www.melodyloops.com/

# Initializing pygame
pygame.init()

# Setting the caption for the Main window
pygame.display.set_caption("Game of Life. Lambdaschool Computer Science Project 1")

# Setting the window properties. I can refine this code to obtain the display resolution 
# but I will leave that for another time. There are complexities associated in accomplishing this
# multi display enviroments and different OS.
CURRENT_PATH = os.path.dirname(__file__)
SCREEN_HEIGTH = 1000
SCREEN_WIDTH = 1200
SIDE_P_WIDTH = 200
SIDE_P_HEIGTH = 1000
BACKGROUND = "FFFFFF"
SQUARE_W = 100
SQUARE_H= 100

load_music.music(True , CURRENT_PATH)

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


# Font and Text for the Menu Header
font = pygame.font.SysFont('Times New Roman', 20)
header_text = font.render("Menu",1,(255,255,255))
new_window.blit(header_text, (1000 + (200/2 - header_text.get_width()/2), 5))

# Draw a separation line menu - buttons
pygame.draw.line(new_window, (255,255,255), (1000, 30) , (1200,30))

# Creating the buttons
game_rules = buttons.buttonsClass(100, 40, 1050, 50, "Game Rules", (255,255,255))
draw_pattern = buttons.buttonsClass(100, 40, 1050, 110, "Draw Pattern", (255,255,255))
start_stop = buttons.buttonsClass(100, 40, 1050, 170, "Start/Stop", (255,255,255))
clear = buttons.buttonsClass(100,40, 1050, 230, "Clear All", (255,255,255))
app_credits = buttons.buttonsClass(100,40, 1050, 290, "App Credits", (255,255,255))

# Draw buttons
game_rules.create_button(new_window, (144,238,144)) 
draw_pattern.create_button(new_window, (144,238,144))
start_stop.create_button(new_window, (144,238,144))
clear.create_button(new_window, (144,238,144))
app_credits.create_button(new_window, (144,238,144))

# Draw a separation line buttons - statistics
pygame.draw.line(new_window, (255,255,255), (1000, 350) , (1200,350))

# Font and Text for the Header
font = pygame.font.SysFont('Times New Roman', 20)
header_text = font.render("Statistics",1,(255,255,255))
new_window.blit(header_text, (1000 + (200/2 - header_text.get_width()/2), 343 + (header_text.get_height()/2)))

# Draw a separation line buttons - statistics
pygame.draw.line(new_window, (255,255,255), (1000, 380) , (1200,380))

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
    pygame.display.update()
    # Chequing for mouse and key press events
    for x in pygame.event.get():
        
        # Statement to constantly get the mouse coordinates
        mouse_position = pygame.mouse.get_pos()

        # If statement to quit the app
        if x.type == pygame.QUIT:
            program_is_runing = False
            pygame.quit()
            quit()

        # IF statement to control mouse on menu
        mouse_result = mouse_menu.mouse_over_menu(mouse_position)
        if x.type == pygame.MOUSEMOTION:
            if mouse_result == None:
                game_rules.create_button(new_window, (144,238,144))
                draw_pattern.create_button(new_window, (144,238,144))
                start_stop.create_button(new_window, (144,238,144))
                clear.create_button(new_window, (144,238,144))
                app_credits.create_button(new_window, (144,238,144))
        
            elif mouse_result == 1:
                game_rules.create_button(new_window, (189,183,107)) 
            elif mouse_result == 2:
                draw_pattern.create_button(new_window, (189,183,107)) 
            elif mouse_result == 3:
                start_stop.create_button(new_window, (189,183,107)) 
            elif mouse_result == 4:
                clear.create_button(new_window, (189,183,107))    
            elif mouse_result == 5:
                app_credits.create_button(new_window, (189,183,107))     


        # Describe other

    
    run()  