def construct_main_tuple():
    grid_list = []
    for x in range(0,100):
        for y in range(0,100):
            grid_list.append((y*10 , x*10, "False"))

    return tuple(grid_list)