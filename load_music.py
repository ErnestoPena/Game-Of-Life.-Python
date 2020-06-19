import os
import pygame

def music(status, current_path):
    if status:
        music = pygame.mixer.music.load(os.path.join(current_path, 'in_my_heart.mp3'))
        pygame.mixer.music.play(-1)
    else:
        pass    