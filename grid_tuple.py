import random

def construct_main_tuple():
    grid_list = []
    for x in range(0,101):
        for y in range(0,101):
            grid_list.append((x*10, y*10, False))
    return tuple(grid_list)