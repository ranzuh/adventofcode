import sys
import pathlib
import parse
import numpy as np
from queue import Queue

def part1(data):
    data = [list(line) for line in data]
    data = np.array(data, dtype=np.int32)
    pad = np.ones((data.shape[0]+2, data.shape[1]+2)) * 9
    pad[1:data.shape[0]+1, 1:data.shape[1]+1] = data

    lowest_points = []
    for row in range(1, len(data)+1):
        for col in range(1, len(data[0])+1):
            value = pad[row, col]

            if value < pad[row+1,col] and \
                value < pad[row, col+1] and \
                value < pad[row-1, col] and \
                value < pad[row, col-1]:
                lowest_points.append(value)
    
    return np.sum(np.array(lowest_points) + 1).astype(np.int32)

def part2(data):
    data = [list(line) for line in data]
    data = np.array(data, dtype=np.int32)
    pad = np.ones((data.shape[0]+2, data.shape[1]+2)) * 9
    pad[1:data.shape[0]+1, 1:data.shape[1]+1] = data

    lowest_points = []
    for row in range(1, len(data)+1):
        for col in range(1, len(data[0])+1):
            value = pad[row, col]

            if value < pad[row+1,col] and \
                value < pad[row, col+1] and \
                value < pad[row-1, col] and \
                value < pad[row, col-1]:
                lowest_points.append((row,col))

    basin_sizes = []

    # breadth first search from lowest points until 9 is reached
    for lowest in lowest_points:
        visited = set()
        point_queue = Queue()
        point_queue.put(lowest)

        while not point_queue.empty():
            current_point = point_queue.get()
            visited.add(current_point)
            
            for direction in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                x = current_point[0] + direction[0]
                y = current_point[1] + direction[1]
                neighbor = (x, y)
                if neighbor not in visited and pad[neighbor] < 9:
                    point_queue.put(neighbor)
        
        basin_sizes.append(len(visited))
    
    basin_sizes.sort()
    return np.array(basin_sizes[-3:]).prod()    

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)