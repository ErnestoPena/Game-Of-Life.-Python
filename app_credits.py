import pygame

def load_credits(screen):
    image_to_load = pygame.image.load('epena.png')
    
    # This will adjust the image size to the corresponding screen resolution
    image_to_load = pygame.transform.scale(image_to_load, (80 , 110))
    screen.blit(image_to_load, [1010, 660])

            
