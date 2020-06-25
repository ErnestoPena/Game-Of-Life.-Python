import sys
import pygame

def grid(rows_width, columns_heigth, game_window):
    game_window.fill(pygame.Color("white"), (0, 0, 999, 999))
    for row in range(0, 101):
        pygame.draw.line(game_window, (0,0,0), [0,row*10], [1000,row*10]) 
        row = row + 10

        for col in range(1, 101):
            pygame.draw.line(game_window, (0,0,0), (col*10, 0 ), (col*10,1000))     
            col = col + 10            


# class grid:
#     def __init__(self, rows_width, columns_heigth):
#         self.rows_width = rows_width
#         self.columns_heigth = columns_heigth

#     def draw_grid(self, game_window):

#         for row in range(0, 101):
#             pygame.draw.line(game_window, (0,0,0), [0,row*10], [1000,row*10]) 
#             row = row + 10

#         for col in range(1, 101):
#             pygame.draw.line(game_window, (0,0,0), (col*10, 0 ), (col*10,1000))     
#             col = col + 10



