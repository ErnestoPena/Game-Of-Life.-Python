import random

def construct_main_tuple():
    grid_list = []
    for y in range(0,100):
        for x in range(0,100):
            grid_list.append([x*10, y*10, False])
    return grid_list