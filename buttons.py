import pygame

class buttonsClass:
    def __init__(self, width, height, x, y, text, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.color = color

    def create_button(self, window, outline):
        # Creating the rectangle
        pygame.draw.rect(window, outline, (self.x, self.y, self.width, self.height),0)
        
        # # Font and Text for the buttons
        font = pygame.font.SysFont('Times New Roman', 16)
        text = font.render(self.text,1,(0,0,0))

        window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))