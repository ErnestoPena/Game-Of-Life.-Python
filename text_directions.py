import pygame

def print(text, window):   
        font = pygame.font.SysFont('Times New Roman', 18)
        header_text = font.render(text,1,(255,255,0))
        window.blit(header_text, (1000 + (200/2 - header_text.get_width()/2), 680 + (header_text.get_height()/2)))        