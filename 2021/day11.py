import sys
import pathlib
from parse import parse
import numpy as np


def simulate(data, n):
    """
    Simulate on data for n steps and keep track of flash count and 
    the first time step that all cells will flash at the same time.
    """
    grid = np.array([list(line) for line in data], dtype=np.int32)
    
    num_flashes = 0
    all_flashes_t = 0

    for t in range(n):
        # add 1 to every cell
        grid += 1
        # boolean for every cell
        flashed = np.zeros_like(grid)
        # is this step done (no more flashes)
        done = False
        while not done:
            done = True
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    # do the flash
                    if grid[row, col] > 9 and not flashed[row, col]:
                        flashed[row, col] = 1
                        done = False
                        num_flashes += 1
                        # +1 for every adjacent cell
                        for dir in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]:
                            new_row = row + dir[0]
                            new_col = col + dir[1]
                            if 0 <= new_row <= len(grid)-1 and 0 <= new_col <= len(grid[0])-1:
                                grid[new_row, new_col] += 1        
        
        # finally zero all cells that are over 9 (they have flashed already)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row, col] > 9:
                    grid[row, col] = 0
        
        # store the first time that all values are zero
        if grid.sum() == 0 and all_flashes_t == 0:
            all_flashes_t = t+1

    return num_flashes, all_flashes_t

def part1(data):
    return simulate(data, 200)[0]

def part2(data):
    return simulate(data, 500)[1]

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)