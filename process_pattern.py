
def process_pattern(pattern):
    # The function argument  "pattern" is a tupple of tuples representing one alive node information and the corresponding neighbours cells information states and coordinates
    # The format is ((node), (TL) , (T) , (TR) , (R) , (BR) , (B) , (BL) , (L)) where:
    # node => Node.(x,y)
    # TL   => Top Left neighbour coordinates and status.(x,y, True/False) => True for 'live cell' - False for 'dead cell'
    # T    => Top Left neighbour coordinates and status.
    # TR   => Top Left neighbour coordinates and status.
    # BR   => Top Left neighbour coordinates and status.
    # B    => Top Left neighbour coordinates and status.
    # BL   => Top Left neighbour coordinates and status.
    # L    => Top Left neighbour coordinates and status.

    grid_list = []
    for node in pattern:
        TL = (node[0]-10, node[1]-10)
        if TL in pattern:
            print()
        print(TL)
        # for y in range(0,9):
        #     pattern[x]
        #     grid_list.append((y*10 , x*10, False))

    print(tuple(grid_list))
