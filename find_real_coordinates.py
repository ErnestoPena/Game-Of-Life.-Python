import pygame

def real_coord(raw_coord):

    x,y = raw_coord

    x_coord_return = 0
    y_coord_return = 0

    xstring = str(x)
    ystring = str(y)

    if len(str(x)) == 1:
        x_coord_return = 1
    elif len(str(x)) == 2:
        x_coord_return = int((xstring[0]) + '0')   
    elif len(str(x)) == 3:
        x_coord_return = int((xstring[0:2]) + '0')  

    if len(str(y)) == 1:
        y_coord_return = 1
    elif len(str(y)) == 2:
        y_coord_return = int((ystring[0]) + '0')   
    elif len(str(y)) == 3:
        y_coord_return = int((ystring[0:2]) + '0')  

    return (x_coord_return, y_coord_return)          