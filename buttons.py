import pygame

class buttonsClass:
    def __init__(self, width, height, x, y, text, window):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.window = window

    def create_button(self, outline):
        self.outline = outline

        # Creating the rectangle
        pygame.draw.rect(self.window, self.outline, (self.x, self.y, self.width, self.height),0)
        
        # Font and Text for the buttons
        font = pygame.font.SysFont('Times New Roman', 16)
        text = font.render(self.text,1,(0,0,0))
        self.window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def hover_state(self, coordinates):
        self.coordinates = coordinates

        if (self.x <= self.coordinates[0] <= (self.x + self.width)) and (self.y <= self.coordinates[1] <= (self.y + self.height)):    
            return True
        else:
            return False


    def change_color_on_click(self,  color):
        self.color = color

        if self.hover_state and self.color == self.color[0]:
            self.color = self.color[1]
            self.create_button(self.color)
            return True
        elif self.hover_state and self.color == self.color[1]:
            self.color = self.color[0]
            self.create_button(self.color)
            return False

    def change_color_on_hover(self, is_hover):
        self.is_hover = is_hover 

        if is_hover:
            color = (189,183,107)
        else:
            color = (144,238,144)

        self.create_button(color)         


