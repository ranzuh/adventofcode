import sys
import pathlib
import parse
import numpy as np

def part1(data):
    list_of_strings = data[0].split(',')
    positions = np.array(list_of_strings, dtype=np.int32)

    candidates = np.arange(0, positions.max())

    lowest_cost = np.inf
    for c in candidates:
        fuel_costs = np.where(positions-c >= 0, positions-c, c-positions)
        if sum(fuel_costs) < lowest_cost:
            lowest_cost = sum(fuel_costs)
            #print(fuel_costs, c)
    
    return lowest_cost

def part2(data):
    list_of_strings = data[0].split(',')
    positions = np.array(list_of_strings, dtype=np.int32)

    candidates = np.arange(0, positions.max())

    lowest_cost = np.inf
    for c in candidates:
        fuel_costs = np.where(positions-c >= 0, positions-c, c-positions)
        fuel_costs = fuel_costs*(fuel_costs+1) // 2
        if sum(fuel_costs) < lowest_cost:
            lowest_cost = sum(fuel_costs)
    
    return lowest_cost

if __name__ == "__main__":
    path = sys.argv[0][:-3] + ".txt"
    data = pathlib.Path(path).read_text().splitlines()
    output1 = part1(data)
    output2 = part2(data)
    print(output1, output2)