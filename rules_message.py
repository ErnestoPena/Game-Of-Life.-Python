import pygame

def rules(new_window):
    new_window.fill(pygame.Color("black"), (5, 5, 990, 300))

    # Header
    font_header = pygame.font.SysFont('Times New Roman', 24)
    header_text = font_header.render("GAME RULES",1,(255,255,0))
    new_window.blit(header_text, (20 , 20 ))        
    

    font_header = pygame.font.SysFont('Times New Roman', 18)

    # First Rule
    text1 = font_header.render("Birth: a cell that is dead at this_generation will be alive at this_generation + 1 if exactly 3 of its eight neighbors",1,(255,255,0)) 
    text2 = font_header.render("were alive at this_generation",1,(255,255,0)) 
    
    # Second Rule
    text3 = font_header.render("Death: a cell can die by: Overcrowding: if a cell is alive at this_generation and 4 or more of its neighbors are also ",1,(255,255,0)) 
    text4 = font_header.render("alive at alive at this_generation, the cell will be dead at this_generation + 1.",1,(255,255,0)) 
     
    # Third Rule
    text5 = font_header.render("Exposure: If a live cell at this_generation has only 1 live neighbor or no live neighbors, it will be dead at this_generation + 1",1,(255,255,0)) 
     
    # Fourth Rule
    text6 = font_header.render("Survival: a cell survives from this generation to this_generation + 1  if and only if 2 or 3 of its neighbors are alive at this_generation",1,(255,255,0)) 
    
       
    new_window.blit(text1, (20 , 50 ))   
    new_window.blit(text2, (20 , 70 )) 
 
    new_window.blit(text3, (20 , 120 ))
    new_window.blit(text4, (20 , 140 ))

    new_window.blit(text5, (20 , 190 ))


    new_window.blit(text6, (20 , 240 ))
    
    pygame.display.update()    




  