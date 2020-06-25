# This is the class that will create the live objets
# Importing required modules

import sys
import pygame

class live:
    def __init__(self, image_to_load, x , y, width , height):
        self.image_to_load = pygame.image.load(image_to_load)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.objects_coordinates = objects_coordinates
        
        # This will adjust the image size to the corresponding screen resolution
        self.image_to_load = pygame.transform.scale(self.image_to_load, (self.width , self.height))

    def draw_object(self, screen , map_object):
        #for x in self.objects_coordinates:
        screen.blit(self.image_to_load, [self.x, self.y])