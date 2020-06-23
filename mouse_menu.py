import pygame

def mouse_over_menu(position):
    # IF Statemen to control Game Rules Mouse Click and hover events
    if (1050 <= position[0] <= 1150) and (50 <= position[1] <= 90):
        return 1    

    # IF Statemen to control Draw Patterns Mouse Click and hover events
    if (1050 <= position[0] <= 1150) and (110 <= position[1] <= 150):
        return 2    

    # IF Statemen to control Start/Stop Mouse Click and hover events
    if (1050 <= position[0] <= 1150) and (170 <= position[1] <= 210):
        return 3     

    # IF Statemen to control Clear Mouse Click and hover events
    if (1050 <= position[0] <= 1150) and (230 <= position[1] <= 270):
        return 4   

    # IF Statemen to control App Credits Mouse Click and hover events
    if (1050 <= position[0] <= 1150) and (290 <= position[1] <= 330):
        return 5
        


def mouse_click_menu(position, pressed):
    # IF Statemen to control Game Rules Mouse Click and hover events
    if (1050 <= position[0] <= 1150) and (50 <= position[1] <= 90) and pressed:
        pressed = False
        return (6,pressed)    
    else:
        pressed = True
        return (7,pressed)    

    # IF Statemen to control Draw Patterns Mouse Click and hover events
    if (1050 <= position[0] <= 1150) and (110 <= position[1] <= 150) and pressed:
        pressed = False
        return (8,pressed)
    else:
        pressed = True
        return (9,pressed)        

    # IF Statemen to control Start/Stop Mouse Click and hover events
    if (1050 <= position[0] <= 1150) and (170 <= position[1] <= 210) and pressed:
        pressed = False
        return (10,pressed)
    else:
        pressed = True
        return (11,pressed)         

    # IF Statemen to control Clear Mouse Click and hover events
    if (1050 <= position[0] <= 1150) and (230 <= position[1] <= 270) and pressed:
        pressed = False
        return (12,pressed)
    else:
        pressed = True
        return (13,pressed)       

    # IF Statemen to control App Credits Mouse Click and hover events
    if (1050 <= position[0] <= 1150) and (290 <= position[1] <= 330) and pressed:
        pressed = False
        return 14
    else:
        pressed = True
        return 15    
