# Importing required modules
import sys
import os
import pygame

# Importing App modules
import game_window
import game_grid
import live_object
import side_panel
import buttons
import load_music
import app_credits
import mouse_menu
import rules_message
import grid_tuple
import process_pattern

# https://www.melodyloops.com/

# Initializing pygame
pygame.init()

#hold_grid_data = grid_tuple.construct_main_tuple()


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
game_rules_pressed = False
draw_pattern_pressed = False
start_stop_pressed = False
clear_pressed = False
app_credits_pressed = False

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
game_rules = buttons.buttonsClass(100, 40, 1050, 50, "Game Rules", new_window)
draw_pattern = buttons.buttonsClass(100, 40, 1050, 110, "Draw Pattern", new_window)
start_stop = buttons.buttonsClass(100, 40, 1050, 170, "Start/Stop", new_window)
clear = buttons.buttonsClass(100,40, 1050, 230, "Clear All", new_window)
app_credits = buttons.buttonsClass(100,40, 1050, 290, "App Credits", new_window)

# Draw buttons
game_rules.create_button((144,238,144)) 
draw_pattern.create_button((144,238,144))
start_stop.create_button((144,238,144))
clear.create_button((144,238,144))
app_credits.create_button((144,238,144))

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

#process_pattern.process_pattern(hold_grid_data)

def run():
   
    # draw the live object
    live_object.draw_object(new_window, grid)

    # update our display
    pygame.display.flip()


# Main program loop
while program_is_runing:
    pygame.display.update()
    # Chequing for mouse and key press events
    for x in pygame.event.get():
        
        # Statement to constantly get the mouse coordinates
        position = pygame.mouse.get_pos()

        # If statement to quit the app
        if x.type == pygame.QUIT:
            program_is_runing = False
            pygame.quit()
            quit()

        # IF statement to control mouse on menu
        mouse_result = mouse_menu.mouse_over_menu(position)
        
        # Variables to control mouse press on buttons
        game_rules_state = game_rules.hover_state(position)
        draw_pattern_state = draw_pattern.hover_state(position)
        start_stop_state = start_stop.hover_state(position)
        clear_all_state = clear.hover_state(position)
        app_credits_state = app_credits.hover_state(position)

        print(game_rules_state)
        #mouse_click_result = mouse_menu.mouse_click_menu(position, pressed)

        # if x.type == pygame.MOUSEMOTION:
        #     if mouse_result == None and game_rules_state == False and draw_pattern_state == False and start_stop_state == False and clear_all_state == False and app_credits_state == False:
        #         game_rules.create_button((144,238,144))
        #         draw_pattern.create_button((144,238,144))
        #         start_stop.create_button((144,238,144))
        #         clear.create_button((144,238,144))
        #         app_credits.create_button((144,238,144))
        #     elif mouse_result == 1:
        #         game_rules.create_button((189,183,107)) 
        #     elif mouse_result == 2:
        #         draw_pattern.create_button((189,183,107)) 
        #     elif mouse_result == 3:
        #         start_stop.create_button((189,183,107)) 
        #     elif mouse_result == 4:
        #         clear.create_button((189,183,107))    
        #     elif mouse_result == 5:
        #         app_credits.create_button((189,183,107))     

        if x.type == pygame.MOUSEBUTTONDOWN:
            # IF Statemen to control Game Rules Mouse Click and hover events
            if (1050 <= position[0] <= 1150) and (50 <= position[1] <= 90):
                if game_rules_pressed:
                    game_rules_pressed = False
                    game_rules.create_button((189,183,107))    
                else:
                    game_rules_pressed = True
                    game_rules.create_button((144,238,144))    

            # IF Statemen to control Mouse Click events
            if (1050 <= position[0] <= 1150) and (110 <= position[1] <= 150):
                if draw_pattern_pressed:
                    draw_pattern_pressed = False
                    draw_pattern.create_button((189,183,107))    
                else:
                    draw_pattern_pressed = True
                    draw_pattern.create_button((144,238,144))       

            # IF Statemen to control Start/Stop Mouse Click and hover events
            if (1050 <= position[0] <= 1150) and (170 <= position[1] <= 210):
                if start_stop_pressed:
                    start_stop_pressed = False
                    start_stop.create_button((189,183,107))    
                else:
                    start_stop_pressed = True
                    start_stop.create_button((144,238,144))        

            # IF Statemen to control Clear Mouse Click and hover events
            if (1050 <= position[0] <= 1150) and (230 <= position[1] <= 270):
                if clear_pressed:
                    clear_pressed = False
                    clear.create_button((189,183,107))    
                else:
                    clear_pressed = True
                    clear.create_button((144,238,144))           

            # IF Statemen to control App Credits Mouse Click and hover events
            if (1050 <= position[0] <= 1150) and (290 <= position[1] <= 330):
                if app_credits_pressed:
                    app_credits_pressed = False
                    app_credits.create_button((189,183,107))    
                else:
                    app_credits_pressed = True
                    app_credits.create_button((144,238,144)) 

        # Describe other

    
    run()  