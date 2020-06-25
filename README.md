# Game-Of-Life.-Python
Computer Science Build Week 1 



The rules of the game are simple, and describe the evolution of the
grid:
◮ Birth: a cell that is dead at time t will be alive at time t + 1
if exactly 3 of its eight neighbors were alive at time t.
◮ Death: a cell can die by:
◮ Overcrowding: if a cell is alive at time t + 1 and 4 or more of
its neighbors are also alive at time t, the cell will be dead at
time t + 1.
◮ Exposure: If a live cell at time t has only 1 live neighbor or no
live neighbors, it will be dead at time t + 1.
◮ Survival: a cell survives from time t to time t + 1 if and only
if 2 or 3 of its neighbors are alive at time t.
