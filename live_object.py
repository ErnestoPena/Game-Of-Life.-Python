# This is the function that will draw the live/dead objets

import sys
import pygame

def print_cell(image_to_load, x , y, width , height, screen , map_object, status):
    live, dead = image_to_load

    if status:
        image_to_load = live
    else:
        image_to_load = dead     

    image_to_load = pygame.image.load(image_to_load)
    image_to_load = pygame.transform.scale(image_to_load, (width , height))
    screen.blit(image_to_load, [x+1, y+1])        