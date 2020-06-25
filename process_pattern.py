import pygame

# Update Cell State when user clicks on grid
def update_master(coordinates, master_grid_data, count_if_live_cells_exists):
    
    coordinates.append(False)
    
    value_index = master_grid_data.index(coordinates) if coordinates in master_grid_data else None
    
    if not value_index:
        coordinates[2] = True
        value_index = master_grid_data.index(coordinates) if coordinates in master_grid_data else None

    temp_state = master_grid_data[value_index][2]

    if temp_state:
        master_grid_data[value_index][2] = False
        count_if_live_cells_exists = count_if_live_cells_exists -1
    else:
        master_grid_data[value_index][2] = True
        count_if_live_cells_exists = count_if_live_cells_exists + 1
    return (master_grid_data, master_grid_data[value_index][2], count_if_live_cells_exists)




# Function to find the status of cell neighbours 
def process_neighbours(master_grid_data):
    # The function argument  "master_grid_data" is a list of lists representing
    # cell coordinates and status 
    
    #Copying the core List into a temporary list for the double buffer
    temp_grid_list = master_grid_data

    for node_index, node in enumerate(temp_grid_list):
        #Finding the cell index and calculating neighbours indexes 
        
        #Top Left Cell
        TL = abs(node_index - 101)
        TL = temp_grid_list[TL]
        TL = TL[2]

        #Top
        T = abs(node_index - 100)
        T = temp_grid_list[T]
        T = T[2]

        #Top Right Cell
        TR = abs(node_index - 99)
        TR = temp_grid_list[TR]
        TR = TR[2]

        #Right Cell
        R = node_index + 1
        R = temp_grid_list[R]
        R = R[2]

        #Bottom Right Cell
        BR = node_index + 101
        BR = temp_grid_list[BR]
        BR = BR[2]

        #Bottom Cell
        B = node_index + 100
        B = temp_grid_list[B]
        B = B[2]

        #Bottom Left Cell
        BL = node_index + 99
        BL= temp_grid_list[BL]
        BL = BL[2]

        #Left Cell
        L = abs(node_index - 1)
        L = temp_grid_list[L]
        L = L[2]

        neighbours_tuple = (TL, T, TR, R, BR, B, BL, L)
        count_true = neighbours_tuple.count(True)
        count_false = neighbours_tuple.count(False)

        #If cell is alive, lets check if it dies or remain alive
        if node[2] and (2 <= count_true <=3):
            pass
        elif node[2] and count_true >=4:
            temp_grid_list[node_index][2] = False
        elif node[2] and count_true <= 1:
            temp_grid_list[node_index][2] = False    

        #If cell is dead, lets check if it remain dead or goes live
        if not node[2] and count_true ==3:
            temp_grid_list[node_index][2] = True

    return temp_grid_list
        
        
    